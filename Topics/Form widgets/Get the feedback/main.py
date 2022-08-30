from django import forms

FREQ = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
]


class CommentForm(forms.Form):
    name = forms.CharField(
        label="Name",
    )
    comment = forms.CharField(
        label="Comment",
        widget=forms.Textarea(),
    )
    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput())
    frequency = forms.ChoiceField(
        label="How often should I send notifications?",
        required=False,
        widget=forms.RadioSelect(),
        choices=FREQ,
    )
