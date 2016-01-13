from rest_framework.renderers import JSONRenderer


class ExampleJSONRenderer(JSONRenderer):
    media_type = 'application/vnd.example.books+json'
