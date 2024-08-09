from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/budgeting/', include('budgeting.urls')),
    path('api/investments/', include('investments.urls')),
   # path('api/goals/', include('goals.urls')),
    #path('api/risk/', include('risk.urls')),
    
]
