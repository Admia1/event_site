from django.contrib.auth import  login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import datetime
from furl import furl
from zeep import Client
import json

from django.contrib.auth.models import User

from django.contrib.staticfiles.templatetags.staticfiles import static
from .models import Person, Invoice, Event, Discount, EventGroup

from . import secret

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

    if post['detail_type'] not in ['0','1','2','3', '4']:
        return "bad format of detail_type"

    type = int(post['detail_type'])

    if type == 0:
        # res = string_type_validator("guide_id", 99)
        # if res:
        #     return res
        comment = "do nothing"

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
        return HttpResponseRedirect(reverse('registeration:event_group', kwargs={'event_group_pk':1}))
    else:
        if request.method == 'POST':
            #validation of data
            error_message = register_post_validator(request.POST)
            if not error_message:
                # if user didnt registered before
                if not Person.objects.filter(national_id = request.POST['national_id']).exists():
                    # then create the user
                    user = User(
                        username = request.POST['email'],
                    )
                    user.set_password(request.POST['national_id'])
                    user.save()
                    person = Person(user = user)
                    person.first_name = request.POST['first_name']
                    person.last_name = request.POST['last_name']
                    person.national_id = request.POST['national_id']
                    person.phone_number = request.POST['phone_number']
                    person.email = request.POST['email']
                    person.detail_type = int(request.POST['detail_type'])

                    type = person.detail_type
                    if type == 0:
                        if 'guide_id' in request.POST:
                            if request.POST['guide_id']:
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
                    return HttpResponseRedirect(reverse('registeration:event_group', kwargs={'event_group_pk':1}))

                else:
                    return render(request,template,{'error_message': "شما قبلا این بلیط را خریده اید"})
            else:
                return render(request,template,{'error_message': error_message})
        else:
            #load page for first time
            return render(request,template)

def login_view(request):
    template = 'registeration/login.html'
    if request.user.is_authenticated :
        return HttpResponseRedirect(reverse('registeration:event_group', kwargs={'event_group_pk':1}))

    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            if User.objects.filter(username=request.POST['username']).exists():
                user = User.objects.get(username=request.POST['username'])
                if user.check_password(request.POST['password']):
                    login(request, user)
                    return HttpResponseRedirect(reverse('registeration:event_group', kwargs={'event_group_pk':1}))
                else:
                    return render(request, template, {'error_message': 'رمز عبور نادرست است'})
            else:
                return render(request, template, {'error_message': 'ایمیل شما در سایت ثبت نشده است'})
        else:
            return render(request, template, {'error_message': 'missing username or password in json'})

    return render(request, template)


def user_page_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('registeration:login'))
    template = 'registeration/user_page.html'
    event_groups = EventGroup.objects.all()
    person = Person.objects.get(user=request.user)
    tickets = Invoice.objects.filter(paid=1, person=person)
    return render(request,template,{'event_groups' : event_groups, 'tickets' : tickets})

def home_view(request):
    template = 'registeration/home.html'
    return render(request,template)

def verify_view(request):
    MERCHANT = secret.MERCHANT
    if request.GET.get('Status') == 'OK':
        authority = request.GET['Authority']
        try:
            invoice = Invoice.objects.get(authority=authority)
        except:
            return HttpResponseRedirect(reverse('registeration:error'))

        client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
        result = client.service.PaymentVerification(MERCHANT, invoice.authority, invoice.amount)
        if result.Status == 100 or result.Status == 101:
            #payed
            invoice = Invoice.objects.get(authority=request.GET['Authority'])
            invoice.refid = result.RefID
            invoice.active = 1
            invoice.paid = 1
            invoice.save()

            for o_invoice in Invoice.objects.filter(person=invoice.person, event=invoice.event, active=1):
                if o_invoice.pk != invoice.pk:
                    o_invoice.active=0
                    o_invoice.save()
            return HttpResponseRedirect("%s?payment_success=true" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))
            
        else:
            #failed to pay
            invoice.active = 0
            invoice.save()
            return HttpResponseRedirect("%s?payment_error=پرداخت ناموفق" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))

    return HttpResponseRedirect("%s?payment_error=پرداخت ناموفق" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))


def purchase_view(request, event_pk):
    invoice_cleaner()
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('registeration:login'))

    template = 'registeration/user_page.html'
    try :
        person = Person.objects.get(user=request.user)
    except:
        return render(request, template, {'error_message': 'bad person'})
    try:
        event  = Event.objects.get(pk = event_pk)
    except:
        return render(request, template, {'error_message': 'همچین رویدادی وجود ندارد'})
    
    if request.method != 'POST':
        return error(request)
    if 'discount_code' not in request.POST:
        return error(request)
    
    if request.POST['discount_code']:
        try:
            discount = Discount.objects.get(event_group=event.event_group, code=request.POST['discount_code'])#debug event
            discount_pk = discount.pk
        except:
            return HttpResponseRedirect("%s?payment_error=این کد تخفیف نامعتبر است" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))

    else:
        discount_pk = 0
    if Invoice.objects.filter(event=event, person=person, paid=1).exists():
        return HttpResponseRedirect("%s?payment_error=شما قبلا بلیط این رویداد را خریداری کرده اید" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))        
    
    #cheat the cheaters
    for invoice in Invoice.objects.filter(active=1, paid=0, amount=event.price, event=event, discount_pk=discount_pk, person=person):
        if datetime.datetime.now(datetime.timezone.utc)- invoice.created_date > datetime.timedelta(minutes=15):
            #come back so soon ? use old link
            return redirect('https://www.zarinpal.com/pg/StartPay/' + str(invoice.authority))
        else:
            #else make new and kill old :D
            n_invoice = Invoice(active=1, paid=0, person=invoice.person, amount=invoice.amount, event=invoice.event)
            invoice.active=0
            n_invoice.save()
            invoice.save()
            return send_to_zarin(request, invoice)

    if Invoice.objects.filter(event=event, active=1).count() >= event.capacity:
        invoice_cleaner()# :/
        if Invoice.objects.filter(event=event, active=1).count() >= event.capacity:
            return HttpResponseRedirect("%s?payment_error=ظرفیت این رویداد به اتمام رسیده است" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))        


    amount  = event.price
    invoice = Invoice.objects.create(person=person, event=event, amount=amount)

    if Invoice.objects.filter(event=event, active=1).count() > event.capacity:
        invoice.active=0
        invoice.save()
        return HttpResponseRedirect("%s?payment_error=ظرفیت این رویداد به اتمام رسیده است" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))        
        
    #cant turn off other invoices of this person :(
    #change amount for off here

    if request.POST['discount_code']:
        if Invoice.objects.filter(discount_pk=discount.pk, event=event, active=1).count() >= discount.capacity:
            invoice.active=0
            invoice.save()
            return HttpResponseRedirect("%s?payment_error=دفعات مجاز استفاده از این کد تخفیف به پایان رسیده است" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))        

        invoice.discount_pk = discount.pk

        if discount.percent >= 0 and discount.percent <= 100:
            invoice.amount = invoice.amount * (100 - discount.percent) / 100
            invoice.save()

        if Invoice.objects.filter(discount_pk=discount.pk, event=event, active=1).count() > discount.capacity:
            invoice.active=0
            invoice.save()
            return HttpResponseRedirect("%s?payment_error=دفعات مجاز استفاده از این کد تخفیف به پایان رسیده است" % reverse('registeration:event_group', kwargs={'event_group_pk':1}))        

    return send_to_zarin(request, invoice)




def send_to_zarin(request, invoice):
    template = 'registeration/user_page'
    MERCHANT = secret.MERCHANT
    client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
    description = "جهت خرید بلیط "  + invoice.event.name               # Required
    email  = invoice.person.email                         # Optional
    mobile = invoice.person.phone_number                  # Optional
    CallbackURL = furl(request.build_absolute_uri(reverse("registeration:verify")))
    
    amount = invoice.amount

    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        invoice.authority = result.Authority
        invoice.save()
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        invoice.active = 0
        invoice.save()
        return render(request, template, {'error_message':'خطای درگاه'})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect(reverse('registeration:home'))

def error(request):
    return HttpResponse("error")


def invoice_cleaner():
    for invoice in Invoice.objects.filter(active=1, paid=0):
        if  datetime.datetime.now(datetime.timezone.utc) - invoice.created_date > datetime.timedelta(hours=1):
            invoice.active=0
            invoice.save()

def event_group_view(request, event_group_pk):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("registeration:login"))
    template = 'registeration/event_group.html'
    try:
        event_group = EventGroup.objects.get(pk=event_group_pk)
    except:
        return error(request)
    events = Event.objects.filter(event_group=event_group)

    for event in events:
        if Invoice.objects.filter(event=event, person=Person.objects.get(user=request.user), paid=1).exists():
            
            ticket_data = {
                'event': event
            }

            # hardcoded
            if event.name == 'شیراز':
                logos = [
                    static('home/hami1.jpg'),
                    static('home/hami4.jpg'),
                    static('home/shiraz_uni.jpg'),
                ]
            else:
                logos = []

            ticket_data['logos'] = logos

            return render(request, 'registeration/event_group_paid.html', {
                'ticket_data': ticket_data,
                'payment_success' : request.GET.get('payment_success', '')
            })

    return render(request, template, {
        'events' : events,
        'discount_check_url': furl(request.build_absolute_uri(reverse("registeration:discount_check", kwargs={'event_group_pk': event_group_pk}))),
        'payment_error' : request.GET.get('payment_error', ''),
        'payment_success' : request.GET.get('payment_success', '')
    })


@csrf_exempt
def discount_check_api(request, event_group_pk):
    # if not request.user.is_authenticated:
    #     return JsonResponse({"status" : "error", "error_message" : "access denied"})

    if request.method != "POST":
        return JsonResponse({"status" : "error", "error_message" : "it should be post"})
    data = json.loads(request.body)
    if 'discount_code' not in data:
        return JsonResponse({"status" : "error", "error_message" : "bad json format"})

    try:
        event_group = EventGroup.objects.get(pk=event_group_pk)
    except:
        return JsonResponse({"status" : "ok", "result" : "error", "error_message" : "همچین رویدادی وجود ندارد"})

    try:
        discount = Discount.objects.get(code=data['discount_code'], event_group=event_group)
    except:
        return JsonResponse({"status" : "ok", "result" : "error", "error_message" : "این کد تخفیف برای این رویداد نامعتبر است"})

    invoice_cleaner()

    if Invoice.objects.filter(discount_pk = discount.pk, active=1).count() >= discount.capacity :
        return JsonResponse({"status" : "ok", "result" : "error", "error_message" : "دفعات مجاز استفاده از این کد تخفیف به پایان رسیده است"})

    return JsonResponse({"status" : "ok", "result" : "ok", "percent" : discount.percent})
