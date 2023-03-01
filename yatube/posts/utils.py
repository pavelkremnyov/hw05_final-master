from django.conf import settings
from django.core.paginator import Paginator


def page_obj_func(place_page, request):
    paginator = Paginator(place_page, settings.POST_LIST)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
