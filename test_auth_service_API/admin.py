from django.contrib import admin
from test_auth_service_API.models import Role, Perm

admin.site.register(Role)
admin.site.register(Perm)