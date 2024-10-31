from django.urls import path
app_name = 'conversation'
from . import views

urlpatterns = [
    path("", views.new_conversation, name="new-conversation"),
]
