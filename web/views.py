import json
from django.http import JsonResponse
from django.shortcuts import render
from web.models import Gallery,Category,Contact,Detail
from django.http.response import HttpResponse


def index(request):
    galleries = Gallery.objects.all()
    categories = Category.objects.all()
    category_name = request.GET.get('category')
    details = Detail.objects.get()

    context = {
        'galleries' : galleries,
        'categories' : categories,
        'category_name' : category_name,
        'details' : details,
    }

    return render(request, "index.html",context = context)


def contact(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    message = request.POST.get("message")

    if not Contact.objects.filter(email=email).exists():

        Contact.objects.create(
            name = name,
            email = email,
            message = message,
        )
        response_data = {
            "status" :"success",
            "message" : "Your message has been successfully sent. We will contact you very soon!",
            "title" : "Thank you for contacting us"
        }
    else:
        response_data = {
            "status" :"warning",
            "message" : "This email address is already being used",
            "title" : "Add another email address that you own"
        }

    return HttpResponse(json.dumps(response_data),content_type="application/javascript")

def category(request):
    category_name =request.GET.get('category')
    if category_name:

        if category_name == "All":

            galleries = Gallery.objects.all().values()
            data = list(galleries)  
            response_data = {
                "title" : "success",
                "data" : data,
            }
        elif Category.objects.filter(name=category_name).exists():
            if Gallery.objects.filter(category__name=category_name).exists():
                galleries = Gallery.objects.filter(category__name=category_name).values()
                data = list(galleries)  

                response_data = {
                    "title" : "success",
                    "data" : data,
                }
            else:
                response_data = {
                    "title" : "failed",
                    "message" : "Projects not found",
                }
        else:
            response_data = {
                "title" : "failed",
                "message" : "Category not found",
            }
    else:
        response_data = {
            "title" : "failed",
            "message" : "Category not found",
        }

    return JsonResponse({'response_data': response_data})
