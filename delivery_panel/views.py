from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def list_delivery(request):
    return render(request, 'delivery_panel/delivery_panel.html')
