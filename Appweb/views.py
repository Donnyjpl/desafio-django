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
    
    return HttpResponse(
    """
        <form action="" method="post">
            <ul>
                <li>
                <label for="name">Nombre:</label>
                <input type="text" id="name" name="user_name" />
                </li>
                <li>
                <label for="mail">Correo electrónico:</label>
                <input type="email" id="mail" name="user_mail" />
                </li>
                <li>
                <label for="msg">Mensaje:</label>
                <textarea id="msg" name="user_message"></textarea>
                </li>
                <input type="submit" value="Enviar" />
            </ul>
        </form>
    """         
    )        