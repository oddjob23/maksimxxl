from django.urls import path
from .views import HomePageView, ProductDetailView, CategorieView
app_name = "maksim"
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>', ProductDetailView.as_view(), name='detail'),
    path('category/<category_name>', CategorieView.as_view(), name='category')
]
