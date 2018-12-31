from django.contrib import admin
from boards.models import Board, Topic, Post

# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
    )
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'user',
        'board',
        'created_at',
        'updated_at',
        'views',
    )
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'topic',
        'created_at',
        'updated_at',
        'user',
    )

admin.site.register(Board, BoardAdmin)

admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)