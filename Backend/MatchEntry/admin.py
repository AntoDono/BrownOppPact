from django.contrib import admin
from MatchEntry.models import MatchEntry
# Register your models here.

@admin.register(MatchEntry)
class MatchEntry(admin.ModelAdmin):
    list_display = ('email', 'firstname', 'lastname')
    list_filter = ('email', 'firstname', 'lastname')
    search_fields = ('email', 'firstname', 'lastname')