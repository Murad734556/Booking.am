from django.urls import path 
from apps.hotels.views import hotel_detail, hotels

urlpatterns = [
    path('hotel/<int:id>', hotel_detail, name="hotel_detail" ),
    path('hotels/<int:id>', hotels, name="hotels")

]