from django.shortcuts import render, HttpResponse

# Create your views here.
html_base = """
<h1>Mi Web Personal</h1>
<nav>
        <ul>
            <li><a href="/">Portada</a></li>
            <li><a href="/about-me/">Sobre Mí</a></li>
            <li><a href="/portfolio/">Proyectos</a></li>
            <li><a href="/contacto/">Contacto</a></li>
        </ul>
    </nav>
"""

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')
    

def contacto(request):
    return render(request, 'core/contacto.html')