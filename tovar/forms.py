from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        label="ФИО",
        widget=forms.TextInput
    )

    phone = forms.IntegerField(
        label="Телфон",
        widget=forms.NumberInput
    )

    email = forms.EmailField(
        widget=forms.EmailInput
    )
    message = forms.CharField(
        label="Сообщение",
        widget=forms.Textarea
    )


