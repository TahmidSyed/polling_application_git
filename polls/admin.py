from django.contrib import admin

# Register your models here.
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question_text'],
        })
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    #list_filter = ['pub_date']
    search_fields = ['question']



admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
