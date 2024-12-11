from django.contrib import admin
from .models import Categoria, Produto, Entrada, Saida, LogAtividade

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'produtos_count')
    search_fields = ('nome',)
    prepopulated_fields = {'slug': ('nome',)}

    def produtos_count(self, obj):
        return obj.produto_set.count()
    produtos_count.short_description = 'Quantidade de Produtos'

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'quantidade', 'esta_em_baixo_estoque')
    list_filter = ('categoria', 'data_cadastro')
    search_fields = ('nome', 'codigo_barras')
    date_hierarchy = 'data_cadastro'

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'data', 'usuario')
    list_filter = ('data', 'usuario')
    date_hierarchy = 'data'
    search_fields = ('produto__nome', 'usuario__username')

@admin.register(Saida)
class SaidaAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'destino', 'data', 'usuario')
    list_filter = ('data', 'usuario')
    date_hierarchy = 'data'
    search_fields = ('produto__nome', 'destino', 'usuario__username')

@admin.register(LogAtividade)
class LogAtividadeAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'tipo_acao', 'data')
    list_filter = ('tipo_acao', 'data', 'usuario')
    date_hierarchy = 'data'
    search_fields = ('descricao', 'usuario__username')
    readonly_fields = ('usuario', 'tipo_acao', 'descricao', 'data')
