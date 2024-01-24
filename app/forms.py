from django import forms



g=[['MALE','MALE'],['FEMLAE','FEMALE']]
c=[['PYTHON','PYTHON'],['DJANGO','DJANGO'],['SQL','SQL']]
class nameform(forms.Form):
    sname=forms.CharField()
    sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea (attrs={'col':5,'row':3}))
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c)

