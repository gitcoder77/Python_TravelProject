from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def demo(request):
   obj=Place.objects.all()
   tobj=Team.objects.all()

   return render(request,"index.html",{'result':obj,'tresult':tobj})
#def about(request):
#   return render(request,"about.html")
#def contact(request):
#   return render(request,"contact.html")
#def addition(request):
 #   x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
 #   res=x+y
 #   return render(request,"about.html",{'result':res})
