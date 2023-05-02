from django.contrib import admin
from .models import *

# Register your models here.


admin.site.register(Doctor)
admin.site.register(Notes)
admin.site.register(Patient)
admin.site.register(ForumPost)
admin.site.register(BlogPost)
admin.site.register(JournalPost)
admin.site.register(Comment)