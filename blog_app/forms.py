from django import forms
from blog_app.models import Comment, Post, Profile

class ProfileForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Repeat Password')
    class Meta():
        model = Profile
        fields = ['first_name', 'last_name', 'username', 'email', 'linkedin', 'instgram', 'github', 'password1', 'password2']

        # This is to connect these widgets to the css styling by using their class names created here
        widgets = {
            **dict.fromkeys(['first_name','last_name','username'], forms.TextInput(attrs={'class':'textinputclass'})), # Assigning one value to multiple dictionary keys
            'profile_pic':forms.ImageField(attrs={'class':'profilepictureinput'}),
            'email':forms.EmailInput(attrs={'class':'emailinputclass'}),
            **dict.fromkeys(['password1', 'password2'], forms.PasswordInput(attrs={'class':'passwordinputclass'})),
            **dict.fromkeys(['linkedin', 'instagram', 'github'], forms.URLInput(attrs={'class':'urlfieldclass'}))
        }

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['author', 'title', 'text', 'image', 'tag']

        widgets = {
            **dict.fromkeys(['title', 'tag'], forms.TextInput(attrs={'class':'textinputclass'})),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'image':forms.FileInput(attrs={'class':'postpictureinput'}),
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ['author', 'text']

        # This is to connect these widget to my css styling by using their class names created here
        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }