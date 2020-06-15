from django import forms


CHOICE_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddChoiceForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=CHOICE_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)