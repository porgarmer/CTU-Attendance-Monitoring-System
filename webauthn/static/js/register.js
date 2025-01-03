async function registerWebAuthn() {
    const response = await fetch("/webauthn/register/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
    });
    const { registration_data } = await response.json();

    const credential = await navigator.credentials.create({
        publicKey: registration_data,
    });

    await fetch("/webauthn/register/complete/", {
        method: "POST",
        body: JSON.stringify(credential),
        headers: { "Content-Type": "application/json" },
    });
}