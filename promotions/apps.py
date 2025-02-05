from django.apps import AppConfig
import django

class PromotionsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'promotions'
    verbose_name='Акции'

    def ready(self):
        if not django.apps.apps.ready:
            return
            
        from django_q.tasks import schedule
        from django_q.models import Schedule
        
        try:
            schedule('promotions.tasks.check_expired_promos',
                    schedule_type=Schedule.DAILY,
                    next_run='00:00')
        except Exception:
            pass