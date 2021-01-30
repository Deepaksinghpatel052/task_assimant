from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(),name="ViewProduct"),
    path('create-product', views.CreateProjectView.as_view(),name="CreateProduct"),
    path('<pk>/update-product', views.ProductUpdateView.as_view(),name="update_product"),
    path('<slug:prodict_id>/deletye-product', views.ProductSoftleteView.as_view(),name="product_delete"),
]