document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchTypeInput = document.getElementById('search-type');
    const resultsContainer = document.getElementById('search-results');
    const noResultsMessage = document.getElementById('no-results');
    let timeoutId;

    searchInput.addEventListener('input', function() {
        const termino = this.value.trim(); // Obtener el valor actual del campo de búsqueda
        const placeholder = document.querySelector('#search-options .dropdown-item.active')?.getAttribute('data-placeholder') || 'Buscar';
    

        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            if (termino) {
                buscarDinamico(termino, placeholder); // Llamar a tu función de búsqueda dinámica con ambos parámetros
            } else {
                resultsContainer.style.display = 'none';
                resultsContainer.innerHTML = '';
                noResultsMessage.style.display = 'none';
            }
        }, 300); // Esperar 300 ms antes de hacer la búsqueda
    });

    // Agregar evento click a cada elemento del menú desplegable
    document.querySelectorAll('#search-options .dropdown-item').forEach(item => {
        item.addEventListener('click', function(event) {
            event.preventDefault(); // Prevenir el comportamiento por defecto del enlace
            // Remover la clase 'active' de todos los elementos
            document.querySelectorAll('#search-options .dropdown-item').forEach(el => {
                el.classList.remove('active');
            });

            // Agregar la clase 'active' al elemento seleccionado
            this.classList.add('active');

            // Actualizar el placeholder del campo de búsqueda
            const placeholder = this.getAttribute('data-placeholder');
            searchInput.placeholder = placeholder;
            searchTypeInput.value = placeholder; // Actualizar el valor del input hidden
        });
    });

});