"""django_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path

urlpatterns = [
    path('', views.go_to_function, name="go_to_function"),
    path('laptops', views.get_laptops, name="get_laptops"),
    path('get_laptop_details', views.get_laptop_details, name="get_laptop_details"),
    # path('save_prod', views.go_to_function, name="go_to_function"),
    path('show_models', views.show_models, name="show_models"),
    path('add_cellphones', views.add_cellphones, name="add_cellphones"),
    path('get_cell_details', views.get_cell_details, name="get_cell_details"),
    path('delete_mob', views.delete_mob, name="delete_mob"),
]
