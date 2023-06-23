from django import forms

from products.models import Category, Product


class ProductCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all()
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'category',
            'description',
            'price',
            'image',
            'is_available'
        ]


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
            'image',
        ]
