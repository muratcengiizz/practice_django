from django.urls import path 
from . import views 

urlpatterns = [ 
    path('', views.index, name="index"),
    path("iletisim", views.iletisimm, name="iletisim"),
    path('hakkimda', views.hakkimda, name="hakkimda"),
    
    path("yazilar", views.yazilarr, name="yazilar"),
    
    path("yazilar/<category>", views.yazi1, name="yazi1")
]