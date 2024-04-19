# from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

######### file import  #########
from .views import * 




urlpatterns = [

        
    ##############################  all page  ##############################
    
    path('dashboard/', dashboard, name="dashboard"),
 

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

