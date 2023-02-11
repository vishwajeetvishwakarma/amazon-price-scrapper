from django.urls import path
from . import views
urlpatterns = [
    path("", views.home_page, name="home"),
    path("delete/<int:pk>/", views.ProductDeleteView.as_view(),
         name="delete-product"),
    path("update/", views.update_price, name="update"),
]
