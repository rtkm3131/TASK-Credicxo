from django.contrib import admin
from django.urls import include, path
from . import views

app_name="accountinfo"

urlpatterns = [
	# path('admin/', admin.site.urls),
	path('', views.returnData, name="returnData"),
	path('add_student/', views.add_student, name="add_student"),
	path('add_teacher/', views.add_teacher, name="add_teacher")
]