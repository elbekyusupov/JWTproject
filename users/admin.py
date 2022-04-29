from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
# from django.utils.translation import ugettext_lazy as _
from .models import User, Condition
# from related_admin import RelatedFieldAdmin


class UserAdmin(DjangoUserAdmin, admin.ModelAdmin):
    fieldsets = (
        ('Main', {'fields': ('phone', 'password', 'code', 'verified')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'middle_name',
                                         'email', 'address', 'avatar', 'firebase_token')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2', 'verified'),
        }),
    )
    list_display = ('phone', 'get_fullname', 'is_staff', 'date_joined', 'verified', 'created_at')
    search_fields = ('email', 'first_name', 'last_name', 'phone',)
    ordering = ('id',)
    list_filter = (
        'verified', 'is_active', 'is_staff', 'is_superuser',
    )

    @staticmethod
    def get_fullname(obj):
        return "{} {}".format(obj.first_name, obj.last_name)


admin.site.register(User, UserAdmin)
admin.site.register(Condition)