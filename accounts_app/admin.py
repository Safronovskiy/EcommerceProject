from django.contrib import admin
from .models import *


@admin.register(AuthUserModel)
class AuthUserModelAdmin(admin.ModelAdmin):
    pass

@admin.register(AuthUserProfileModel)
class AuthUserProfileModel(admin.ModelAdmin):
    pass

@admin.register(AuthUserContacts)
class AuthUserContacts(admin.ModelAdmin):
    pass
