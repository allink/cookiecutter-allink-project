{% raw %}
tinyMCE.init({
    selector: 'textarea.tinymce_widget',
    {% include "tinymce/tinymce_settings.js" %}
});
{% endraw %}
