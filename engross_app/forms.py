from django import forms

class UserForm(forms.Form):
    name = forms.CharField(required=True,widget= forms.TextInput(attrs={'class':'form-control','Placeholder':'Full Name*'}))
    email = forms.CharField(required=True,widget= forms.TextInput(attrs={'class':'form-control','Placeholder':'Email*'}))
    mobile = forms.IntegerField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'Mobile Number*'}))
    gender = forms.ChoiceField(widget=forms.Select(attrs= {'class':'form-control'}),choices=[('Male','Male'),('Female','Female'),('Other','Other')])
    qualification = forms.ChoiceField(widget=forms.Select(attrs= {'class':'form-control'}),choices=[('BE/BTech','BE/BTech'),('BCA','BCA'),('BCS','BCS'),('BSC','BSC'),('MCA','MCA'),('MBA IT','MBA IT'),('MSC','MSC'),('MCS','MCS')])
    # age = forms.CharField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'Age'}))
    # qualification = forms.CharField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'Highest Qualification'}))
    batch = forms.ChoiceField(widget=forms.Select(attrs= {'class':'form-control'}),choices=[('2023','2023'),('2022','2022'),('2021','2021'),('2020','2020'),('2019','2019'),('2018','2018'),('2017','2017'),('Pursuing ','Pursuing')])
    college = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','Placeholder':'College*'}))
    city = forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','Placeholder':'City*'}))
    # state = forms.CharField(widget= forms.TextInput(attrs= {'class':'form-control','Placeholder':'State'}))
    