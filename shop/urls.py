from . import views
from django.urls import path

urlpatterns = [
    path('categories/', views.CategoryListView.as_view()),
    path('category/<slug:slug>/detail', views.CategoryDetail.as_view()),
    path('category-create/', views.CreateCategoryView.as_view()),
    path('category/<slug:slug>/update/', views.UpdateCategoryView.as_view()),
    path('category/<slug:slug>/delete/', views.DeleteCategoryView.as_view()),
    path('category/<slug:category_slug>/<slug:group_slug>/', views.ProductListView.as_view()),

    # group
    path('category/<slug:slug>/', views.GroupListView.as_view()),
]