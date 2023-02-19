from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    # Filtrando objetos por 'pub_date'
    list_filter = ['pub_date']
    # Adicionando barra de pesquisa para 'question_text'
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)