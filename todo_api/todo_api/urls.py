from django.conf.urls import url
from django.urls import include

urlpatterns = [
    url('api/v1/', include('todo.urls')),
]