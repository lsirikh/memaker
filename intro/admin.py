from django.contrib import admin
from .models import Intro, EduHistory


# Register your models here.
class EduHistoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content',
        'period_from',
        'period_to',
    )



admin.site.register(Intro)
admin.site.register(EduHistory, EduHistoryAdmin)