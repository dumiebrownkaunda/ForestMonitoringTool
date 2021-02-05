from django.shortcuts import render


def licences(request):
     args = {'licence': request.licence}
     return render(request, 'Licences/licences.html', args)

