from django.db import models
from django.forms import ModelForm
from django.forms import DateInput, Textarea


class complaint(models.Model):
    Complain_id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=30, blank=True)
    Assigned_Date = models.DateField()
    Completed_Date = models.DateField(null=True, blank=True)
    Description = models.TextField(blank=True)
    st = (('Pending','Pending'), ('Working','Working'), ('Done','Done'))
    Status = models.CharField(default="Pending", max_length=10, choices=st)

    class meta:
        managed = True

    def __str__(self):
        return self.Name

class ComplaintForm(ModelForm):
    class Meta:
        model = complaint
        fields = ('Complain_id', 'Name', 'Assigned_Date', 'Completed_Date', 'Description', 'Status')
        widgets = {
            'Assigned_Date':DateInput(attrs={'type':'date'}),
            'Completed_Date':DateInput(attrs={'type':'date'}),
            'Description': Textarea(attrs={'rows':3, 'cols':30}),
        }
