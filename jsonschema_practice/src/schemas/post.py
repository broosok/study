POST_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "title": {"type": "string", "enum": ["Post 1", "Post 2", "Post 3"]},
    },
    "required": ["id", "title"]
}