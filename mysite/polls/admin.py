from django.contrib import admin

# Register your models here.

<<<<<<< HEAD
from .models import Question, Choice

class ChoiceInline(admin.StackedInline):
=======
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
>>>>>>> 462348be47731fbc16353f1fee48bfc510d71c6b
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
<<<<<<< HEAD
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}),
        ]
        
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
=======
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')

    list_display = ('question_text', 'pub_date', 'was_published_recently')

    list_filter = ['pub_date']

    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
>>>>>>> 462348be47731fbc16353f1fee48bfc510d71c6b
