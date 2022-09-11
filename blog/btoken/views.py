from ..user.models import UserProfile
from django.conf import settings
import jwt
import json
import time
import hashlib
from ..utils import restful


# Create your views here.


## 登入
def login(request):
    if request.method != 'POST':
        return restful.permission_error("請先登入")

    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj['username']
    password = json_obj['password']

    try:
        user = UserProfile.objects.get(username=username)
    except Exception as e:
        print(e)
        return restful.params_error("用戶名或密碼錯誤")

    pm = hashlib.md5()
    pm.update(password.encode())
    if pm.hexdigest() != user.password:
        return restful.params_error("用戶名或密碼錯誤")
    token = make_token(username)
    result = {'username': username, 'token': token.decode()}
    return restful.ok(data=result)


# 產生token
def make_token(username, expire=3600 * 24):
    key = settings.JWT_TOKEN_KEY
    now_t = time.time()
    payload_data = {'username': username, 'exp': now_t + expire}
    return jwt.encode(payload_data, key, algorithm='HS256')
