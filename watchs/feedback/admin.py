from django.contrib import admin
from .models import Feedback

# Register your models here.
class FeedbackAdmin(admin.ModelAdmin):
    list_display=("name","email","subject","message")

admin.site.register(Feedback, FeedbackAdmin)



