from django.conf.urls import url

from rest_framework.routers import DefaultRouter

from .views import MyWebView
from .viewsets import FooViewSet

router = DefaultRouter()
router.register('api/foo', FooViewSet)

urlpatterns = [
    url(r'^web/foo/mywebview/$', MyWebView.as_view(), name='mywebview'),
]
urlpatterns += router.urls
