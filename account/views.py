# Create your views here.
from django.utils.decorators import method_decorator
from rest_framework.views import APIView

from account.decorators import login_exempt
from account.services import Login, Register
from common.utils import APIResponse


@method_decorator(login_exempt, name="dispatch")
class LoginView(APIView):
    def post(self, request):
        data = request.body
        username = data.get("username")
        password = data.get("password")
        try:
            token = Login.login(user_uid=username, password=password)
            return APIResponse(token=token)
        except Exception as e:
            return APIResponse(result=False, message=f"{e}")


@method_decorator(login_exempt, name="dispatch")
class RegisterView(APIView):

    def post(self, request):
        user_info = request.data
        try:
            Register.register(user_info=user_info)
            return APIResponse()
        except Exception as e:
            return APIResponse(code=-1, message=f"{e}")
