import jwt
import traceback
from django.conf import settings

class TokenSimpleJWTAuth:
    def get_user_id_from_token(token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            return payload['user_id']
        except:
            tb = traceback.format_exc()
            print(tb)
            return 'error decoding token'
