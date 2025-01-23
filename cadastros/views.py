from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count, ExpressionWrapper, F, OuterRef, Q, Subquery, Sum
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .models import Departamento, Perfil, Usuario


# CADASTRO DE DEPARTAMENTOS
@login_required
def departamentos(request):
    if request.session.get("perfil_atual") not in {"Administrador"}:
        messages.error(request, "Você não é administrador!")
        return redirect("core:main")
    if request.method == "post":
        messages.success(request, "Implementar depois.")
    departamento_lista = (
        Departamento.objects.all().exclude(nome__iexact="Geral").order_by("nome")
    )
    paginator = Paginator(departamento_lista, settings.NUMBER_GRID_PAGES)
    numero_pagina = request.GET.get("page")
    page_obj = paginator.get_page(numero_pagina)
    return render(request, "departamentos.html", {"page_obj": page_obj})
