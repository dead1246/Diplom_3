import uuid


BUN_NAME = "Флюоресцентная булка R2-D3"
FILLING_NAME = "Мясо бессмертных моллюсков Protostomia"


def unique_user():
    suffix = uuid.uuid4().hex[:10]
    return {
        "email": f"valentin_ui_{suffix}@example.com",
        "password": f"Password{suffix}",
        "name": f"Valentin {suffix}",
    }
