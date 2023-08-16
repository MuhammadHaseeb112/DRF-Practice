from django.shortcuts import render,redirect
from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests
# Create your views here.
def home(request):
    # Set the API URL
    api_url = 'http://127.0.0.1:8000/api/stuAPI/'  # Replace with your actual API URL

    # Set the headers with JWT token
    # token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4NDEzMjMzLCJpYXQiOjE2ODg0MDk2MzMsImp0aSI6ImZiOThlNjgzOGQ1MTQ0OTFhYzUwMzMxMWEwNWY5MjU0IiwidXNlcl9pZCI6Mn0.dTMTEhDbl2M8Bt17npMGGK1tyop-4cbrRIPCOMRJe_o'  # Replace with the JWT token obtained from authentication
    access_token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {access_token}'}

    # Make the request to the API view
    response = requests.get(api_url, headers=headers)
    data = response.json()

    print(data)

    api_url = 'http://127.0.0.1:8000/api/tecAPI/'
    # Process the data as needed
    response2 = requests.get(api_url, headers=headers)
    data2 = response2.json()

    return render(request, 'home.html', {'data': data,'data2': data2})

from django.contrib.auth.models import User, auth 
from rest_framework_simplejwt.tokens import RefreshToken
def login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            username = username.strip()
            password = password.strip()
            # user = auth.authenticate(username==username,password==password)
            user = auth.authenticate(username=username,password=password)
            


            if user is not None :
                print("you are login")
                # messages.info(request, "Wellcome "+username)
                print("Wellcome")

                auth.login(request, user)
                request.session['username'] = username
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)

                # Store the access token in the session or return it as JSON response
                request.session['access_token'] = access_token
                # Alternatively, return the access token as a JSON response
                # return JsonResponse({'access_token': access_token})
                
                s_user= request.session['username']

                print('you are ' , request.session.get('username'))
                print('user = ', s_user)
                return redirect("home")
            else:
                # messages.info(request, "invalid username or password")
                print("invalid username or password")
               
                return redirect("login")

        else:
            return render(request,'login.html')
    else:
        # messages.info(request, "your account is already login! please logout first")
        print("your account is already login! please logout first")
        return redirect('home')
    

def logout(request):
    auth.logout(request)
    # del request.session['access_token']
    request.session.flush()
    request.session.clear_expired()
    print('you are ' , request.session.get('username'))
    print('you are ' , request.session.get('access_token'))
    return redirect('home')