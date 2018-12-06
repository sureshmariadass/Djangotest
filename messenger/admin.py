from django.contrib import admin

from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name','email', 'sent_date', )
    list_filter = ('name',)
admin.site.register(Contact,ContactAdmin)

# Register your models here.
