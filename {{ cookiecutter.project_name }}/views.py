import json
from django.http import HttpResponse
from feincms.module.page.models import Page
from feincms.module.medialibrary.models import MediaFile


def get_tiny_mce_links(request):
    link_list = query_to_tuple(Page.objects.filter(parent__isnull=True))

    media_file_list = tuple((image.translation.caption if image.translation else str(image), image.get_absolute_url()) for image in MediaFile.objects.all())
    link_list += tuple((' ', '  ')) + media_file_list

    output = "var %s = %s" % ("tinyMCELinkList", json.dumps(link_list))
    return HttpResponse(output, content_type='application/json')


def query_to_tuple(query, level=0):
    link_list = tuple()
    prefix = (''.join(u'-' for i in range(level)) + ' ')
    for p in query:
        link_list += ((prefix + p.title, p.get_absolute_url()),)
        link_list += query_to_tuple(p.get_children(), level=level + 1)
    return link_list
