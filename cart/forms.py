from django import forms
from cart.models import Cart


class CartAddContentForm(forms.Form):
    #CONTENT_QUANTITY_CHOICE = [(i, str(i)) for i in range(1, 21)]
    # quantity = forms.TypedChoiceField(
    #     label='수량',
    #     choices=CONTENT_QUANTITY_CHOICE,
    #     coerce=int,
    #     widget=forms.Select(attrs={'class': 'btn-group',
    #                                'placeholder': '.col-sm-1'}),
    # )
    quantity = forms.IntegerField(
        label='수량',
        widget=forms.NumberInput(attrs={
            'id':'quantity',
            'name':'quantity',
            'value':'1',
            'min': '1',
            'max': '100'}),
    )

    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)

    def get_stock(self):
        print("CardAddContentForm : ", self)
        return "CardAddContentForm : " + str(self)

class CartAddContentUserForm(forms.Form):
    class Meta:
        model = Cart
        fields = [
                    # 'user',
                    # 'content',
                    # 'cost',
                    'quantity',
                    # 'created_at',
                    # 'updated_at',
                  ]

    quantity = forms.IntegerField(
        label='수량',
        widget=forms.NumberInput(attrs={
            'name': 'quantity',
            'value': '1',
            'min': '1',
            'max': '100',}))