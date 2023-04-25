from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(Doctor)
admin.site.register(Notes)
admin.site.register(Patient)
admin.site.register(Post)
admin.site.register(Comment)