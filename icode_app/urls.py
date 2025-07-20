from django.urls import path,include
from icode_app import views

urlpatterns = [
    path('',views.Homeview.as_view()),
    path('insertcontact',views.insertcontact,name="insertcontact"),
    path('insertreservation',views.insertreservation,name="insertreservation")
]