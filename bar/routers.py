from rest_framework.routers import DefaultRouter, DynamicListRoute, Route


class MyCustomRouter(DefaultRouter):

    routes = list(DefaultRouter.routes)
    routes[0] = Route(
        url=r'^{prefix}/a-custom-path/(?P<custom_pk>\d+){trailing_slash}$',
        mapping={
            'get': 'list',
            'post': 'create',
            'patch': 'partial_update_multiple',
            'delete': 'delete_multiple',
        },
        name='{basename}-list',
        initkwargs={'suffix': 'List'}
    )
    routes[1] = DynamicListRoute(
        url=r'^{prefix}/a-custom-path/(?P<custom_pk>\d+)/{methodname}{trailing_slash}$',
        name='{basename}-{methodnamehyphen}',
        initkwargs={}
    )
