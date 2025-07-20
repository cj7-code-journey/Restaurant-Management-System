from django.db import models

# Create your models here.
# class contact(models.Model):
#     Name=models.CharField(max_length=100)
#     Queries=models.CharField(max_length=100)
#     Email=models.CharField(max_length=100)
#     Phone=models.CharField(max_length=100)
#     Massage=models.CharField(max_length=100)
#     class Meta:
#         db_table="contact"
class contact(models.Model):
    Fname=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    Queries=models.CharField(max_length=100)
    massage=models.CharField(max_length=100)
    class Meta:
        db_table="contact"

class reservation(models.Model):
    Party_size=models.CharField(max_length=100)
    Reservation_Date=models.CharField(max_length=100)
    Reservation_Time=models.CharField(max_length=100)
    name2=models.CharField(max_length=100)
    email2=models.CharField(max_length=100)
    Special_Request=models.CharField(max_length=100)
    class Meta:
        db_table="reservation"