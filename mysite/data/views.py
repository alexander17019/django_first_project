from django.http import JsonResponse

# Create your views here.

def index(request):
    data = {
    "Name" : "Oluwafemi Adenuga",

    "Track" : "Backend(Python)",

    "Message" : "Hi, mentor, you're doing a great job"
}

    return JsonResponse(data)

