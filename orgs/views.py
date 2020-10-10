from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the orgs index.")

def detail(request, org_id):
    return HttpResponse("You're looking at org %s." % org_id)