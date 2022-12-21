from django.shortcuts import render
from django.views.generic import ListView, CreateView,UpdateView # new
from django.urls import reverse_lazy # new
from django.http import HttpResponse
from .models import Fmea_Record


def index(request):
    webpage_list_fmea = Fmea_Record.objects.order_by("Occ")
    ncr_dict_fmea ={'access_records_fmea': webpage_list_fmea}
    return render(request,'Fmea_status.html',context=ncr_dict_fmea)


    
    
from .forms import PostForm # new
class CreatePostView(CreateView): # new
    model = Fmea_Record
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('index')
