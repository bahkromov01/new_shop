from shop.views import CategoryListView, CategoryDetail, CreateCategoryView, UpdateCategoryView, DeleteCategoryView, ProductListView, ProductDetail
from django.urls import path

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('category-create/', CreateCategoryView.as_view(), name='category_create'),
    path('category/<slug:slug>/update/', UpdateCategoryView.as_view(), name='category_update'),
    path('category/<slug:slug>/delete/', DeleteCategoryView.as_view(), name='category_delete'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<slug:slug>/', ProductDetail.as_view(), name='product_detail'),

]