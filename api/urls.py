from django.urls import path
from . import views

urlpatterns = [
    path('tables/', views.getTableNames),
    path('tables/<str:name>/', views.getTableData),
    path('test/', views.test),
	path('tables/<str:name>/post', views.postTableData)
]
