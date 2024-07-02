document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const resultsContainer = document.getElementById('search-results');
    const noResultsMessage = document.getElementById('no-results');
    let timeoutId;

    searchInput.addEventListener('input', function() {
        const termino = this.value.trim(); // Obtener el valor actual del campo de búsqueda
        const place_holder = document.querySelector('#search-options .dropdown-item.active')?.getAttribute('data-placeholder') || 'Buscar';

        clearTimeout(timeoutId);
        timeoutId = setTimeout(() => {
            if (termino) {
                buscarDinamico(termino, place_holder); // Llamar a tu función de búsqueda dinámica con ambos parámetros
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
            searchInput.placeholder = this.getAttribute('data-placeholder');
        });
    });

    document.querySelector('form').addEventListener('submit', function(event) {
        event.preventDefault(); // Esto evitará que el formulario se envíe y cambie la URL
    });

    function buscarDinamico(termino, place_holder) {
        const searchUrl = `/buscar?placeholder=${encodeURIComponent(place_holder)}&termino=${encodeURIComponent(termino)}`;  // Ajusta la URL según sea necesario

        // Realizar solicitud AJAX a la función de vista 'buscar'
        fetch(searchUrl)
            .then(response => response.json())
            .then(data => {
                // Limpiar resultados anteriores
                resultsContainer.innerHTML = '';

                if (data.length > 0) {
                    // Mostrar ventana emergente con resultados
                    data.forEach(item => {
                        const resultElement = document.createElement('div');
                        resultElement.textContent = item.nombre;  // Ajusta según los datos que recibas
                        resultsContainer.appendChild(resultElement);
                    });

                    resultsContainer.style.display = 'block';  // Mostrar contenedor
                    noResultsMessage.style.display = 'none';  // Ocultar mensaje de "cero resultados"
                } else {
                    resultsContainer.style.display = 'none';
                    noResultsMessage.style.display = 'block';  // Mostrar mensaje de "cero resultados"
                }
            })
            .catch(error => {
                console.error('Error fetching search results:', error);
                resultsContainer.style.display = 'none';
                noResultsMessage.style.display = 'none';
            });
    }
});
