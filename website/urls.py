from django.urls import path
from .views import HomePageView, ProductDetailView
app_name = "maksim"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),

]
