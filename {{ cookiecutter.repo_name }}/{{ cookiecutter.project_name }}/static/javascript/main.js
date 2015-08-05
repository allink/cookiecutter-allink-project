$(function() {
    $(document.body).on('submit', '#mailchimp-form', function(event){
        event.preventDefault();
        var $this = $(this);
        $.post($this.attr('action'), $this.serialize(), function(data) {
            if (data == 'ok'){
                $this.parents('.mailchimp-result').html( 'Vielen Dank für Ihre Anmeldung.' );
                dataLayer.push({'event': 'newsletter.sent'});
            }
            else {
                $this.parents('.mailchimp-result').html(data);
            }
        });
        return false;
    });
});
