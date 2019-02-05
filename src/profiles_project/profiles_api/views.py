from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            'Uses HTTP methods as function(get, post, put, patch, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello', 'an_apiview': an_apiview})
