$(document).ready(function() {
    // Delegación de eventos para botones de cambiar estado
    $(document).on('click', '.btn-cambiar-estado', function(e) {
        e.preventDefault();
        var id_critica = $(this).data('id-critica');
        var estado = $(this).data('estado');

        $.ajax({
            type: 'POST',
            url: '{% url 'actualizar_estado_critica' %}',
            data: {
                'id_critica': id_critica,
                'estado': estado,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function(data) {
                console.log('Estado actualizado correctamente');
                // Actualizar la lista de críticas
                actualizarListaCriticas();
            },
            error: function(xhr, status, error) {
                console.error('Error al actualizar el estado de la crítica:', error);
            }
        });
    });

    // Función para actualizar la lista de críticas
    function actualizarListaCriticas() {
        $.ajax({
            type: 'GET',  // Puedes usar GET u otra forma de solicitud según tu implementación
            url: window.location.href,  // Puedes ajustar la URL según la estructura de tu aplicación
            success: function(data) {
                var nuevasCriticasHtml = $(data).find('#lista-criticas').html();  // Suponiendo que el div de la lista de críticas tiene el ID 'lista-criticas'
                $('#lista-criticas').html(nuevasCriticasHtml);  // Actualiza la lista de críticas en el DOM
            },
            error: function(xhr, status, error) {
                console.error('Error al actualizar la lista de críticas:', error);
            }
        });
    }
});
