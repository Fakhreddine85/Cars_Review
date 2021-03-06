from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...


# Create a `contact` view to return a static contact page
#def contact(request):

# Create a `login_request` view to handle sign in request
# def login_request(request):
# ...
def login_request(request):
    context = {}
    if request.method == "Post":
        #get username and password from request.post dictionary
        username = request.POST['username']
        password = request.POST['password']
        #Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid cll login method to login current user
            login(request,user)
            return render(request,'djangoapp/index.html',context)
        else:
            # If not, return to login page again 
            return render(request,'djangoapp/index.html',context)
    else:
        return render(request, 'djangoapp/index.html')

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
# ...
def logout_request(request):
    #Get the user object based on session id in request
    print("log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to the home page 
    return redirect ('djangoapp/index.html')
# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...
def registration_request(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/registration.html', context)
# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

