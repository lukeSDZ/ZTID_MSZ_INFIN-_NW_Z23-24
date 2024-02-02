const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");
const passwordErrorMsg = document.getElementById("password-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // Walidacja hasła
    // Haslo musi zawierac Wielka litere, jedna cyfre
    // oraz miec ponad 6 znakow
    
    const hasUpperCase = /[A-Z]/.test(password);
    const hasLowerCase = /[a-z]/.test(password);
    const hasNumber = /\d/.test(password);

    if (!hasUpperCase || !hasLowerCase || !hasNumber || password.length < 6) {
        passwordErrorMsg.style.opacity = 1;
    } else {
        passwordErrorMsg.style.opacity = 0;
        alert("You have successfully logged in.");
        location.reload();
    }
});

