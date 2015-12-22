from rest_framework.viewsets import ModelViewSet

from .models import Foo


class FooViewSet(ModelViewSet):
    queryset = Foo.objects.all()
