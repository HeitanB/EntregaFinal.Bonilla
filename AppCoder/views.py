from django.shortcuts import render
from django.http import HttpResponse
from AppCoder import admin
from AppCoder.forms import Estudiante,Tutor,UserRegisterForm,Programa,UserEditForm
from AppCoder.models import Estudiante,Avatar,Tutor,Programa

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required



#Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    inlines = ()
    
    
def estudiante(request):
    return render(request,"AppCoder/estudiante.html")

@login_required
def leerEstudiante(request):
    estudiante = Estudiante.objects.all()
    contexto = {"estudiantes":estudiante}
    return render(request,"AppCoder/estudiante.html",contexto)

def formularioestudiante(request):
    if request.method == 'POST':
        miFormulario = Estudiante(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data
		    
            estudiante = Estudiante(nombreEstudiante=informacion['nombreEstudiante'],
            edad=informacion['edad'],programa=informacion['programa'],fecha=informacion['fecha'])
		    
            estudiante.save()

            estudiantes = Estudiante.objects.all()
    
            return render(request,"AppCoder/estudiante.html",{"estudiantes":estudiantes})

    else:
        miFormulario = Estudiante()
    return render(request, "AppCoder/formularioEstudiante.html",{"miFormulario":miFormulario})

def editarEstudiante(request,estudiante_nombre):

    estudiante = Estudiante.objects.get(nombreEstudiante = estudiante_nombre)

    if request.method == 'POST':
        miFormularioEstudiante = Estudiante(request.POST)
        print(miFormularioEstudiante)

        if miFormularioEstudiante.is_valid:
            
            informacion = miFormularioEstudiante.cleaned_data
		    
            estudiante.nombreEstudiante=informacion['nombreEstudiante']
            estudiante.edad=informacion['edad']
            estudiante.programa=informacion['programa']
            estudiante.fecha=informacion['fecha']
		    
            estudiante.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioEstudiante= Estudiante(initial={'nombreestudiante': estudiante.nombreAnimal, 'edad': estudiante.edad , 
        'programa':estudiante.programa ,'fecha':estudiante.fecha }) 
    
    return render(request, "AppCoder/editarEstudiante.html", {"miFormularioEstudiante": miFormularioEstudiante, "estudiante_nombre":estudiante_nombre})
        
def eliminarEstudiante(request,estudiante_nombre):
    estudiante = estudiantes.objects.get(nombreEstudiante=estudiante_nombre)
    estudiante.delete()
    estudiantes = Estudiante.objects.all()
    contexto ={"estudiantes":estudiantes}
    return render(request,"AppCoder/estudiante.html",contexto)

@login_required
def busquedaEstudiante(request):
    return render(request,"AppCoder/busquedaEstudiante.html")
    
@login_required
def buscar(request):
        
    if request.GET["nombreEstudiante"]:
        nombreEstudiante = request.GET['nombreestudiante']
        estudiantes = Estudiante.objects.filter(nombreEstudiante__icontains=nombreEstudiante)
        
        return render(request, "AppCoder/estudiante.html",{"estudiantes":estudiantes})

    else:
        respuesta = "No enviaste nada"
    return render(request,"AppCoder/inicio.html",{"respuesta":respuesta})


#Tutor
def tutor(request):
    return render(request,"AppCoder/tutor.html")

@login_required
def leerTutor(request):
    tutores = Tutor.objects.all()
    contexto = {"tutores":tutores}
    return render(request,"AppCoder/tutor.html",contexto)

def formularioTutor(request):

    if request.method == 'POST':
        miFormularioTutor = Tutor(request.POST)
        print(miFormularioTutor)

        if miFormularioTutor.is_valid:
            
            informacion = miFormularioTutor.cleaned_data
		    
            tutor = Tutor(nombre=informacion['nombre'],
            apellido=informacion['apellido'],telefono=informacion['telefono'])
		    
            tutor.save()

            tutores = Tutor.objects.all()
            
            return render(request,"AppCoder/tutor.html",{"tutores":tutores})

    else:
        miFormularioTutor = Tutor()
    return render(request, "AppCoder/formularioTutor.html",{"miFormularioTutor":miFormularioTutor})

def editarTutor(request,tutor_nombre):

    tutor = Tutor.objects.get(nombre = tutor_nombre)

    if request.method == 'POST':
        miFormularioTutor = Tutor(request.POST)
        print(miFormularioTutor)

        if miFormularioTutor.is_valid:
            
            informacion = miFormularioTutor.cleaned_data
		    
            tutor.nombre=informacion['nombre']
            tutor.apellido=informacion['apellido']
            tutor.telefono=informacion['telefono']
            tutor.programa=informacion['Programa']
		    
            tutor.save()
            
            return render(request, "AppCoder/inicio.html")

    else:
        miFormularioTutor= Tutor(initial={'nombre': tutor.nombre, 'apellido':tutor.apellido, 
            'telefono':tutor.telefono, 'programa' :tutor.programa }) 
    
    return render(request, "AppCoder/editartutor.html", {"miFormularioTutor": miFormularioTutor, "tutor_nombre":tutor_nombre})
        
def eliminarTutor(request,tutor_nombre):
    tutor = Tutor.objects.get(nombre=tutor_nombre)
    tutor.delete()
    tutores = Tutor.objects.all()
    contexto ={"tutores":tutores}
    return render(request,"AppCoder/tutor.html",contexto)

#TutorCVB

# class TutorList(ListView):
#     model= Tutor
#     template_name= "AppCoder/tutor_list.html"


# class TutorDetalle(DetailView): 
#     model=Tutor
#     template_name= "AppCoder/tutor_detalle.html"

# class TutorCreacion(CreateView):
#     model= Tutor
#     succcess_url = "/AppCoder/tutor/list"	
#     fields = ['nombre','apellido','telefono','programa']


# class TutorUpdate(UpdateView):
    
#     model= Tutor
#     succcess_url = "/AppCoder/tutor/list"	
#     fields = ['nombre','apellido','telefono','programa']


# class TutorDelete(DeleteView):  
#     model= tutor
#     succcess_url = "/AppCoder/tutor/list"	

#Programa

def programa(request):
    return render(request,"AppCoder/programa.html")

@login_required
def leerPrograma(request):
    programas = programas.objects.all()
    contexto = {"programas":programas}
    return render(request,"AppCoder/prohrama.html",contexto)

def formularioPrograma(request):

    if request.method == 'POST':
        miFormularioPrograma = Programa(request.POST)
        print(miFormularioPrograma)

        if miFormularioPrograma.is_valid:
            
            informacion = miFormularioPrograma.cleaned_data
		    
            programa = Programa(programa=informacion['Programa'],
            id=informacion['id'],programa=informacion['programa'], codigo=informacion['codigo'])
		    
            programa.save()

            programas = Programa.objects.all()
            
            contexto = {"programas":programas}
            return render(request,"AppCoder/programa.html",contexto)

    else:
        miFormularioPrograma = Programa()
    return render(request, "AppCoder/formularioPrograma.html",{"miFormularioPrograma":miFormularioPrograma})




#-----------------------------------------Loguin/Register-------------------------------------------------------
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario,password = contra)

            if user is not None:
                login(request,user)

                return render(request,"AppCoder/inicio.html",{"mensaje":f"Bienvenido {usuario}"})
            else:
                
                return render(request,"AppCoder/inicio.html",{"mensaje":"Error,datos incorrectos"})

        else:
            
                return render(request,"AppCoder/inicio.html",{"mensaje":"Error,formulario erroneo"})

    form = AuthenticationForm()

    return render(request,"AppCoder/login.html",{'form':form})


def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppCoder/inicio.html",{"mensaje":"Usuario Creado :)"})
    else:
        form = UserRegisterForm()
        #form = UserCreationForm()
    return render(request,"AppCoder/registro.html",{"form":form})


def inicio(request):
    return render(request,"AppCoder/inicio.html")

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password1']            
            usuario.save()
            

            return render(request, "AppCoder/inicio.html")
    else:

        miFormulario = UserEditForm(initial={'email':usuario.email})
    return render(request, "AppCoder/editarPerfil.html",{"miFormulario": miFormulario, "usuario":usuario})



#-----------------------------------------Avatar-------------------------------------------------------
@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)

    return render(request,"AppCoder/inicio.html", {"url":avatares[0].imagen.url})
