from django import forms

Q1= [
    (1, 'Chest'),
    (2, 'Back'),
    (3, 'Shoulders'),
    (4, 'Triceps'),
    ]

Q2= [
    (1, 'Push exercise'),
    (2, 'Pull exercise'),
    (3, 'Legs exercise'),
    (4, 'Stretch'),
    ]

class UserForm(forms.Form):
    
    q1= forms.CharField(label='1. Which muscle group is the least affected by dips?', widget=forms.RadioSelect(choices=Q1))
    q2= forms.CharField(label='2. Incline dumbbell bench press is a:', widget=forms.RadioSelect(choices=Q2))

