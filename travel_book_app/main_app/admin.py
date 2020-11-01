from django.contrib import admin

# Register your models here.
from .models import Travel, Step, Stopover

admin.site.register(Travel)
admin.site.register(Step)
admin.site.register(Stopover)