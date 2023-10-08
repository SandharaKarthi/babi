from django.shortcuts import render
from django.http import HttpResponse
from trial.models import employee_details
from trial.forms import f1, f2
from django.views.generic import TemplateView 


# Create your views here.

def greens(request):
    return HttpResponse('HI.... i am greens function views')

def blue(request):
    a=105
    b=[6,4,2,9,5,1]
    z = {"ki":a,"kl":b}
    return render(request,'fst.html', context=z)

def grey(request):
    a = employee_details.objects.all()
    return render(request,'R.hml', {'dataa:a'})

def yellow(request):
    a = f1()
    if request.method == 'POST':
         a = f1(request.POST)
         if a.is_valid():
              pass
    return render(request,'c.html', {'fr':a})

def red(request):
       a = f2()
       if request.method == "POST":
            a = f2(request.POST)
            if a.is_valid():
                 a.save()
                 return grey(request)
       return render(request, 'cr.html', {'fr':a})

                             
def upd(request,pk):
     a = employee_details.objects.get(Emp_id=pk)
     b = f2(instance=a)
     if request.method == "POST":
          b = (request.POST, instance=a)
          if b.is_valid():
          b.save()
          return grey(request) 
     return render(request, "upd.html", {'fr':b})

def dlt(request,pk):
     a = employee_details.objects.get(Emp_id=pk)
     if request.method == "POST":
         return grey(request)
     return render(request, 'dlt.html' {'gt':a})

class orange(TemplateView):
     template_name = "or.html"

     def get_context_data(self, **kwargs):
         a = super().get_context_data()
         a['ke'] = 10
         a['kj'] = 26
         return a







    

