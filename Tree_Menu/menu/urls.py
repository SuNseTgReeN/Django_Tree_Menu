from django.urls import path

from .views import MenuListView, MenuDetailView

app_name = 'menu'

urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),
    path('<slug:parent_slug>/<slug:slug>/', MenuDetailView.as_view(), name='menu_detail'),
]
