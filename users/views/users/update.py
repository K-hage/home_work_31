from rest_framework.generics import UpdateAPIView

from users.models import User
from users.serializers import UserUpdateSerializer


class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

