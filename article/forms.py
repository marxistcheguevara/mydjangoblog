from django import forms
from models import Article,  Comment, Category, Author

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ('title',  'body', 'thumbnail', 'pub_date')#, 'author', 'category')


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'body')


#class CategoryForm(forms.ModelForm):
    
 #   class Meta:
  #      model = Category
   #     fields = ('name')

