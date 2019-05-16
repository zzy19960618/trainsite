from django import forms

class ConfigTrainForm(forms.Form):
    trainNo = forms.CharField(label="列车车次", max_length=10)
    startP = forms.CharField(label="始 发 站", max_length=20)
    endP = forms.CharField(label="终 点 站", max_length=20)
    startT = forms.DateTimeField(label="起始日期时间")
    endT = forms.DateTimeField(label="结束日期时间")
    carriageList = forms.CharField(label='列车编号', widget=forms.Textarea())
