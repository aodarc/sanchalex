from django import forms


class CommentForm(forms.Form):
    text = forms.CharField(label="Текст", max_length=250, widget=forms.Textarea)
