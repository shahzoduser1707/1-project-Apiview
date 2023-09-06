from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class ProductView(APIView):
    def get(self,request):
        return Response({'apple' : '2-days ago'})

class BranchView(APIView):
    def post(self,request):
        print(request.data)
        return Response({ 'id' : 'date'})
    