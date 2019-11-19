from django.urls import path
from .views import HomePageView, ProductDetailView, CollectionView
app_name = "maksim"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('kolekcija/<str:kolekcija>', CollectionView.as_view(), name='kolekcija')
]
