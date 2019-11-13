from django.contrib import admin

from .models import Constraint, Definition


class DefinitionInline(admin.StackedInline):
    model = Definition
    extra = 1

class ConstraintAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields': ['name']}),
    ]
    inlines = [DefinitionInline]

admin.site.register(Constraint, ConstraintAdmin)