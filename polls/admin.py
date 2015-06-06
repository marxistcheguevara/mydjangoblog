from polls.models import Poll, Choice
from django.contrib import admin
from django.utils import timezone
import datetime
class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	
	fieldsets = [
	(None, {'fields': ['question']}),
	('Date Information', {'fields': ['pub_date'], 'classes':['collapse']})
	
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'	
	
admin.site.register(Poll, PollAdmin)

