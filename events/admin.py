from django.contrib import admin

from events.models import Event, Sponsor, Speaker

admin.site.register(Event)
admin.site.register(Speaker)
admin.site.register(Sponsor)
