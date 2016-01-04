from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Bar
from .serializers import BarSerializer


class BarViewSet(ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

    def partial_update_multiple(self, request, custom_pk, *args, **kwargs):
        return Response(
            'Do some bulk update op for the given custom pk : {pk}'.format(pk=custom_pk)
        )

    def delete_multiple(self, request, custom_pk, *args, **kwargs):
        return Response(
            'Do some bulk delete op for the given custom pk : {pk}'.format(pk=custom_pk)
        )

    @list_route(methods=['get'], url_path='so-dope-path')
    def a_custom_callback(self, request, custom_pk, *args, **kwargs):
        return Response(
            'Like American people say : AWESOME! We now have a custom '
            'dynamic list route with a custom path and take a custom pk '
            'which is : {pk}'.format(pk=custom_pk)
        )

