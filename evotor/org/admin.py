from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdminBase
from org.models import (
    Organization,
    User,
)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(User)
class UserAdmin(UserAdminBase):
    list_display = UserAdminBase.list_display + ("organization", "role")

