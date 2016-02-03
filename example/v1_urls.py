from django.conf.urls import include, url

from rest_framework.routers import SimpleRouter

from bar.viewsets import BarViewSet
from baz.viewsets import BazViewSet


router = SimpleRouter()
router.register('baz', BazViewSet)
router.register('foo', BazViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(
        r'^bar/$',
        BarViewSet.as_view(actions={'get': 'list'}),
        name='bar-list',
    ),
]
