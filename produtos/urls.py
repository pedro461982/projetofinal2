from django.urls import path
from produtos.views import (
    CategoriaCreateView, CategoriaDeleteView, CategoriaListView, CategoriaUpdateView, 
    ProdutoCreateView, ProdutoDeleteView, ProdutoListView, ProdutoUpdateView
)

urlpatterns = [
    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/nova', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/excluir', CategoriaDeleteView.as_view(), name='categoria_delete'),

    path('produtos/', ProdutoListView.as_view(), name='produto_list'),
    path('produtos/novo', ProdutoCreateView.as_view(), name='produto_create'),
    path('produtos/<int:pk>/editar', ProdutoUpdateView.as_view(), name='produto_update'),
    path('produtos/<int:pk>/excluir', ProdutoDeleteView.as_view(), name='produto_delete'),
]