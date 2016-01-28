# -*- coding: utf-8 -*-

from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Bar
from .serializers import BarSerializer


class BarViewSet(ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer

    @list_route()
    def open(self, request, *args, **kwargs):

        if request.version == 'v1':
            return Response(
                "Whaaat? Pas de 404 par ``ALLOWED_VERSIONS`` ?? Faut pas "
                "déconner, cette version, elle est trop naze."
            )
        elif request.version == 'v2':
            return Response("Arrrf, c'est la v2. Tu peux prendre la v3 stp ?")
        elif request.version == 'v3':
            return Response("Avec modération !")
        else:
            return Response("Naaaan, j'ai craqué l'URLconf ???")
