# from django import forms

# class EmailForm(forms.Form):
#     recipient = forms.EmailField(label='Recipient Email')
#     subject = forms.CharField(max_length=200, label='Subject')
#     message = forms.CharField(widget=forms.Textarea, label='Message')

from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=200, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
    recipient = forms.EmailField(label='Recipient Email')
    attachments = forms.FileField(
        label='Attachments',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
        required=False,
    )

    
