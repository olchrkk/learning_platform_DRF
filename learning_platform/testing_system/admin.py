from django.contrib import admin

from .models import (
    AnswerOption,
    Attempt,
    CompletedArticle,
    CompletedTest,
    Questions,
    Test,
)

admin.site.register(Test)
admin.site.register(Questions)
admin.site.register(CompletedTest)
admin.site.register(CompletedArticle)
admin.site.register(Attempt)

@admin.register(AnswerOption)
class AnswerOptionAdmin(admin.ModelAdmin):
    list_display = ['question_id', 'answer']
    list_filter = ('is_correct',)
