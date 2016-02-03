from distutils.version import LooseVersion

from rest_framework.decorators import list_route
from rest_framework.mixins import ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .models import Bar
from .serializers import BarSerializer


class BarViewSet(ListModelMixin, GenericViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

    def list(self, request, *args, **kwargs):
        return Response('You are using version {v}'.format(v=request.version))

    @list_route()
    def open(self, request, *args, **kwargs):
        """
        Added only since v2 for happy hours
        """
        if LooseVersion(request.version) >= LooseVersion('v2'):
            return Response('Mike will made iiiit')
        else:
            return Response('Whaaaat??')

    @list_route()
    def close(self, request, *args, **kwargs):
        """
        Only added at v3 because it was a real mess!
        """
        if request.version == 'v3':
            return Response('We got London On Da Traaaaack')
        else:
            return Response('Whaaaat??')
