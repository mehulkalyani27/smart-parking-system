from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import pstorey
from .models import pstorey1
from .models import feedback

class pstorey(admin.ModelAdmin):
    pass
    admin.site.register(pstorey)

class pstorey1(admin.ModelAdmin):
    pass
    admin.site.register(pstorey1)

class feedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact')
  
    def has_add_permission(self, request):
        return False

admin.site.register(feedback, feedbackAdmin)