from django.db import models


class BudgetObject(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    value = models.DecimalField(max_digits=19, decimal_places=4, null=False) # TODO use django-money

    class Meta:
        abstract = True
    
    # choice field classes
    
    def __str__(self):
       return self.name
    
    # def save(self):
    #     pass

    # def get_absolute_url(self):
    #     pass

    # custom methods


class Budget(BudgetObject):
   pass


class BudgetGroup(BudgetObject):
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)


class BudgetItem(BudgetObject):
    budget_group = models.ForeignKey(BudgetGroup,  on_delete=models.CASCADE)
    category = models.CharField(max_length=200, blank=False, null=False)