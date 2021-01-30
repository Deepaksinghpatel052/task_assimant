from django.contrib import admin
from .models import product,webpage
# Register your models here.

admin.site.register(product)

class webpageAdmin(ImportExportModelAdmin):
    list_display = ('CompanyName','CompanyURL', 'Created_date')

admin.site.register(webpage,webpageAdmin)