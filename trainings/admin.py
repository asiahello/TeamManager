from django.contrib import admin

from trainings.models import AgeCategory, Comment, Event, Exercise

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author')
    list_filter = ('date', 'author', 'performer')
    search_fields = ('title', )
    # prepopulated_fields = {'slug': ('title',)}  # slug -> tiltle 
    # raw_id_fields = ('author',) # id instead of name
    date_hierarchy = 'date'  # if many
    ordering = ['date']


admin.site.register(Event, EventAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'created', 'author',)
    list_filter = ('created',)
    search_fields = ('email', 'body')
    ordering = ['created']


admin.site.register(Comment, CommentAdmin)

admin.site.register(Exercise)

admin.site.register(AgeCategory)
