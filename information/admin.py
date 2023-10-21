from django.contrib import admin

from .models import Carousel, AboutUs , Team, Contact, Client

admin.site.register(Carousel)
admin.site.register(AboutUs)
admin.site.register(Team)
admin.site.register(Client)

admin.site.register(Contact)