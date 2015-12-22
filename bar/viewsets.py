from rest_framework.viewsets import ModelViewSet

from .models import Bar


class BarViewSet(ModelViewSet):
    queryset = Bar.objects.all()
