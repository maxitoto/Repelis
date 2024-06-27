document.addEventListener('DOMContentLoaded', function () {
    const searchInput = document.getElementById('search-input');
    const placeholderTextElement = document.getElementById('placeholder-text');
    let placeholderText = '';
    let categorySelected = false; // Variable para rastrear si se ha seleccionado una categoría
           
    // Evento input para detectar cuando se escribe en el input de búsqueda
    searchInput.addEventListener('input', function () {
        if (!searchInput.value.trim() && !categorySelected && event.inputType === 'deleteContentBackward') {
            // Si el input está vacío o solo contiene espacios en blanco, no se ha seleccionado una categoría,
            // y se presionó la tecla de borrar, restaurar el placeholder por defecto
            searchInput.placeholder = "Buscar";
            placeholderTextElement.classList.add('placeholder-text'); // Aplicar estilo del placeholder
        }
    });
           
    // Agregar evento click a cada opción del menú desplegable
    document.querySelectorAll('#search-options .dropdown-item').forEach(item => {
        item.addEventListener('click', function () {
            categorySelected = true; // Marcar que se ha seleccionado una categoría
            placeholderText = this.getAttribute('data-placeholder');
            searchInput.placeholder = placeholderText ? placeholderText : "Buscar";
            placeholderTextElement.classList.add('placeholder-text'); // Aplicar estilo del placeholder
        });
    });
           
    // Evento keydown para detectar la tecla de borrar
    searchInput.addEventListener('keydown', function (event) {
        if (event.key === 'Backspace' && !searchInput.value && searchInput.placeholder !== "Buscar") {
            // Si se presiona la tecla de borrar, la barra de búsqueda está vacía y el placeholder no es "Buscar",
            // restaurar el placeholder por defecto
            searchInput.placeholder = "Buscar";
            placeholderTextElement.classList.add('placeholder-text'); // Aplicar estilo del placeholder
        }
    });
});
