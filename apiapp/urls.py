from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.member_list),
    path('members/<int:pk>', views.member_detail),
]