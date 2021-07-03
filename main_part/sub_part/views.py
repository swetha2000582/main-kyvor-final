from django.shortcuts import render,redirect
from . models import form_info

# Create your views here.
def index(request):
    products=form_info.objects.all()
    context={'products':products}   
    return render(request,'index.html', context)
    

def instruclogin(request):
    
    return render(request,'instruclogin.html')  

def instructreg(request):
    return render(request,'instructreg.html') 


def show(request,id):
    items=form_info.objects.get(id=id)
    context={'items':items}
    return render(request,'show.html',context)       

def forms(request):
    if request.method=='POST':
        adding=form_info()
        adding.first_name=request.POST.get('enter_first')
        adding.last_name=request.POST.get('enter_last')
        adding.short_name=request.POST.get('enter_short')
        adding.first_name=request.POST.get('enter_first')
        if len(request.FILES) != 0:
             adding.image=request.FILES['images']
        adding.contacts=request.POST.get('enter_contact')
        adding.contacts_ext=request.POST.get('enter_contact_ext')
        adding.team=request.POST.get('enter_team')
        adding.job_title=request.POST.get('enter_job_title')
        adding.join_date=request.POST.get('datetime')
        adding.last_date=request.POST.get('last_datetime')
        adding.email_id=request.POST.get('enter_email')
        adding.titleof=request.POST.get('titleof')
        adding.save()
        
        return redirect(index)         
    return render(request,'forms.html',)      