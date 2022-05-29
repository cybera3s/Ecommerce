from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User, Setting
from django_json_widget.widgets import JSONEditorWidget
from django.db import models


UserAdmin.list_display = ('phone', 'email', 'first_name', 'last_name', 'is_staff')
UserAdmin.search_fields = ('phone', 'first_name', 'last_name', 'email')
UserAdmin.ordering = ('phone',)
UserAdmin.fieldsets[0][1]['fields'] = ('phone', 'password')
UserAdmin.add_fieldsets[0][1]['fields'] = ('phone', 'password1', 'password2')

admin.site.site_header = settings.SITE_NAME + "Admin"
admin.site.site_title = f"{settings.SITE_NAME} Admin Portal"
admin.site.index_title = f"{settings.SITE_NAME}"

admin.site.register(User, UserAdmin)


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    """
    wide Setting admin model
    overrides default json field with a perfect editor
    """
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }