from .views import BookList, BookViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

#Register the BookViewSet with the router:
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    # Maps to the BookList view
    path('', BookList.as_view(), name='book-list'),
    # Include the router URLs for BookViewSet 
    path('', include(router.urls)),
]
