from django.shortcuts import render
from .models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
import random
from django.conf import settings

def send_otp_to_mobile(mobile):
    try:
        otp = random.randint(1000,9999)
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{phone_number}/{otp}'
        response = requests.get(url)
        return otp
    except Exception as error:
        return None



@api_view(['POST'])
def send_otp(request):
    data = request.data
    if data.get('mobile') is None:
        return Response({"status":False, "message":"Mobile No is required"})

    if data.get('password') is None:
        return Response({"status":False, "message":"password is required"})

    user = User.objects.create(
        mobile = data.get('mobile'),
        otp = send_otp_to_mobile(data.get('mobile'))
    )
    user.set_password = data.get('set_password')
    user.save()
    return Response({"status":True, "message":"OTP sent Successfully !"})



