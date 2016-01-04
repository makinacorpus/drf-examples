from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from bar.viewsets import BarViewSet
from baz.viewsets import BazViewSet
from foo.viewsets import FooViewSet


router = DefaultRouter()
router.register('api/bar', BarViewSet)
router.register('api/baz', BazViewSet)
router.register('api/foo', FooViewSet)

urlpatterns = [
    # Some Web views
    url(r'^foo/', include('foo.urls', namespace='foo')),
    url(r'^bar/', include('bar.urls', namespace='bar')),
    url(r'^baz/', include('baz.urls', namespace='baz')),
]
# Append our API views
urlpatterns += router.urls
