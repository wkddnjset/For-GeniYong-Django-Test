from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^test/', PostList.as_view()),
]
