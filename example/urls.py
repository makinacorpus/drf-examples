from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from bar.viewsets import BarViewSet
from baz.viewsets import BazViewSet
from foo.viewsets import FooViewSet


router = DefaultRouter()
router.register('bar', BarViewSet)
router.register('baz', BazViewSet)
router.register('foo', FooViewSet)

urlpatterns = [
    # Some Web views
    url(r'^foo/', include('foo.urls', namespace='foo')),
    url(r'^bar/', include('bar.urls', namespace='bar')),
    url(r'^baz/', include('baz.urls', namespace='baz')),
    url(r'^api/v1/', include(router.urls, namespace='v1')),
    url(r'^api/v2/', include(router.urls, namespace='v2')),
    url(r'^api/v3/', include(router.urls, namespace='v3')),
]
