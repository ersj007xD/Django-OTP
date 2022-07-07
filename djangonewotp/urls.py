from django.contrib import admin
from django.urls import path
from otp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('send_otp/', send_otp)
]
