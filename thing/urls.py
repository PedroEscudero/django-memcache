from django.urls import path

from . import views
from thing.views import Middleware

urlpatterns = [
    path('chroniclingamerica', Middleware.as_view(), name='middleware_endpoint'),
]
