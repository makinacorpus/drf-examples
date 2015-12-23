from django.conf.urls import include, url

urlpatterns = [
    url(r'^', include('foo.urls', namespace='foo')),
    url(r'^', include('bar.urls', namespace='bar')),
    url(r'^', include('baz.urls', namespace='baz')),
]
