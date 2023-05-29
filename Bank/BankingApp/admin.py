from django.contrib import admin
from .models import Branch,District,DistBranch

# Register your models here.
admin.site.register(Branch)
admin.site.register(District)
admin.site.register(DistBranch)
