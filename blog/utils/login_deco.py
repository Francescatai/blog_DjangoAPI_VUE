from django.conf import settings
from ..user.models import UserProfile
import jwt
import restful


def login_check(func):
    def wrap(request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')
        if not token:
            return restful.permission_error("請重新登入")

        try:
            res = jwt.decode(token, settings.JWT_TOKEN_KEY)
        except Exception as e:
            print(e)
            return restful.permission_error("請重新登入")

        username = res['username']
        user = UserProfile.objects.get(username=username)
        request.my_user = user
        return func(request, *args, **kwargs)

    return wrap
