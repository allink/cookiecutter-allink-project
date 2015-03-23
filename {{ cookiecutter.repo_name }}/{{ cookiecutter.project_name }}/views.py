import json
from django.http import HttpResponse
from feincms.module.page.models import Page


def query_to_tuple(query, level=0):
    link_list = list()
    for p in query:
        if p.get_children():
            link_list.append({'title': p.title, 'menu': query_to_tuple(p.get_children(), level=level + 1)})
        else:
            link_list.append({'title': p.title, 'value': p.get_absolute_url()})
    return link_list


def get_tiny_mce_links(request):
    link_list = query_to_tuple(Page.objects.filter(parent__isnull=True))

    output = json.dumps(link_list)
    return HttpResponse(output, content_type='application/json')
