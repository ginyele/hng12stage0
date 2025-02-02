from django.shortcuts import render
from django.http import JsonResponse
from django.utils.timezone import now

# Create your views here.

def detailView(request):
    return JsonResponse({
        "email": "inyelegoody@gmail.com",
        "current_datetime" : now().isoformat(),
        "github_url" : "https://github.com/ginyele/hng12stage0.git"
    })