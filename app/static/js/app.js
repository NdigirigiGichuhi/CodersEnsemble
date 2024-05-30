document.addEventListener("DOMContentLoaded", function() {
    function checkAuthStatus() {
        return fetch('/auth-status')
            .then(response => response.json())
            .then(data => data.isAuthenticated);
    }

    function renderButtons(isAuthenticated) {
        const authButtonsDiv = document.getElementById('auth-buttons');

        if (isAuthenticated) {
            authButtonsDiv.innerHTML = `
                <form id="logout-form" action="/logout" method="POST">
                    <button type="submit" class="logout">Logout</button>
                </form>
            `;
        } else {
            authButtonsDiv.innerHTML = `
                <a href="/login">
                    <button class="login">Login</button>
                </a>
            `;
        }
    }

    checkAuthStatus().then(isAuthenticated => {
        renderButtons(isAuthenticated);
    });

    document.addEventListener('submit', function(event) {
        if (event.target.id === 'logout-form') {
            event.preventDefault();
            fetch('/logout', { method: 'POST' })
                .then(response => {
                    if (response.redirected) {
                        window.location.href = response.url;
                    } else {
                        return response.json();
                    }
                })
                .then(data => {
                    if (data && data.message === 'Logout successful') {
                        renderButtons(false);
                    }
                });
        }
    });
});
