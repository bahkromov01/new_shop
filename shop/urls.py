from . import views
from django.urls import path
from shop.auth.views import LoginAPIView, LogoutAPIView, RegisterAPIView
from confic.custom_obtain_views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('category/', views.CategoryListView.as_view()),
    path('category/<slug:slug>/detail', views.CategoryDetail.as_view()),
    path('category-create/', views.CreateCategoryView.as_view()),
    path('category/<slug:slug>/update/', views.UpdateCategoryView.as_view()),
    path('category/<slug:slug>/delete/', views.DeleteCategoryView.as_view()),
    path('category/<slug:category_slug>/<slug:group_slug>/', views.ProductListView.as_view()),
    path('product/<slug:slug>/products/attributes/', views.ProductAttributeView.as_view(), name='product-attributes'),

    # group
    path('category/<slug:slug>/', views.GroupListView.as_view()),

    # Auth
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),

    # JWT
    path('register-page/', RegisterView.as_view(), name='register'),
    path('login-page/', LoginView.as_view(), name='login'),
    path('logout-page/', LogoutView.as_view(), name='logout'),

]