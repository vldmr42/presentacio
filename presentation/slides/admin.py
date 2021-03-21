from django.contrib import admin
from .models import Presentations, Slides


@admin.register(Presentations, Slides)
class AuthorAdmin(admin.ModelAdmin):
    pass
