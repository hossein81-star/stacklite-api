from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models.skill import Skill


from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ("title", "level")

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model=User

    inlines = [SkillInline]
    list_display = ["email", "is_staff","is_active","date_joined","is_verified"]
    list_filter = ["is_staff","is_active","date_joined"]
    fieldsets = (
        ("Authenticate", {"fields": ("email", "password")}),

        ("Permissions", {"fields":("is_staff","is_active","is_superuser","is_verified")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),


    )
    add_fieldsets = (
        ("Personal info", {"fields": ("email","password1","password2",)}),
        ("Permissions", {"fields": ("is_staff","is_active","is_superuser","is_verified")}),
    )
    readonly_fields = ("last_login", "date_joined")
    ordering = ("email",)