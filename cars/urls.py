from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^cars/(?P<id>\d+)/?', views.delete_by_id),

    re_path(r'^cars/?$', views.handle_cars),

    re_path(r'^rate/?$', views.add_rate_by_id),

    re_path(r'^popular/?$', views.get_cars_with_rates),
]