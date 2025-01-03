async function authenticateWebAuthn() {
    const response = await fetch("/webauthn/authenticate/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
    });
    const { auth_data } = await response.json();

    const assertion = await navigator.credentials.get({
        publicKey: auth_data,
    });

    await fetch("/webauthn/authenticate/complete/", {
        method: "POST",
        body: JSON.stringify(assertion),
        headers: { "Content-Type": "application/json" },
    });
}