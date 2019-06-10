from django.contrib import admin
from infos.models import ServiceUsage, PrivacyPolicy

# Register your models here.

class ServiceUsageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at',
        'updated_at',
    )
class PrivacyPolicyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'created_at',
        'updated_at',
    )


admin.site.register(ServiceUsage, ServiceUsageAdmin)
admin.site.register(PrivacyPolicy, PrivacyPolicyAdmin)
