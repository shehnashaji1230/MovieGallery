from django import forms

class MovieForm(forms.Form):
    options=(
        ("Drama","Drama"),
        ("Action","Action"),
        ("Fiction","Fiction"),
        ("Comedy","Comedy")
    )
   

    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    genre=forms.ChoiceField(choices=options,widget=forms.Select(attrs={'class':'form-control form-select'}))
    language=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    year=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    run_time=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    director=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data=super().clean()
        year=cleaned_data.get("year")
        
        run_time=cleaned_data.get("run_time")
        if int(year)<1990:
            error_message="year should be greater than 1990"

            self.add_error("year",error_message)
        if run_time not in range(60,360):
            error_message="runtime should be between 60 and 360"

            self.add_error("run_time",error_message)
