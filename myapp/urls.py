from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login_view'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('book/', views.book, name='book'),
    path('register/', views.register, name='register'),
    path('cart/', views.cart, name='cart' ),
    path('additems/', views.additems, name='additems'),
    path('viewitem/', views.viewitem, name='viewitem'),
    path('update_item/<int:item_id>/', views.update_item, name='update_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)