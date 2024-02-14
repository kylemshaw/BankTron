from django.contrib import admin

from .models import Budget, BudgetGroup, BudgetItem

admin.site.register(Budget)
admin.site.register(BudgetGroup)
admin.site.register(BudgetItem)
