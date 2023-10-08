from django.urls import path
from trial import views 

app_name = 'trial'


urlpatterns = [
    
    path("t1/",views.greens,name="t1"),
    path("t2/",views.blue,name="t2"),
    path("t3/",views.grey,name="t3"),
    path("t4/",views.yellow,name="t4"),
    path("t5/",views.red,name="t5"),
    path("t6/<str:pk>",views.upd,name="t6"),
    path("t7/<str:pk>",views.dlt,name="t7"),
    path("t8/",views.orange.as_view(),name="t8"),

       ]





