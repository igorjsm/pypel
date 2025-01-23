from django.urls import path

from . import views

app_name = "cadastros"

urlpatterns = [
    # CADASTRO DE DEPARTAMENTO
    path("departamentos/", views.departamentos, name="departamentos"),
    # path(
    #     "obter-departamento-por-id/",
    #     views.obter_departamento_por_id,
    #     name="obter-departamento-por-id",
    # ),
    # path(
    #     "excluir-departamento/", views.excluir_departamento, name="excluir-departamento"
    # ),
    # path(
    #     "pesquisar-departamento-por-nome",
    #     views.pesquisar_departamento_por_nome,
    #     name="pesquisar-departamento-por-nome",
    # ),
    # FIM DE CADASTRO DE DEPARTAMENTOS
]
