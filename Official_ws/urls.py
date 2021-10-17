from Official_ws  import views
from django.urls import path

urlpatterns=[
   path('index/',views.index,name='index'),
   path('about_us/',views.about_us,name='about_us'),
   path('courses/',views.courses,name='courses'),
   path('login/',views.login,name='login'),

]