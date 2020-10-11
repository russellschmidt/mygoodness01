from django.contrib import admin

# Register your models here.
from .models import Org, Detail

class DetailInline(admin.StackedInline):
    model = Detail


class OrgAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['organization_text']}),
        ('Category',         {'fields': ['category_text']}),
        ('Stream Info', {'fields': ['title_text', 'subtitle_text', 'button_label', 'background_image']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [DetailInline]

admin.site.register(Org, OrgAdmin)