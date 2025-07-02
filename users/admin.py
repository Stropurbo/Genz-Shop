from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'profile_image_tag' ,'is_active')
    list_filter = ('is_staff', 'is_active')

    # this is for admin
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ( 'profile_image' ,'first_name', 'last_name', 'address', 'phone_number')}),
        ('permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields':('last_login', 'date_joined')})
    )

    # this is for new user
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'password1', 'password2', 'profile_image' ,'is_staff', 'is_active')
        }),
    )
    
    search_fields = ('email', )
    ordering = ('email',)

    def profile_image_tag(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover;" />', obj.profile_image)
        return "-"
    profile_image_tag.short_description = 'Profile Image'


admin.site.register(User, CustomUserAdmin)
