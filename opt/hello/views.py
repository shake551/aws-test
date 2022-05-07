from django.http import JsonResponse

def index(request):

    res = {
        "message": "hello"
    }

    return JsonResponse(res, status=200)
