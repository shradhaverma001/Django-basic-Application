from django.shortcuts import render
from django.shortcuts import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.

# def index(request):
#     return HttpResponse("Hello World!")
def index(request):
    # my_dict={'insert_me':"Hello I am from views.py!"}
    # my_dict={'insert_me':"Now I am coming from first_app/index.html!"}
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'first_app/index.html',context=date_dict)
    