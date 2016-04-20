{% raw %}
width: '615px',
height: '400px',
link_list: '/admin/tinymce_links.js',
valid_children : '+body[style]',
plugins: 'fullscreen paste link code visualblocks image',
paste_auto_cleanup_on_paste: true,
paste_as_text: true,
relative_urls: false,
invalid_elements: 'script',
statusbar: false,
toolbar: 'insertfile undo redo | styleselect | bold | bullist numlist | link | code visualblocks',
menubar : false,
visualblocks_default_state: true,
style_formats: [
    {title: 'H2', block: 'h2'},
    {title: 'H3', block: 'h3'},
    {title: 'Paragraph', block: 'p'}
],
file_browser_callback: function(field_name, url, type, win) {
    var cssFileExists = false;

    $.each(document.styleSheets,function(i,v){
        if(v.href.indexOf('style.css') != -1) cssFileExists = true;
    });

    if(!cssFileExists) $('head').append('<link rel="stylesheet" type="text/css" href="/static/allink_files/stylesheets/style.css">');

    $('body').append('<div class="lightbox">' +
        '<div class="wrapper">' +
            '<div class="inner">' +
                '<div class="content"><iframe src="/admin/allink_files/file/editor-add/" width="500px">' +
                '</iframe></div>' +
            '</div>' +
        '</div>' +
    '</div>');

    window.imageUploadSuccess = function(image_path){
        $('#' + field_name).val(image_path);
        $('.lightbox').remove();
    };

    $('.lightbox iframe').load(function(){
        var iframe = $('.lightbox iframe').contents();
        iframe.find(".file-btn-close").on('click',function(e){
            $('.lightbox').remove();
        });
    });

    $(document).keydown(function(e){
        if(e.keyCode == 27) $('.lightbox').remove();
    });
}
{% endraw %}
