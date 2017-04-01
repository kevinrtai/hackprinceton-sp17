from django.contrib import admin

from .models import Login, User, Group, Media, Review, Destination, Trip

# Register your models here.
admin.site.register(Login)
admin.site.register(User)
admin.site.register(Group)
admin.site.register(Media)
admin.site.register(Review)
admin.site.register(Destination)
admin.site.register(Trip)

