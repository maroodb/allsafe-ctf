from django.http import JsonResponse
from django.shortcuts import render

from magazine.forms import NewsLettreForm
from magazine.models import NewsLettre


def home(request):
    newslettre_form = NewsLettreForm()
    return render(request, "magazine/comingsoon.html", locals())


def newslettre(request):

    response = {
        "success": False,
        "error": "",
        "is_registered": False
    }

    name = request.POST.get("name")
    email = request.POST.get("email")

    response["is_registered"] = NewsLettre.objects.filter(email__iexact=email).exists()

    if not response["is_registered"]:
        news_lettre = NewsLettre()
        news_lettre.name = name
        news_lettre.email = email
        news_lettre.save()
        response["success"] = True

    else:
        response["error"] = "This email is already registered."
        response["success"] = False

    return JsonResponse(response)
