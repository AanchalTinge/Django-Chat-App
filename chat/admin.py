from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'message', 'timestamp', 'read')
    search_fields = ('sender__username', 'receiver__username', 'message')
    list_filter = ('timestamp', 'read')