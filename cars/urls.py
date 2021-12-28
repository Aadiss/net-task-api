from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.handle_cars),
    path('cars', views.handle_cars),

    path('cars/<int:id>', views.delete_by_id),
    path('cars/<int:id>/', views.delete_by_id),

    path('rate/', views.add_rate_by_id),
    path('rate', views.add_rate_by_id),

]