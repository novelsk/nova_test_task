from django.urls import path
from . import views

app_name = 'service'

urlpatterns = [
    path('api/message/', views.api_webhook),
    path('api/set_webhook/', views.api_get_webhook_info),
    path('api/get_webhook_info/', views.api_get_webhook_info),
]
