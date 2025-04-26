document.addEventListener('DOMContentLoaded', () => {
    const btnModo = document.getElementById('btn-modo');
    const body = document.body;

    // Verificar si hay un tema guardado en localStorage
    if (localStorage.getItem('dark-mode') === 'enabled') {
        body.classList.add('dark-mode');
        btnModo.innerHTML = '🌙'; // Cambia a luna en modo oscuro
    } else {
        btnModo.innerHTML = '☀️'; // Estrellita en modo claro
    }

    btnModo.addEventListener('click', () => {
        body.classList.toggle('dark-mode');

        // Cambiar el contenido del botón
        if (body.classList.contains('dark-mode')) {
            btnModo.innerHTML = '🌙'; // Cambia a luna en modo oscuro
            localStorage.setItem('dark-mode', 'enabled');
        } else {
            btnModo.innerHTML = '☀️'; // Cambia a estrellita en modo claro
            localStorage.setItem('dark-mode', 'disabled');
        }
    });
});
