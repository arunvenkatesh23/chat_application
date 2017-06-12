$('#chat-form').on('submit', function(event){
    event.preventDefault();

    $.ajax({
        url : '/post/',
        type : 'POST',
        data : { message : $('#id_message').val() },

        success : function(response){
            if (response.result === 'OK') {
                if (response.data && typeof(response.data) === 'object') {
                    alert(response.data);
                }
            }
        }
    });
});