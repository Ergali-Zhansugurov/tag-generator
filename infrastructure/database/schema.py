schema = {
    "classes": [
        {
            "class": "Book",
            "properties": [
                {"name": "title", "dataType": ["string"]},
                {"name": "author", "dataType": ["string"]},
                {"name": "description", "dataType": ["string"]},
                {"name": "embedding", "dataType": ["number[]"]},
            ],
        }
    ]
}

client.schema.create(schema)