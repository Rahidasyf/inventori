from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Rahida Syafa Nurdya',
        'kelas': 'PBP B',
        'menu': 'Kue Jongkong',
        'amount': '10',
        'description': 'Kue basah tradisional nan lembut, ringan disantap, lumer dimulut dan pastinya legit',
        'price': 'Rp25.000',
        'category': 'Kue Basah',
    }

    return render(request, "main.html", context)