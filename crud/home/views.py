from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse

# Create your views here.

def home(request):
    
    
    # If the request method is GET, retrieve data from the API
    response = requests.get('http://127.0.0.1:8000/product/ProductAPI/')
    data = response.json()
    
    return render(request, 'home.html', {'data': data})
    

def post(request):
    if request.method == 'POST':
        # Assuming you have form data in the request.POST dictionary
        form_data = request.POST
        file_data = request.FILES # Access uploaded files using request.FILES

        # Make a POST request to the API
        api_url = 'http://127.0.0.1:8000/product/ProductAPI/'
        # response = requests.post(api_url, data=form_data)
        response = requests.post(api_url, data=form_data, files=file_data)

        
        # Check the response status code to ensure successful post
        if response.status_code == 201:  # Assuming 201 means successful creation
            print('Data posted successfully!')
            return redirect(home)
        else:
            return HttpResponse('Failed to post data.')
    return render(request, 'post.html')





def edit(request, id):
    if request.method == 'POST':
        # Assuming you have form data in the request.POST dictionary
        form_data = request.POST
        file_data = request.FILES
        # Make a POST request to the API
        api_url = 'http://127.0.0.1:8000/product/ProductAPI/'+str(id)+'/'

        
        response = requests.put(api_url, data=form_data, files=file_data)
        # response = requests.patch(api_url, data=form_data)

        # print(response.status_code)
        # Check the response status code to ensure successful post
        if response.status_code == 200:  # Assuming 201 means successful creation
            print('Data posted successfully!')
            return redirect(home)
        else:
            print(response.status_code)
            return redirect(home)
            # return HttpResponse('Failed to post data.')
    url= 'http://127.0.0.1:8000/product/ProductAPI/'+ str(id)+'/'
    print(url)
    response = requests.get(url)
    data = response.json()
    return render(request, 'edit.html',{'data':data})


def delete(request, id):
    url= 'http://127.0.0.1:8000/product/ProductAPI/'+ str(id)+'/'
    print(url)
    response = requests.delete(url)
    return redirect(home)
    