from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):

    serializer_class= serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIVIew features"""
    

        an_apiView=[
            "Uses HTTP methods as functions (POST, GET, PUT, PATCH, DELETE)",
            "Is similar to a traditional",
            "Is mapped manually",
            "Gives you the most handy to work on complex things"
        ]

        return Response({"message": "Hello", "an_apiView": an_apiView})

    def post(self, request):
        """Create a hello message with our name"""

        print(request.data)
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handling updating of object"""

        return(Response({"method":"PUT"}))

    def patch(self, request, pk=None):
        """Handling updating object partially"""
        return(Response({"method":"PATCH"}))
    
    def delete(self, request, pk=None):
        """"Deleting the object"""
        return(Response({"method":"DELETE"}))


class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_ViewSet=[
            "Uses HTTP methods as functions (POST, GET, PUT, PATCH, DELETE)",
            "Is similar to a traditional",
            "Is mapped manually",
            "Gives you the most handy to work on complex things"
        ]

        return Response({"message": "Hello", "a_ViewSet": a_ViewSet})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"hello {name}"

            return Response({"message":message})
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Retrieve the data of single object"""
        return(Response({"method":"GET"}))

    def update(self, request, pk=None):
        """Handling updating of object"""

        return(Response({"method":"PUT"}))

    def partial_update(self, request, pk=None):
        """Handling updating object partially"""
        return(Response({"method":"PATCH"}))
    
    def destroy(self, request, pk=None):
        """"Deleting the object"""
        return(Response({"method":"DELETE"}))


class UserProfileViews(viewsets.ModelViewSet):

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', 'email')


class LoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewset(viewsets.ModelViewSet):
    """Handles all the HTTP Methods for UserFeed"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.ProfileFeedSerializer
    queryset = models.UserProfileFeed.objects.all()
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated,
    )

    def perform_create(self, serializer):
        """set the user profile to the logged user"""
        serializer.save(user_profile=self.request.user)

