import uuid

def generate_uuid() -> str:
    return str(uuid.uuid5(
        uuid.NAMESPACE_X500, str(uuid.uuid4())
    ))