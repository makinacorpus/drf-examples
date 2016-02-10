from django.db import IntegrityError, transaction

from rest_framework.decorators import detail_route
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Bar
from .serializers import BarSerializer


class BarViewSet(ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    permission_classes = (IsAuthenticated,)

    @detail_route(methods=['patch'], permission_classes=(AllowAny,))
    def name(self, request, *args, **kwargs):
        """
        Stupid endpoint which blindly try to update a unique field. This is
        just for purpose : raising an IntegrityError. DB transaction is still
        active and need a rollback/commit command if we want to be able to
        continue to write some stuff.
        """
        instance = self.get_object()
        instance.name = request.data.get('name')  # no check, hack me if you want

        try:
            instance.save()  # Write query fail
        except IntegrityError:
            transaction.rollback()  # End transaction to continu
            instance.name = None
            instance.save()  # Because we rollback, we can now write new changes
            return Response("I will survive!")

        return Response(instance.name)
