from django.urls import path
from blogs.views import blogs_view


urlpatterns = [
    path('post/', blogs_view)
]