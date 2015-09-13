from polls.models import Poll, Choice
from django.contrib import admin


class ChoiceInline(admin.TabularInline):
#class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
#    fields = ('pub_date', 'question')
    fieldsets = [
        (None, {'fields': ['question']}),
        ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ('TO BE CONTINUE', {'fields': []}),
    ]

    list_display = ['question', 'pub_date', 'was_published_recently']

    inlines = [ChoiceInline]

    list_filter = ['pub_date']

    search_fields = ['question']

    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
