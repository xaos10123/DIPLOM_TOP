from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .admin import CustomIndexDashboard
from django.contrib import admin

@staff_member_required
def dashboard(request):
    dashboard = CustomIndexDashboard(request)
    dashboard.init_with_context(request)
    
    context = {
        'dashboard': dashboard,
        'available_apps': admin.site.get_app_list(request),
        'is_popup': False,
        'has_permission': True,
        'site_url': '/',
    }
    
    return render(request, 'dashboards/dasboards.html', context)
