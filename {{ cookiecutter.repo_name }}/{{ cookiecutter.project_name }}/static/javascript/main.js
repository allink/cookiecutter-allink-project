$(function() {
    $(document.body).on('submit', '#mailchimp-form', function(event){
        event.preventDefault();
        $.post('/mailchimp/', $(this).serialize(), function(data) {
            if (data == 'ok'){
                $(".mailchimp-result").html( 'Vielen Dank für Ihre Anmeldung.' );
            }
            else {
                $(".mailchimp-result").html(data);
            }
        });
        return false;
    });
});
