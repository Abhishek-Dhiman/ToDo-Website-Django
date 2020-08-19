from django.urls import path
from . import views

urlpatterns = [
	path('',views.home,name='home'),
	path('dashboard/',views.dashboard,name='dashboard'),
	path('update/<str:key>/',views.update,name='update'),
	path('delete/<str:key>/',views.delete,name='delete')
]