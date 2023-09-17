from django.urls import path
from contact.views import index

app_name = 'contact'
urlpatterns = [
    path('', index, name='index'),
]
