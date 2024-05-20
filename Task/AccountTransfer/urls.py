from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.ListAccounts.as_view(), name='list'),
    path('update/', views.TransferView.as_view(), name='transfer'),

    # path('', views.ListView.as_view(), name='index'),
]
