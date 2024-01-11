from django import forms
from django.forms import ModelForm
from .models import RSVP

class RSVPForm(forms.ModelForm):
    attending = forms.BooleanField(
        required=False,
        label='Você vai comparecer?',
        widget=forms.CheckboxInput()
    )
    not_attending = forms.BooleanField(
        required=False,
        label='Você vai comparecer?',
        widget=forms.CheckboxInput()
    )
    name = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'rows': '4', 'cols': '40'}),
        label='Nomes de quem vai'
    )
    dietary_restrictions = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': '4', 'cols': '40'}),
        label='Restrições alimentares'
    )
    observations = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': '4', 'cols': '40'}),
        label='Observações'
    )

    class Meta:
        model = RSVP
        fields = ['attending', 'not_attending', 'name', 'dietary_restrictions', 'observations']

    use_required_attribute = False

class RSVPForm(ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'
        # Customizing the form fields with CSS classes and placeholders
        widgets = {
            'attending': forms.CheckboxInput(attrs={'class': 'checkbox', 'placeholder': 'Sim'}),
            'not_attending': forms.CheckboxInput(attrs={'class': 'checkbox', 'placeholder': 'Sim'}),
            'name': forms.Textarea(attrs={'class': 'linebreakTextArea', 'placeholder': 'Nomes', 'rows': 4}),
            'dietary_restrictions': forms.Textarea(attrs={'class': 'linebreakTextArea', 'placeholder': 'Restrições Alimentares', 'rows': 4}),
            'observations': forms.Textarea(attrs={'class': 'linebreakTextArea', 'placeholder': 'Observações', 'rows': 4}),
        }

        # Labels for each field
        labels = {
            'attending': 'Sim',
            'not_attending' : 'Não',
            'name': 'Nomes',
            'dietary_restrictions': 'Restrições Alimentares',
            'observations': 'Observações',
        }

        # Help texts for fields (if needed)
        help_texts = {
            # You can add help texts here if needed
        }

        # Disable automatic HTML5 validation
        use_required_attribute = False

