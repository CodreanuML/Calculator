from django.urls import include,path

app_name="CALC"

from . import views as CALC_VIEWS




urlpatterns = [
	path('calc/',CALC_VIEWS.main,name='calc'),
]