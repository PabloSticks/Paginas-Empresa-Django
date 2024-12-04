from django.shortcuts import render


def inicio(request):
    return render(request, 'empresaiei/inicio.html')

def nuestra(request):
    return render(request, 'empresaiei/nuestra.html')

def contacto(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        
        file_path = 'data/pablo_bizama.txt'
        
        with open(file_path, 'a') as file:
            file.write(f'Nombre: {name}\n')
            file.write(f'Correo Electrónico: {email}\n')
            file.write(f'telefono: {telefono}\n\n')
        
    
    return render(request, 'empresaiei/contacto.html')