from django import forms


# your_name = forms.CharField(label='Your name', max_length=100)
class TaskForm(forms.Form):
    # owner = forms.EmailField(label='Your email', max_length=50)
    title = forms.CharField(label='Task title', max_length=50)
    description = forms.CharField(label='Description', max_length=100)
    collaborator1 = forms.CharField(label='Collaborator 1', required=False)
    collaborator2 = forms.CharField(label='Collaborator 2', required=False)
    collaborator3 = forms.CharField(label='Collaborator 3', required=False)
    


# owner = models.ForeignKey(User, related_name="owned_tasks")
#     title = models.CharField(max_length=500)
#     description = models.CharField(max_length=5000)
#     collaborators = models.ManyToManyField(User, related_name="tasks")