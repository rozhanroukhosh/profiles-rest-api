from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

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
