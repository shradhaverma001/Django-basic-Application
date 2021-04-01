from django import forms
from django.core import validators

# 3) # to make your own validations to check forms or form fields write def out of the class
# # for this make changes in class FormName--> name = forms.CharField(validators=[check_for_z])
# def check_for_z(value):
#     if value[0].lower() !='z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter youe Email again: ')
    text = forms.CharField(widget=forms.Textarea)
    # 2) botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # 1) #defining a form validation by checking of a bot 
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOT A BOT")
    #     return botcatcher

    # 2) using django inbuilt form validation
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    # to clean the entire form data
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError("MAKE SURE THAT EMAILS MATCH")
    