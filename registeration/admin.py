from django.contrib import admin
from .models import Event, Invoice, Person, Discount, EventGroup, Visitor
# Register your models here.


admin.site.register(Event)
admin.site.register(Invoice)
admin.site.register(Person)
admin.site.register(Discount)
admin.site.register(EventGroup)
admin.site.register(Visitor)
