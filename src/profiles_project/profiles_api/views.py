from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from . import models
from rest_framework import status
from . import permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class HelloApiView(APIView):
    """test api view"""


    serializer_class=serializers.HelloSerializers

    def get(self, request, format=None):
        """return a list of APIView feature"""

        an_apiview=[
            'uses HTTP methode as function(get, post, put, patch, delete)',
            'it is similar to a traditional django view ',
            'gives you the most control over your_logic',
            'is manully mapped to URLS'
            ]
        return Response({'message':'hello','an_apiview':an_apiview})


    def post(self, request):
         """create a hello message with our name"""
         serializer= serializers.HelloSerializers(data=request.data)

         if serializer.is_valid():
             name=serializer.data.get('name')
             message='Hello {0}'.format(name)
             return Response({'message':message})
         else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """handels updating an object"""
        return Response({'methode':'put'})

    def patch(self, request, pk=None):
        """patch request, only updates provided in the request"""
        return Response({'methode':'patch'})

    def delete(self, request, pk=None):
        """delete request"""
        return Response({'methode':'delete'})



class HelloViewSet(viewsets.ViewSet):
    """test api viewsets"""

    serializer_class=serializers.HelloSerializers

    def list(self, request):
        """return a hello message."""
        a_viewset=[
        'user actions(list, create, retrieve, update, partial_update)',
        'automatically maps to urls using routers',
        'provides  more functionality with less code '
        ]
        return Response({'message':'Hello', 'a_viewset':a_viewset})
    def create(self, request):
        """create a new hello message"""

        serializer=serializers.HelloSerializers(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer,errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        "get a spesific object by it's id"
        return Response({'http_method':'get'})

    def update(self, request, pk=None):
        return Response({'http_method':'put'})

    def partial_update(self, request, pk=None):
        return Response({'http_method':'patch'})

    def destroy(self, request, pk=None):
        return Response({'http_method':'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """handling creating and updating"""

    serializer_class=serializers.UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(permissions.UpdateOwnProfile,)
    
