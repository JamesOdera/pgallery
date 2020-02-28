from django.contrib import admin
from .models import Editor,Article,tags,Location,Category,Image
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Article,ArticleAdmin)
admin.site.register(tags)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)
