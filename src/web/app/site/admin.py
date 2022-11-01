from django.contrib import admin
from django.contrib.admin import SimpleListFilter
import site.models as models

# Register your models here.


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    actions = None
    ordering = ['user',]
    list_display = (
        'user',
        'get_user_active',
        'get_user_superuser',
        'get_user_staff',
        'updated_datetime',
        )
    search_fields = ()  # TWO _ django convention for foreign keys
    list_filter = ()
    raw_id_fields = ['user']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['user']
        else:
            return []

    def get_user_staff(self, obj):
        return obj.user.is_staff
    get_user_staff.short_description = "Staff"
    get_user_staff.boolean = True

    def get_user_superuser(self, obj):
        return obj.user.is_superuser
    get_user_superuser.short_description = "Superuser"
    get_user_superuser.boolean = True

    def get_user_active(self, obj):
        return obj.user.is_active
    get_user_active.short_description = "Active"
    get_user_active.boolean = True

    # This will help you to disbale add functionality
    def has_add_permission(self, request):
        return False

    # This will help you to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return True
