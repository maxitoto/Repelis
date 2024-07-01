document.addEventListener('DOMContentLoaded', (event) => {
    const rangeInput = document.getElementById('id_puntaje');
    const rangeValue = document.getElementById('puntaje_value');
    
    rangeInput.addEventListener('input', (e) => {
        rangeValue.textContent = e.target.value;
    });
});

        