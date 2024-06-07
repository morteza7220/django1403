
from django.http import JsonResponse
py
def go(request):
    return JsonResponse({2:4})


from django.urls import path,include

urlpatterns = [
    path("path1",go)
]

