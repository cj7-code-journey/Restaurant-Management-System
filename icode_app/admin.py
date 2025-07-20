from django.contrib import admin
from icode_app.models import *
# Register your models here.
@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
     list_display = ('Fname','email','phone','Queries','massage')

@admin.register(reservation)
class reservationAdmin(admin.ModelAdmin):
     list_display = ('Party_size','Reservation_Date','Reservation_Time','name2','email2','Special_Request')
    