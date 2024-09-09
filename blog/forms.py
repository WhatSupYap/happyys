from django import forms
from blog.models import Post, Tag, Category

class PostForm(forms.ModelForm):
    tags = forms.CharField(required=False, help_text="Enter tags separated by #")

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags', 'show_yn']

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags:
            tags_list = tags.split('#')
            # 태그가 비어있는지 확인
            tags_list = [tag.strip() for tag in tags_list if tag.strip()]
            if not tags_list:
                raise forms.ValidationError("Tags cannot be empty.")
            return tags_list
        return []