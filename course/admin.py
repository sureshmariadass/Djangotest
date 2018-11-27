from django.contrib import admin
from .models import CourseId, CourseDetails, CourseContent,Question,Progress, Category

# Register your models here.
class CourseIdAdmin(admin.ModelAdmin):
    search_fields = ('courseid', )

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('category', )



class CourseDetailsAdmin(admin.ModelAdmin):


    list_display = ('name', 'courseid', )
    list_filter = ('courseid',)
    search_fields = ('description', 'courseid', )

class CourseContentAdmin(admin.ModelAdmin):


    list_display = ('sub_title', 'courseid', )
    list_filter = ('courseid',)
    search_fields = ('courseid', )

class QuestionAdmin(admin.ModelAdmin):


    list_display = ('question','courseid', )
    list_filter = ('courseid',)
    search_fields = ('question','courseid', )

class ProgressAdmin(admin.ModelAdmin):

    list_display = ('user','cid', )
    list_filter = ('cid',)


admin.site.register(Category,CategoryAdmin)
admin.site.register(Progress, ProgressAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(CourseId, CourseIdAdmin)
admin.site.register(CourseDetails, CourseDetailsAdmin)
admin.site.register(CourseContent, CourseContentAdmin)
