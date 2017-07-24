from django.contrib import admin

from members.models import Member, Position, FakeUser

admin.site.register(Member)
admin.site.register(Position)
admin.site.register(FakeUser)
