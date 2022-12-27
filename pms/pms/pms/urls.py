"""pms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('accounts/login/',signin),
    path('a/addstudent',addstudent),
    path('logout/',signout),
    path('a/',admi,name='admi'),
    path('a/students/',students,name='students'),
    path('a/studedit/<int:id>',studedit),
    path('a/studdelete/<int:id>',studdelete),
    path('changepassword/',changepassword),
    path('a/companies/',companies,name='companies'),
    path('a/comedit/<int:id>',comedit),
    path('a/comdelete/<int:id>',comdelete),
    path('a/addcompany/',addcompany),
    path('a/placements',placements),
    path('a/manage/<int:id>',manage),
    path('a/view/<int:id>',view),
    path('view/<int:id>',viewplace),
    path('placement/',placement),
    path('highlights/',highlights),
    path('a/highlights/',ahighlights),
    path('a/sendnotification/',sendnotification),
    path('a/managenotification/',managenotification,name="notifications"),
    path('a/delnotification/<int:id>',delnotification),
    path('notifications/',notifications)
    
]
