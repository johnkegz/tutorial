from django.shortcuts import render
#views.py
from rest_framework.views import APIView
from rest_framework.response import Response
class HelloWorld(APIView):
    def get(self, request):
        return Response('HELLO WORLD! John kalyango.')
