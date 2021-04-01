from django.shortcuts import render
from apptwo import forms
# Create your views here.

def index(request):
    return render(request,'apptwo/index1.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            #DO SOMETHING CODE
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name']) 
            print("EMAIL: "+form.cleaned_data['email']) 
            print("TEXT: "+form.cleaned_data['text']) 

    return render(request,'apptwo/form_page.html',{'form':form})
