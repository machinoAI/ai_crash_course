import json

def valid_json(data):
    result = []

    if not data:
        return result

    for item in data:
        try:
            item = json.loads(item)
        except json.JSONDecodeError:
            continue

        if isinstance(item, dict):
            if item.get("confidence", 0) >= 0.75:
                result.append(item)

    return result


data = [
    '{"name": "John", "confidence": 0.85}',
    "Hello World",
    '{"name": "Alice", "confidence": 0.65}',
    "This is just a normal string",
    '{"name": "Bob", "confidence": 0.92}',
    "Invalid JSON"
]
result = valid_json(data)

print("Result:", result)