from django.urls import path
from .views import LoginApi

urlpatterns = [
    path('', LoginApi.as_view({'get': 'post', 'post': 'post'}), name='login')
]
