from rest_framework.generics import CreateAPIView

from users.models import User
from users.serializers.users import UserCreateSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer



