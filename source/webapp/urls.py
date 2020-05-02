from django.urls import path
from webapp.views.category_views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from webapp.views.product_views import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='caretories_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/change/<int:pk>/', CategoryUpdateView.as_view(), name='category_change'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]
