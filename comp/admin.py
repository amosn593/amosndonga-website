from django.contrib import admin
from .models import Messages

# Register your models here.


class MessagesAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'message', 'date_sent')
    search_fields = ['full_name', 'phone', 'email']


admin.site.register(Messages, MessagesAdmin)
