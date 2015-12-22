from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from bar.viewsets import BarViewSet
from baz.viewsets import BazViewSet
from foo.viewsets import FooViewSet


router_bar = DefaultRouter()
router_bar.register('bar', BarViewSet)

router_baz = DefaultRouter()
router_baz.register('baz', BazViewSet)

router_foo = DefaultRouter()
router_foo.register('foo', FooViewSet)

urlpatterns = [
    # Some Web views
    url(r'^web/foo/', include('foo.urls', namespace='foo')),
    url(r'^web/bar/', include('bar.urls', namespace='bar')),
    url(r'^web/baz/', include('baz.urls', namespace='baz')),
    # Dirty stuff begins
    url(r'^api/', include(router_bar.urls, namespace='bar')),
    url(r'^api/', include(router_baz.urls, namespace='baz')),
    url(r'^api/', include(router_foo.urls, namespace='foo')),
]
