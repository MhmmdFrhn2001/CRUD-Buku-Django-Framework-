from django import forms

class BookForm(forms.Form):

    title = forms.CharField(label = "Title", widget = forms.TextInput( attrs={'class': 'form-control'} ))
    author = forms.CharField(label = "Author", widget = forms.TextInput( attrs={'class': 'form-control'} ))
    description = forms.CharField(label = "Description", widget = forms.Textarea( attrs={'class': 'form-control', 'rows': '5'} ))
    year = forms.CharField(label = "Year", widget = forms.NumberInput( attrs={'class': 'form-control'} ))

    #validation
    def clean(self):
        super(BookForm, self).clean()

        title = self.cleaned_data.get('title')

        if len(title)<5:
            self.add_error('title','Can not save title less than 5 characters long')
            self.fields['title'].widget.attrs.update({'class': 'form-control  is-invalid'})

        return self.cleaned_data