from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import User

UserAdmin.list_display = ('phone', 'email', 'first_name', 'last_name', 'is_staff')
UserAdmin.search_fields = ('phone', 'first_name', 'last_name', 'email')
UserAdmin.ordering = ('phone',)
UserAdmin.fieldsets[0][1]['fields'] = ('phone', 'password')
UserAdmin.add_fieldsets[0][1]['fields'] = ('phone', 'password1', 'password2')

admin.site.site_header = settings.SITE_NAME + "Admin"
admin.site.site_title = f"{settings.SITE_NAME} Admin Portal"
admin.site.index_title = f"{settings.SITE_NAME}"

admin.site.register(User, UserAdmin)
