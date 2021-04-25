from django import forms

from blog.models import Post


class PostForm(forms.ModelForm):
    # デフォルトでidが付与、id=Integer, primary_key, autoincrement
    class Meta:
        model = Post
        # fields = ('title', 'slug', 'author', 'body', 'publish', 'created', 'updated', 'status')
        fields = '__all__'

        title = forms.CharField(label='タイトル', max_length=128)
        slug = forms.SlugField(label='スラッグ', max_length=128)
        author = forms.CharField(label='Author', max_length=128)
        body = forms.CharField(label='Body', max_length=128)
        status = forms.ChoiceField(
            label='ステータス',
            choices=(
                ('draft', 'Draft'),
                ('published', 'Published'),
            ),
            widget=forms.widgets.Select)

        title.widget.attrs.update({'class': 'form-control'})
        slug.widget.attrs.update({'class': 'form-control'})
        body.widget.attrs.update({'class': 'form-control'})
