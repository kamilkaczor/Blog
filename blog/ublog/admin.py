from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import BlogEntryModel


admin.site.register(BlogEntryModel)
class UserAdmin(admin.ModelAdmin):

    model = User
    fields = ["username"]

#
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)

