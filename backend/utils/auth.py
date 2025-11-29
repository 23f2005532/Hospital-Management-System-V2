from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify
from functools import wraps

def role_required(*allowed_roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()

            if "role" not in claims or claims["role"] not in allowed_roles:
                return {"message": "Unauthorized"}, 403

            return fn(*args, **kwargs)
        return wrapper
    return decorator
