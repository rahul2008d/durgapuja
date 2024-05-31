document.querySelector('.burger-menu').addEventListener('click', () => {
    document.querySelector('.nav-links').classList.toggle('nav-active');
    document.querySelectorAll('.burger-line').forEach(line => {
        line.classList.toggle('burger-line-active');
    });
});
