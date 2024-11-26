from django.urls import path
from homepage.views import homepage

urlpatterns = [
    path('home/', homepage, name='homepage'),  # URL para a homepage
]
