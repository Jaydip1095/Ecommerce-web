"""
URL configuration for watchs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import index,register,signin,signout,about,contact,checkout,feedback
from .views import confirmation_view,place_order,home

urlpatterns = [
    path('admin/',admin.site.urls),
    path('',register,name='register'),
    path('signin/',signin,name='signin'),
    path('signout/',signout,name='logout'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('home/',home, name='home'),
    path('',include('shop.urls')),
    path('', include('cart.urls')),
    path('',include('feedback.urls')),
    path('feedback/',feedback, name='feedback'),
    path('signin/checkout.html',checkout,name='checkout'),
    path('cart/placeorder/', place_order, name='place_order'),
    path('cart/placeorder/confirmation.html/', confirmation_view, name='confirmation'),
    path('',index),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
