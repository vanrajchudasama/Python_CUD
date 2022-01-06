from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',views.home,name="home"),
    path('delete/<int:id>/',views.delete_record,name="data_delete"),

]
