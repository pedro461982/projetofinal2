from django import forms
from produtos.models import Categoria, Produto

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
        labels = {
            'nome': 'Nome da Categoria'
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria', 'quantidade', 'imagem']  # Verifique que os nomes correspondem ao modelo
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço (R$)',
            'categoria': 'Categoria',
            'quantidade': 'Quantidade do Produto',
            'imagem': 'Imagem do Produto',
        }
