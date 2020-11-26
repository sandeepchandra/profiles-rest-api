from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


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

            return Response(serializer.errors, status=status.HTTTP_400_BAD_REQUEST)

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


