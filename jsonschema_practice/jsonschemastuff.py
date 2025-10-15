import requests
from configuration import SERVICE_URL
from jsonschema_practice.src.baseclasses.response import Response
from jsonschema_practice.src.schemas.post import POST_SCHEMA


def test_getting_posts():
    r = requests.get(SERVICE_URL)
    recieved_posts = Response(r)
    recieved_posts.assert_status_code(200).validate_schema(POST_SCHEMA)