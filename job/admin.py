from django.contrib import admin
from .models import Applay, job, Cateogry

class ProductAdmin(admin.ModelAdmin):
    list_display=['owner','title','published_at','cateogry','description','job_type' ]
    list_display_links=['published_at','cateogry']
    list_editable=['owner','title','description','job_type']
    search_fields= ['title']
    
admin.site.register(job,ProductAdmin)
admin.site.register(Cateogry)
admin.site.register(Applay)