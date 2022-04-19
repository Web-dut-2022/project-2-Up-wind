from django.contrib import admin

from .models import Biding, Comments, Listing

# Register your models here.
admin.site.register(Listing)
admin.site.register(Biding)
admin.site.register(Comments)
