from rest_framework.parsers import JSONParser


class ExampleJSONParser(JSONParser):
    media_type = 'application/vnd.example.books+json'
