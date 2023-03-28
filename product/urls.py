from django.urls import path 
from .views import * 

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list_view'),
    path('create', ProductCreateAPIView.as_view(), name='product_create_view'),
    path('update/<int:id>', ProductUpdateView.as_view(), name='product_update_view'),
    path('delete/<int:id>', ProductDeleteView.as_view(), name='product_delete_view')
]
