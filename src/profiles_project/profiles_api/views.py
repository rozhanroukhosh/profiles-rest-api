from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class HelloApiView(APIView):
    """test api view"""

    def get(self, request, format=None):
        """return a list of APIView feature"""

        an_apiview=[
            'uses HTTP methode as function(get, post, put, patch, delete)',
            'it is similar to a traditional django view ',
            'gives you the most control over your_logic',
            'is manully mapped to URLS'
            ]
        return Response({'message':'hello','an_apiview':an_apiview})
