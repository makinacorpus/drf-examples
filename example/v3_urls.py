from django.conf.urls import include, url

from rest_framework.routers import SimpleRouter

from bar.viewsets import BarViewSet
from baz.viewsets import BazViewSet
from foo.viewsets import FooViewSet


router = SimpleRouter()
router.register('bar', BarViewSet)  # Include every endpoints for v3
router.register('baz', BazViewSet)
router.register('foo', FooViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
