from django.urls import path

from .views import about, index_page, whoami

urlpatterns = [
    path('', index_page.as_view(), name='index_page'),
    path('about/', about.as_view(), name='about'),
    path('about/whoami/', whoami.as_view(), name='whoami'),
]
