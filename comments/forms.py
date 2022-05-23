from django import forms
from .models import Comment


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', ]
        widgets = {
            'body': forms.Textarea(
                attrs={'class': 'size-110 bor8 stext-102 cl2 p-lr-20 p-tb-10', 'placeholder': 'your comment here'}),
        }

    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'size-111 bor8 stext-102 cl2 p-lr-20', 'placeholder': 'your name'}))
    # email = forms.EmailField(required=True, widget=forms.EmailInput(
    #     attrs={'class': 'size-111 bor8 stext-102 cl2 p-lr-20', 'placeholder': 'your email'}))
