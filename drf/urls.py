from django.urls import path
# from .views import get_products, create_products, update_product, get_product, delete_product
# from .views import ProductAPI
# from rest_framework.routers import DefaultRouter
# from .views import ProductViewSet
from .views import ProductListCreate

# router = DefaultRouter()
# router.register('products', ProductViewSet)

urlpatterns = [
    # path('products/', get_products),
    # path('products/<int:pk>', get_product),
    # path('products/delete/<int:pk>', delete_product),
    # path('products/add/', create_products),
    # path('products/update/<int:pk>', update_product),
    # path('products/', ProductAPI.as_view()),
    path('products/', ProductListCreate.as_view()),
]

# urlpatterns = router.urls