"""
URL configuration for hotel project.

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
from hotelapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('login/',views.login),
    path('createaccount/',views.createaccount),
    path('userlogin/',views.userlogin),
    path('userinput/',views.userinput),
    path('signup/',views.signup),
    path('admin1/',views.admin1),
    path('user1/',views.user1),
    path('addhotel/',views.addhotel),
    path('hotelinput/',views.hotelinput),
    path('viewhotel/',views.viewhotel),
    path('removehotel/',views.removehotel),
    path('delhotel/<int:id>',views.delhotel),
    path('hotelhomepage/',views.hotelhomepage),

  
    path('userview/',views.viewuser),
  
    path('addfood/',views.addfood),
    path('addfoodmenu/',views.addfoodmenu),
    path('viewfood/',views.viewfood),
    path('viewhotelprofile/',views.viewhotelprofile),
    path('addmenu/',views.addmenu),
    path('updateuser1/',views.updateuser1),
    path('updateuser2/<int:id>',views.updateuser2),
    path('updateuser3/<int:id>',views.updateuser3),
    path('updatehotel/',views.updatehotel1),
    path('updtRest2/<int:id>',views.updtRest2),
    path('updatehotel2/<int:id>',views.updatehotel2),
    path('addoffer/',views.addoffer),
    path('addoffersform/',views.addofferform),
    path('viewmenuitem/',views.viewfoodmenuitem),
    path('viewoffer/',views.viewoffer),
    

    
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
