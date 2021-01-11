from django.urls import path,include
from django.conf.urls import url
from printapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.main_view),
    path('home/',views.main_view2),
    path('stamp/',views.stamps_view),
    path('stamp2/',views.stamps_view_2),
    path('contact/',views.contact_us_view),
    path('contactus/',views.contact_us_2_view),
    path('about/',views.about_us_view),
    path('signup/', views.signup_view), 
    path('accounts/',include('django.contrib.auth.urls')), 
    #path('category/<int:id>/<slug:slug>/', views.stamp_detail_view,name='product_detail'),

    path('product/',views.stamp_detail_view)
    #url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/', views.stamp_detail_view,name='post_detail'),  
 
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

