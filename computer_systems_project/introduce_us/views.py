from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Member

def member_list(request):
    members = Member.objects.all()
    return render(request, 'introduce_us/member_list.html', {'members': members})
