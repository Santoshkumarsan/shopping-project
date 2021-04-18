from django.urls import path,include
from django.conf.urls import url
from printapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main_view),
    path('home/',views.main_view2),
    path('stampppp/',views.stamps_view),
    path('stamp2/',views.stamps_view_2),
    path('contact/',views.contact_us_view),
    path('contactus/',views.contact_us_2_view),
    path('about/',views.about_us_view),
    path('signup/', views.signup_view), 
    path('accounts/',include('django.contrib.auth.urls')), 
    #path('list/',views.list_view.as_view(),name='listcat'),
    path('stamp/',views.list_view.as_view(),name='stamplist'),
    path('category/<int:pk>/', views.stamp_detail_view.as_view(),name='stampdetails'),
    
    #url(r'^(?P<id>\d+)/product', views.stamp_detail_view, name='detail'),
   # path('product/',views.stamp_detail_view),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

