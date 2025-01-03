import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WebAuthnCredential

# Create your views here.
from fido2.server import Fido2Server
from fido2.webauthn import PublicKeyCredentialRpEntity

# Define the Relying Party (RP)
rp = PublicKeyCredentialRpEntity("localhost", "fingerprint-scan")
fido2_server = Fido2Server(rp)

# Registration Challenge View
@csrf_exempt
def webauthn_register(request):
    if request.method == "POST":
        user = request.user
        user_id = str(user.id).encode()
        user_name = user.username

        # Generate registration challenge
        registration_data, state = fido2_server.register_begin(
            {
                "id": user_id,
                "name": user_name,
                "displayName": user_name,
            },
            user_verification="discouraged",
        )
        request.session["state"] = state  # Save state for verification later
        return JsonResponse({"registration_data": registration_data})
    
@csrf_exempt
def webauthn_register_complete(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        state = request.session.pop("state", None)

        # Verify the registration response
        auth_data = fido2_server.register_complete(state, data["clientData"], data["attestationObject"])

        # Save the credential
        WebAuthnCredential.objects.create(
            user=request.user,
            credential_id=auth_data.credential_id,
            public_key=auth_data.credential_public_key,
            sign_count=auth_data.sign_count,
        )

        return JsonResponse({"status": "ok"})
    
    
@csrf_exempt
def webauthn_authenticate(request):
    if request.method == "POST":
        user = request.user
        credentials = [
            {"id": cred.credential_id, "transports": ["usb", "ble", "nfc"]}
            for cred in user.webauthn_credentials.all()
        ]
        auth_data, state = fido2_server.authenticate_begin(credentials)
        request.session["state"] = state
        return JsonResponse({"auth_data": auth_data})
    
@csrf_exempt
def webauthn_authenticate_complete(request):
    if request.method == "POST":
        import json
        data = json.loads(request.body)
        state = request.session.pop("state", None)

        # Retrieve the credential from the database
        credential = WebAuthnCredential.objects.get(credential_id=data["id"])

        # Verify authentication
        fido2_server.authenticate_complete(
            state,
            credential.public_key,
            credential.sign_count,
            data["clientData"],
            data["authenticatorData"],
            data["signature"],
        )

        # Update the sign count
        credential.sign_count = data["authenticatorData"]["signCount"]
        credential.save()

        return JsonResponse({"status": "ok"})