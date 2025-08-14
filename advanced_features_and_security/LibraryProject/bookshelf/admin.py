from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("date_of_birth", "profile_photo")}),
    )


admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Post

# Register the Post model in admin
admin.site.register(Post)

# Automatically create permissions for the Post model
content_type = ContentType.objects.get_for_model(Post)
permissions = [
    Permission.objects.get_or_create(codename="can_view", content_type=content_type),
    Permission.objects.get_or_create(codename="can_create", content_type=content_type),
    Permission.objects.get_or_create(codename="can_edit", content_type=content_type),
    Permission.objects.get_or_create(codename="can_delete", content_type=content_type),
]

# Create groups and assign permissions to them
viewers_group, created = Group.objects.get_or_create(name="Viewers")
editors_group, created = Group.objects.get_or_create(name="Editors")
admins_group, created = Group.objects.get_or_create(name="Admins")

# Assign permissions to groups
viewers_group.permissions.add(permissions[0])  # can_view
editors_group.permissions.add(
    permissions[0], permissions[1], permissions[2]
)  # can_view, can_create, can_edit
admins_group.permissions.add(
    permissions[0], permissions[1], permissions[2], permissions[3]
)  # all permissions
