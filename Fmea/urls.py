
from Fmea import views

from .views import CreatePostView

from django.urls import re_path



urlpatterns = [
    
    re_path(r'^$',views.index,name="index"),
    
    
    re_path(r'^post/$', CreatePostView.as_view(), name='add_post'),
    
    ]