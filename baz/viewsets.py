from rest_framework.viewsets import ModelViewSet

from .models import Baz


class BazViewSet(ModelViewSet):
    queryset = Baz.objects.all()
