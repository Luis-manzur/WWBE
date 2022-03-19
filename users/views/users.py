"""users views."""
#DjangoREST Framework
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response


#Permissions
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsAccountOwner


#Serializers
from users.serializers import UserSignUpSerializer, UserLoginSerializer, UserModelSerializer, AccountVerificationSerializer
from users.serializers import ProfileModelSerializer

#Models
from users.models import User, Profile

class UserViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """user view set.

    Handle sign up, login and account verification
    """

    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    def get_permissions(self):
        """Addign permissiond based on actions"""

        if self.action in ['signup', 'login', 'verify']:
            permissions = [AllowAny,]
        elif self.action in ['retrieve', 'update', 'partial_update']:
            permissions = [IsAuthenticated, IsAccountOwner]
        else:
            permissions = [IsAuthenticated,]

        return [permission() for permission in permissions]

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User Sign up."""
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User Login."""
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def verify(self, request):
        """Account Verification"""
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': 'Congratulations, now go share some rides!'
        }
        return Response(data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put', 'patch'])
    def profile(self, request, *args, **kwargs):
        """Update profile data."""
        user: User = self.get_object()
        profile: Profile = user.profile
        partial = request.method == 'PATCH'
        serializer = ProfileModelSerializer(
            profile,
            data = request.data,
            partial=partial
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = UserModelSerializer(user).data
        return Response(data)