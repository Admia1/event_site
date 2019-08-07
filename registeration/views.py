from django.contrib.auth import  login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from django.contrib.auth.models import User

from .models import Person


def farsi_to_english_digit(number_string):
    dic = {
    "۰" : "0",
    "۱" : "1",
    "۲" : "2",
    "۳" : "3",
    "۴" : "4",
    "۵" : "5",
    "۶" : "6",
    "۷" : "7",
    "۸" : "8",
    "۹" : "9",
    }
    for digit in dic:
        number_string = number_string.replace(digit, dic[digit])
    return number_string


def register_post_validator(post):
    def string_type_validator(field_name, field_max_length):
        if field_name not in post:
            return "field %s is missing"%field_name
        if len(post[field_name]) < 2 :
            return "field %s is too short"%field_name
        if len(post[field_name]) > field_max_length :
            return "field %s is too long"%field_name
        return ""

    for checking_field in ["first_name", "last_name", "national_id", "phone_number","email",]:
        res = string_type_validator(checking_field, 99)
        if res:
            return res
    ### missing check email $$$
    if len(post['national_id']) != 10:
        return "short or long national_id"

    for digit in post["national_id"]:
        if digit not in "0123456789۰۱۲۳۴۵۶۷۸۹":
            return "non numerical national_id"

    for digit in post['phone_number']:
        if digit not in "0123456789۰۱۲۳۴۵۶۷۸۹+":
            return "non numerical phone_number"

    if post['detail_type'] not in ['0','1','2','3','4']:
        return "bad format of detail_type"

    type = int(post['detail_type'])

    if type == 0:
        res = string_type_validator("guide_id", 99)
        if res:
            return res

    elif type == 1:
        for checking_field in ["university", "study_field", "student_id"]:
            res = string_type_validator(checking_field, 99)
            if res:
                return res
        for digit in post["student_id"]:
            if digit not in "0123456789۰۱۲۳۴۵۶۷۸۹":
                return "bad student_id format"

    elif type == 2:
        for checking_field in ["agency", "city",]:
            res = string_type_validator(checking_field, 99)
            if res:
                return res

    elif type == 3:
        for checking_field in ["hotel", "city",]:
            res = string_type_validator(checking_field, 99)
            if res:
                return res

    return ""


def register_view(request):
    template = 'registeration/register.html'
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('registeration:home'))
    else:
        if request.method == 'POST':
            #validation of data
            error_message = register_post_validator(request.POST)
            if error_message:
                # if user didnt registered before
                eng_national_id = farsi_to_english_digit(request.POST['national_id'])
                if ~(Person.objects.filter(national_id = eng_national_id).exists()):
                    # then create the user
                    user = User(
                        username = request.POST['email'],
                        password = farsi_to_english_digit(request.POST['national_id']),
                    )
                    user.save()
                    person = Person(user = user)
                    person.first_name = request.POST['first_name']
                    person.last_name = request.POST['last_name']
                    person.national_id = farsi_to_english_digit(request.POST['national_id'])
                    person.phone_number = request.POST['phone_number']
                    person.email = request.POST['email']
                    person.detail_type = int(request.POST['detail_type'])

                    type = person.detail_type
                    if type == 0:
                        person.guide_id = request.POST['guide_id']
                    elif type == 1:
                        person.university = request.POST['university']
                        person.study_field = request.POST['study_field']
                        person.student_id = request.POST['student_id']
                    elif type == 2:
                        person.agency = request.POST['agency']
                        person.city = request.POST['city']
                    elif type == 3:
                        person.hotel = request.POST['hotel']
                        person.city = request.POST['city']
                    elif type == 4:
                        comment = "do nothig"
                    else:
                        comment = "should not happen"
                    person.save()
                    login(request, user)
                    return HttpResponseRedirect(reverse('registeration:home'))

                else:
                    return render(request,template,{'error_message': "you,ve already registered"})
            else:
                return render(request,template,{'error_message': error_message})
        else:
            return render(request,template)

def login_view(request):
    template = 'registeration/login.html'
    if request.user.is_authenticated :
        return HttpResponseRedirect(reverse('registeration:home'))

    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            if User.objects.filter(username=request.POST['username']).exists():
                user = User.objects.get(username=request.POST['username'])
                if user.check_password(form.request.POST['password']):
                    login(request, user)
                    return HttpResponseRedirect(reverse('polls:home'))

        return render(request, template, {'error_message': 'Wrong username or password'})

    return render(request, template)


def home_view(request):
    template = 'registeration/home.html'
    return render(request,template)

def show_off_view(request):
    template = 'registeration/show_off.html'
    return render(request,template)
