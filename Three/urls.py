from django.conf.urls import url

from Three import views

urlpatterns = [
    url('index/', views.index),
    url('get_grate/', views.get_grate),
    url('get_grate/', views.get_grate),
    url('get_student/', views.get_student),

    # url('add_student/', views.add_student),
    # url('get_student/', views.get_student),
    # url('update_student/', views.update_student),
    # url('delete_student/', views.delete_student)
]
