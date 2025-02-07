from django.shortcuts import render

def list_delivery(request):
    return render(request, 'delivery_panel/delivery_panel.html')
