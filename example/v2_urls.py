from django.conf.urls import include, url

from rest_framework.routers import SimpleRouter

from bar.viewsets import BarViewSet
from baz.viewsets import BazViewSet
from foo.viewsets import FooViewSet


router = SimpleRouter()
router.register('baz', BazViewSet)
router.register('foo', FooViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^bar/$',
        BarViewSet.as_view(actions={'get': 'list'}),
        name='bar-list',
    ),
    # New endpoint added with v2
    url(
        r'^bar/open/$',
        BarViewSet.as_view(actions={'get': 'open'}),
        name='bar-open',
    ),
]
