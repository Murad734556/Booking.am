from django.urls import path 
from apps.hotels.views import hotel_detail

urlpatterns = [
    path('hotel/<int:id>', hotel_detail, name="hotel_detail" )

]