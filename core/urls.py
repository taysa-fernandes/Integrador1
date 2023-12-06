from django.contrib import admin
from django.urls import path
from  core.views import home, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('home/', home),
]
