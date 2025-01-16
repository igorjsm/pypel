from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from cadastros.models import Departamento, Perfil


class Command(BaseCommand):
    help = "Inicializa o sistema com os dados pardão"

    def handle(self, *args, **kwargs):
        # Cria um departamento geral
        departamento, created = Departamento.objects.get_or_create(
            nome="Geral", sigla="GERAL"
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Departametno criado: {departamento.nome}")
            )

        # Cria os perfis de usuário
        perfil_administrador, created = Perfil.objects.get_or_create(
            id=1, nome="Administrador"
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Perfil criado: {perfil_administrador.nome}")
            )

        # Cria os perfis de estoquista
        perfil_estoquista, created = Perfil.objects.get_or_create(
            id=2, nome="Estoquista"
        )
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Perfil criado: {perfil_estoquista.nome}")
            )

        # Cria os perfis de vendedor
        perfil_vendedor, created = Perfil.objects.get_or_create(id=3, nome="Vendedor")
        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Perfil criado: {perfil_vendedor.nome}")
            )

        # Cria o usuário administrador principal do sistema
        User = get_user_model()
        if not User.objects.filter(email="adm@gmail.com").exists():
            usuario = User(
                email="adm@gmail.com",
                nome="Administrador",
                is_admin=True,
                departamento=departamento,
            )
            usuario.set_password("123456")
            usuario.save()

            usuario.perfis.add(perfil_administrador)
            usuario.save()

            self.stdout.write(self.style.SUCCESS("Usuário administrador criado"))
        else:
            self.stdout.write(self.style.WARNING("Usuário admnistrador já existe"))
