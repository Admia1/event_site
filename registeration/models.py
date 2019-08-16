from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class EventGroup(models.Model):
    name = models.CharField(max_length=100)
    detail = models.TextField(max_length=1000)

class Person(models.Model):
    user = models.ForeignKey(User ,on_delete=models.CASCADE)

    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    national_id = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)

    person_type = models.IntegerField(default = 0)

    detail_type = models.IntegerField(default = 4)

    guide_id = models.CharField(default="-", max_length = 100)

    university = models.CharField(default="-", max_length = 100)
    study_field = models.CharField(default="-", max_length = 100)
    student_id = models.CharField(default="-", max_length = 100)

    agancy = models.CharField(default="-", max_length = 100)
    city = models.CharField(default="-", max_length = 100)

    hotel = models.CharField(default="-", max_length = 100)
    #city = models.CharField(default="-", max_length = 100)

    def is_staff(self):
        return self.person_id == 1

    def person_type_show(self):
        type_dictionary = {
        0 : "راهنمای گردشگری",
        1 : "دانشجو",
        2 : "کارمند دفاتر مسافرتی / تور اپراتور",
        3 : "کارمند هتل",
        4 : "آزاد",
        }

        if self.detail_type in type_dictionary:
            return type_dictionary[self.detail_type]
        else:
            return "خطا"

class Event(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=5000)#tooman.
    capacity = models.IntegerField(default=30)#People
    detail = models.TextField(max_length=1000)

    file_name = models.CharField(max_length=50)

    event_group = models.ForeignKey(EventGroup, on_delete=models.PROTECT)

class Invoice(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    event  = models.ForeignKey(Event, on_delete=models.PROTECT)
    amount = models.IntegerField(default=0)# tooman
    active = models.IntegerField(default=1)# 0: deactive     , 1: active
    paid   = models.IntegerField(default=0)# 0: never_paid , 1: $$$

    authority   = models.CharField(max_length = 200, default = "none")
    refid       = models.CharField(max_length = 200, default = "none")

    discount_pk = models.IntegerField(default=0)

    def is_successful(self):
        return self.status == 0


class Discount(models.Model):
    percent = models.IntegerField(default=0)
    #event   = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_group = models.ForeignKey(EventGroup, on_delete=models.PROTECT)
    code    = models.CharField(max_length=100)
    capacity = models.IntegerField(default=0)

    detail = models.CharField(max_length=100)
