from django.http import HttpResponse
from django.views.generic import View


class MyWebView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Coucou! Tu veux voir... mon code ?')
