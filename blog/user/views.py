from django.utils.decorators import method_decorator
from django.views import View
from .models import UserProfile
import json
import hashlib
from ..utils import restful
from ..utils.login_deco import login_check

# Create your views here.

"""
# CBV
更靈活，可繼承
對未定義的http method請求，可以直接返回405
"""


class UserViews(View):
    def post(self, request, username=None):
        ## 用戶後台
        if username:
            try:
                user = UserProfile.objects.get(username=username)
            except Exception as e:
                print(e)
                return restful.params_error("用戶不存在")
            result = {'username': username, 'info': user.info, 'sign': user.sign, 'nickname': user.nickname,
                      'avatar': str(user.avatar)}
            return restful.ok(data=result)

        ## 註冊
        # 從request body裡取數據
        json_str = request.body
        json_obj = json.loads(json_str)
        username = json_obj['username']
        email = json_obj['email']
        password1 = json_obj['password_1']
        password2 = json_obj['password_2']
        phone = json_obj['phone']

        if password1 != password2:
            return restful.params_error("密碼錯誤")
        old_users = UserProfile.objects.filter(username=username)
        if old_users:
            return restful.params_error("用戶名已存在")

        # 密碼md5加密
        pm = hashlib.md5()
        pm.update(password1.encode())
        UserProfile.objects.create(username=username, nickname=username, password=pm.hexdigest(), email=email,
                                   phone=phone)
        result = {'username': username}
        return restful.ok(data=result)

    @method_decorator(login_check)
    def put(self, request, username=None):
        # 更新用戶資訊
        json_str = request.body
        json_obj = json.loads(json_str)
        user = request.my_user

        user.sign = json_obj['sign']
        user.info = json_obj['info']
        user.nickname = json_obj['nickname']
        user.save()
        return restful.ok()


# 更新頭像
@login_check
def user_avatar(request):
    if request.method != 'POST':
        return restful.permission_error("請先登入")

    user = request.my_user
    new_avatar = request.FILES['avatar']
    user.avatar = new_avatar
    user.save()
    return restful.ok()
