from django import forms


class UserDetailForm(forms.Form):
    full_name = forms.CharField(max_length=200)
    phone_number = forms.CharField(max_length=10)
    district = forms.CharField(max_length=50)
    sector = forms.CharField(max_length=50)
    address = forms.CharField(max_length=250)
    payment_method = forms.ChoiceField(
        choices=(
            ("MTN", "MTN"),
            ("Card", "Card"),
            ("Airtel", "Airtel"),
            ("Cash", "Cash"),
        )
    )
    message = forms.CharField(widget=forms.Textarea, required=False)
