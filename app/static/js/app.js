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


//Controlling dropdown for avatar in the dashboard
document.addEventListener('DOMContentLoaded', function() {
    const avatar = document.getElementById('avatar-img');
    const dropdownMenu = document.getElementById('dropdownMenu');

    avatar.addEventListener('click', function() {
        if (dropdownMenu.style.display === 'none' || dropdownMenu.style.display === '') {
            dropdownMenu.style.display = 'block';
        } else {
            dropdownMenu.style.display = 'none';
        }
    });

    // Close the dropdown menu if the user clicks outside of it
    window.addEventListener('click', function(event) {
        if (!avatar.contains(event.target) && !dropdownMenu.contains(event.target)) {
            dropdownMenu.style.display = 'none';
        }
    });
});


// EditingFunction
document.addEventListener('DOMContentLoaded', function() {
    // Event listener for edit button
    document.querySelectorAll('.editBtn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            const postContent = document.getElementById('postContent-' + postId);
            const editSection = document.getElementById('editSection-' + postId);
            const editTextarea = document.getElementById('editTextarea-' + postId);

            editTextarea.value = postContent.textContent;
            editSection.style.display = 'block';
            postContent.style.display = 'none';
            this.style.display = 'none';
        });
    });

    // Event listener for save button
    document.querySelectorAll('.saveBtn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            const editTextarea = document.getElementById('editTextarea-' + postId);
            const postContent = document.getElementById('postContent-' + postId);
            const editSection = document.getElementById('editSection-' + postId);

            // Send AJAX request to update post
            fetch('/update_post', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                body: new URLSearchParams({
                    'post_id': postId,
                    'content': editTextarea.value
                })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    postContent.textContent = editTextarea.value;
                    editSection.style.display = 'none';
                    postContent.style.display = 'block';
                    // Reload the page after saving
                    location.reload();
                } else {
                    alert(data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    // Event listener for cancel button
    document.querySelectorAll('.cancelBtn').forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            const postContent = document.getElementById('postContent-' + postId);
            const editSection = document.getElementById('editSection-' + postId);
            const editBtn = document.querySelector('.editBtn[data-post-id="' + postId + '"]');

            editSection.style.display = 'none';
            postContent.style.display = 'block';
            editBtn.style.display = 'inline';
            // Reload the page after canceling
            location.reload();
        });
    });
});

