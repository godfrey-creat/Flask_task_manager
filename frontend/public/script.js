document.addEventListener('DOMContentLoaded', () => {
    const loginBtn = document.getElementById('loginBtn');
    const getStartedBtn = document.getElementById('getStartedBtn');

    loginBtn.addEventListener('click', () => {
        window.location.href = '/login';
    });

    getStartedBtn.addEventListener('click', () => {
        window.location.href = '/dashboard';
    });
});

