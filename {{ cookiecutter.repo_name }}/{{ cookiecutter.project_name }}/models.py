from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent

Page.register_extensions(
    'allink_essentials.feincms_extensions.metas_v2',
    'allink_essentials.in_footer.page_extension_v2',
    'feincms.module.extensions.translations',
    # 'feincms.module.extensions.datepublisher',
    'feincms.module.extensions.changedate',
    'feincms.module.page.extensions.navigation',
    'feincms.module.page.extensions.symlinks',
)

Page.register_templates({
    'key': 'content',
    'title': 'Inhalt',
    'path': 'content.html',
    'regions': (
        ('main', 'Haupt Inhalt'),
        ('header', 'Header'),
    ),
})

Page.create_content_type(RichTextContent, regions=('main',))
