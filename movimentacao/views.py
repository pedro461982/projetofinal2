from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Movimentacao, Produto
from .forms import MovimentacaoForm

class MovimentacaoListView(ListView):
    model = Movimentacao
    template_name = 'movimentacao_list.html'

class MovimentacaoCreateView(CreateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')

class MovimentacaoUpdateView(UpdateView):
    model = Movimentacao
    form_class = MovimentacaoForm
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacao_list')

    def form_valid(self, form):
        movimentacao = form.save(commit=False)
        
        # Lógica para atualizar a quantidade do produto
        if movimentacao.pk:  # Se já existe uma movimentação
            movimentacao_antiga = get_object_or_404(Movimentacao, pk=movimentacao.pk)
            # Restaura a quantidade anterior do produto
            if movimentacao_antiga.tipo == 'E':
                movimentacao_antiga.produto.quantidade -= movimentacao_antiga.quantidade
            else:
                movimentacao_antiga.produto.quantidade += movimentacao_antiga.quantidade
            
            # Atualiza os dados da movimentação
            movimentacao_antiga.produto.save()  # Salva a quantidade antiga
            movimentacao_antiga.quantidade = movimentacao.quantidade
            movimentacao_antiga.tipo = movimentacao.tipo
            movimentacao_antiga.valor_total = movimentacao.produto.preco * movimentacao.quantidade
            movimentacao_antiga.produto.save()  # Salva a quantidade atualizada
            movimentacao_antiga.save()  # Salva a movimentação atualizada
            
        else:
            movimentacao.valor_total = movimentacao.produto.preco * movimentacao.quantidade
            movimentacao.produto.quantidade += movimentacao.quantidade if movimentacao.tipo == 'E' else -movimentacao.quantidade
            movimentacao.produto.save()  # Salva a quantidade do produto
            movimentacao.save()  # Salva a nova movimentação

        return redirect(self.success_url)

class MovimentacaoDeleteView(DeleteView):
    model = Movimentacao
    template_name = 'movimentacao_delete.html'
    success_url = reverse_lazy('movimentacao_list')

    def post(self, request, *args, **kwargs):
        movimentacao = self.get_object()
        
        # Atualiza a quantidade do produto antes de excluir
        if movimentacao.tipo == 'E':
            movimentacao.produto.quantidade -= movimentacao.quantidade
        else:
            movimentacao.produto.quantidade += movimentacao.quantidade
        
        movimentacao.produto.save()  # Salva a quantidade atualizada
        movimentacao.delete()  # Exclui a movimentação
        return redirect(self.success_url)
