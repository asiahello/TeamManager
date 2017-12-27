from django.contrib import admin

from trainings.models import AgeCategory, Comment, Event, Exercise

# Register your models here.


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'performer')
    list_filter = ('date', 'author', 'performer')
    search_fields = ('title', )
    # prepopulated_fields = {'slug': ('title',)}  # slug -> tiltle 
    # raw_id_fields = ('author',) # id instead of name
    date_hierarchy = 'date'  # if many
    ordering = ['date']


admin.site.register(Event, EventAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
    ordering = ['created']


admin.site.register(Comment, CommentAdmin)

admin.site.register(Exercise)

admin.site.register(AgeCategory)
