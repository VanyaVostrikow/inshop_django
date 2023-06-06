from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField()

class CouponSearchForm(forms.Form):
    login = forms.CharField(max_length=129)