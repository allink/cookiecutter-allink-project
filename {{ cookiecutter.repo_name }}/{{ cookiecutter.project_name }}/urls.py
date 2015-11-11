from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from feincms.module.page.sitemap import PageSitemap

from allink_essentials.view.langauge_redirect_view import FuzzyLanguageRedirectView

import os


sitemaps = {
    'pages': PageSitemap,
}

urlpatterns = patterns('',
    url(r'^admin/tinymce_links\.js$', '{{ cookiecutter.project_name }}.views.get_tiny_mce_links'),
    # Used for tinymce in Application
    # url(r'^admin/tinymce_settings\.js$', TemplateView.as_view(template_name='tinymce/app_settings.js')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^robots\.txt$', include('robots.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^404/$', 'django.views.defaults.page_not_found'),
    url(r'^500/$', 'django.views.defaults.server_error'),
    url(r'^mailchimp/$', include('allink_essentials.mailchimp_api.urls')),
    url(r'^$', FuzzyLanguageRedirectView.as_view()),
    url(r'', include('feincms.contrib.preview.urls')),
    url(r'', include('feincms.urls')),
)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = patterns('',
        url(r'^__debug__/', debug_toolbar.urls),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/'), 'show_indexes': True}),
    ) + urlpatterns
