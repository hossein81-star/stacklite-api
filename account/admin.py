from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model

from .models.profile import Profile
from .models.skill import Skill, ProfileSkill

User = get_user_model()


# -------------------------
# Inline for Profile Skills
# -------------------------

class ProfileSkillInline(admin.TabularInline):
    model = ProfileSkill
    extra = 1
    autocomplete_fields = ["skill"]
    fields = ("skill", "level")


# -------------------------
# User Admin
# -------------------------

@admin.register(User)
class UserAdmin(BaseUserAdmin):

    list_display = ["email", "is_staff", "is_active", "date_joined", "is_verified"]
    list_filter = ["is_staff", "is_active", "date_joined"]

    fieldsets = (
        ("Authenticate", {"fields": ("email", "password")}),

        ("Permissions", {
            "fields": ("is_staff", "is_active", "is_superuser", "is_verified")
        }),

        ("Important dates", {
            "fields": ("last_login", "date_joined")
        }),
    )

    add_fieldsets = (
        ("Personal info", {
            "fields": ("email", "password1", "password2")
        }),

        ("Permissions", {
            "fields": ("is_staff", "is_active", "is_superuser", "is_verified")
        }),
    )

    readonly_fields = ("last_login", "date_joined")
    ordering = ("email",)


# -------------------------
# Profile Admin
# -------------------------

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ["username"]
    inlines = [ProfileSkillInline]

    fieldsets = (
        ("User Info", {"fields": ("username",)}),

        ("Profile Info", {
            "fields": ("bio", "expertise")
        }),
    )


# -------------------------
# Skill Admin
# -------------------------

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = ["title"]
    search_fields = ["title"]
