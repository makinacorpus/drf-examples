from rest_framework.viewsets import ModelViewSet

from .models import Bar
from .serializers import BarSerializer


class BarViewSet(ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
