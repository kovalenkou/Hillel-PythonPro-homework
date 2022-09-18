from django.urls import path

from .views import randoms

app_name = 'apps.randoms'

urlpatterns = [
    path('randoms/', randoms.as_view(), name='randoms'),
]
