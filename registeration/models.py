from django.db import models

# Create your models here.
class person(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    national_id = models.IntegerField()
    phone_number = models.IntegerField()
    email = models.EmailField(max_length = 100)

    person_type = models.IntegerField()

    detail_type = models.IntegerField()

    guide_id = models.CharField(max_length = 100)
    university = models.CharField(max_length = 100)
    study_field = models.CharField(max_length = 100)
    student_number = models.IntegerField()
    agancy = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)



    def is_staff(self):
        return self.person_id == 2799

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
