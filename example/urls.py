from django.conf.urls import include, url

from bar.viewsets import BarViewSet
from baz.viewsets import BazViewSet
from foo.viewsets import FooViewSet

urlpatterns = [
    url(r'^api/bar/$', BarViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='bar-list'),
    url(r'^api/bar/(?P<pk>[^/.]+)/$', BarViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='bar-detail'),
    url(r'^api/baz/$', BazViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='baz-list'),
    url(r'^api/baz/(?P<pk>[^/.]+)/$', BazViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='baz-detail'),
    url(r'^api/foo/$', FooViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='foo-list'),
    url(r'^api/foo/(?P<pk>[^/.]+)/$', FooViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='foo-detail'),
    # Some Web views
    url(r'^foo/', include('foo.urls', namespace='foo')),
    url(r'^bar/', include('bar.urls', namespace='bar')),
    url(r'^baz/', include('baz.urls', namespace='baz')),
]
