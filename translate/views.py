from django.http import HttpResponse
from django.utils.translation import gettext as _


def my_view(request):
    greetings = _('Hello, World!')
    return HttpResponse(greetings)
