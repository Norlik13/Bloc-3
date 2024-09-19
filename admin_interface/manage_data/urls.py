from django.urls import path
from .views import *

urlpatterns = [
#-----Gestion des éléments-----
    path('', ItemListView.as_view(), name='item-list'),
    path('create/', ItemCreateView.as_view(), name='item-create'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('<int:pk>/update/', ItemUpdateView.as_view(), name='item-update'),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name='item-delete'),

#-----Gestion des utilisateurs-----
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
