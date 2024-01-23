from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Article, ArticleImage, Course, Specification, Topic

admin.site.register(ArticleImage)

@admin.register(Specification)
class SpecificationAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name__startswith']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'topic_id', 'creator_id', 'name', 'content', 'is_completed', 'get_article_image_id']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'specification']

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'course_link']

    def course_link(self, obj):
        link = reverse('admin:studying_topic_change', args=[obj.course_id.id])
        return format_html('<a href="{}">{}</a>', link, obj.course_id)

