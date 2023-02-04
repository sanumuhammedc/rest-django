from django.shortcuts import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import Login
from rest_framework.decorators import action


class LoginApi(viewsets.ModelViewSet):
    serializer_class = Login

    @action(detail=False, methods=['GET', 'POST'])
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = Login(data=request.data)
            if serializer.is_valid():
                if serializer.validated_data['name'] == 'aswin' and serializer.validated_data['password'] == '1234':
                    return Response({'status': 'success'})
            else:
                return HttpResponse('Not User')
        return Response({'data': 'login'})
