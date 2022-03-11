from django import forms
from blog_app.models import Comment, Post, RegisterProfile

class RegisterForm(forms.ModelForm):
    class Meta():
        model = RegisterProfile
        fields = '__all__'

        # This is to connect these widget to my css styling by using their class names created here
        widgets = {
            **dict.fromkeys(['first_name','last_name','username','email','password','password'], forms.TextInput(attrs={'class':'textinputclass'})), # Assigning of one value to multiple dictionary keys
            'profile_pic':forms.ImageField(attrs={'class':'profilepictureinput'}),
        }

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['author', 'title', 'text', 'image']

        # This is to connect these widget to my css styling by using their class names created here
        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
            'image':forms.ImageField(attrs={'class':'postpictureinput'}),
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