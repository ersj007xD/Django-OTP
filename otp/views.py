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
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/{mobile}/{otp}'
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

    
    try:
        otp = send_otp_to_mobile(data.get('mobile'))
        result = dict()
        result["data"] = otp
        return Response({"status":True, "result": result, "message":"OTP sent Successfully !"})
    except Exception as error:
        return Response({"status":False, "result": dict(), "message":"OTP doesn't send Successfully !"})



