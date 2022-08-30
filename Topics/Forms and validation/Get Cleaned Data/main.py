def get_cleaned_data(raw_data):
    promo_form = PromoCodeForm(raw_data)
    if promo_form.is_valid():
        return promo_form.cleaned_data
    return {}
