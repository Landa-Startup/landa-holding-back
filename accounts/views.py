from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import Token

class CustomPayload(Token):
    def __init__(self, token):
        super().__init__(token)
        
    @property
    def role(self):
        # Replace this with logic to get the user's role
        return self['roles']
    @property
    def first_name(self):
        # Replace this with logic to get the user's role
        return self['first_name']
    @property
    def last_name(self):
        # Replace this with logic to get the user's role
        return self['last_name']
    @property
    def image(self):
        # Replace this with logic to get the user's role
        return self['image']
    
class GenerateTokenView(APIView):
    def post(self, request):
        user = request.user  # Replace this with your user object
        if user:
            refresh = RefreshToken.for_user(user)
            custom_payload = CustomPayload(refresh.access_token)
            custom_payload['roles'] = 'user'  # Replace with the actual role for the user
            return Response({'access_token': str(refresh.access_token)}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
