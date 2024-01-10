from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import *

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#     verbose_name_plural = 'profiles'

# class UserAdmin(UserAdmin):
#     inlines = (ProfileInline, )

#     actions = ['delete_users']

#     def delete_users(self, request, queryset):
#         for user in queryset:
#             user.delete()
#         self.message_user(request, "Users deleted successfully.")

admin.site.unregister(User)
admin.site.register(cars)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Customer)
