from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(resquest):
    
    return HttpResponse(
        """
        <h1> Esta en el Home </h1>
        
        """ 
    )
    
def about(resquest):
    
    return HttpResponse(
        """
        <h1> Esta en el About</h1>
        
        """ 
    )    
    
def contac(resquest):
    return render(resquest,'plantilla.html')   