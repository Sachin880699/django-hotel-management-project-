from django.urls import path
from.import views

urlpatterns = [
    path("",views.home,name="home"),
    path("room/",views.room,name="room"),
    path("about/",views.about,name="about"),
    path("room_info",views.room_info,name="room_info"),
    path("reserve/",views.reserve,name="reserve"),
    path("reserve_list/",views.reserve_list,name="reserve_list"),
    path("contact/",views.contact,name="contact")
]


