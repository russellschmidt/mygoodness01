from django.shortcuts import get_object_or_404, render

from .models import Org, Detail

def index(request):
    latest_org_list = Org.objects.order_by('-pub_date')[:5]
    context = {'latest_org_list': latest_org_list}
    return render(request, 'orgs/index.html', context)

def stream(request, org_id):
    org = get_object_or_404(Org, pk=org_id)
    return render(request, 'orgs/stream.html', {'org': org})

def detail(request, org_id):
    org = get_object_or_404(Org, pk=org_id)
    return render(request, 'orgs/detail.html', {'org': org})