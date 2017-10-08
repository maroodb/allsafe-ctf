from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from library.models import Document


@login_required
def document_details(request, doc_id):
    response = dict()
    try:

        document = Document.objects.get(pk=doc_id)
        response["success"] = True
        response["title"] = document.title
        response["uploader"] = document.uploader.user.username
        response["description"] = document.description
        response["date"] = document.upload_date.strftime("%d %B %Y %H:%M:%S")
        response["url"] = document.document_file.url
        response["cover_pic"] = document.cover_pic.url

    except Document.DoesNotExist:
        response["success"] = False

    return JsonResponse(response)
