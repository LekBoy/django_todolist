from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.db import connection
from django.test.utils import CaptureQueriesContext
from django.urls import reverse

from .models import Task
from .views import task_list

User = get_user_model()


class TaskListSecurityTest(TestCase):
    """
    Teste de SEGURANÇA da task_list:
    - Verifica se há SQL Injection no parâmetro 'title'
    """

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username="user1",
            password="senha123",
        )
        # Criar uma task qualquer
        Task.objects.create(
            owner=self.user,
            title="Task segura",
            description="desc",
            is_done=False,
        )

    def test_task_list_sql_injection_in_title(self):
        """
        Envia um 'title' malicioso e verifica se ele aparece
        DIRETAMENTE dentro da query SQL.
        Se aparecer, mostra prints claros e marca como vulnerável.
        """
        print("\n" + "=" * 70)
        print("TESTE DE SEGURANÇA: task_list com parâmetro 'title' malicioso")
        print("=" * 70)

        # Input malicioso típico de SQL Injection
        malicious_input = "' OR '1'='1' --"

        # Simula requisição GET: /tasks/?title=...
        request = self.factory.get(f"/tasks/?title={malicious_input}")
        request.user = self.user

        # Captura as queries executadas pela view
        with CaptureQueriesContext(connection) as queries:
            response = task_list(request)

        executed_sql = queries[-1]["sql"] if queries else ""

        print("\n📝 SQL GERADA PELA VIEW task_list:")
        print(executed_sql)
        print()

        # Se o texto malicioso aparece cru na query, há SQL Injection
        if malicious_input in executed_sql:
            print("❌ RESULTADO: VULNERÁVEL A SQL INJECTION!")
            
            print("⚠️ O texto malicioso do usuário foi colocado direto na SQL.")
            print("⚠️ Isso permite que o atacante altere a lógica da consulta.")
            self.fail("SQL INJECTION DETECTADA na task_list")
        else:
            print("✅ RESULTADO: SEM SQL INJECTION DETECTÁVEL PELO TESTE.")
            print("O parâmetro 'title' não apareceu cru dentro da SQL.")


class DeleteTaskSecurityTest(TestCase):
    """
    Teste de SEGURANÇA do delete_task:
    - Garante que um usuário NÃO consegue deletar task de outro.
    """

    def setUp(self):
        # Dono legítimo da task
        self.owner = User.objects.create_user(
            username="owner",
            password="senha123",
        )
        # Usuário intruso
        self.intruder = User.objects.create_user(
            username="intruso",
            password="senha123",
        )
        # Task pertence ao owner
        self.task = Task.objects.create(
            owner=self.owner,
            title="Task do dono",
            description="",
            is_done=False,
        )

    def test_usuario_intruso_nao_deleta_task_de_outro(self):
        """
        Faz login como 'intruso' e tenta deletar a task do 'owner'.
        Se a task for apagada, o teste denuncia a FALHA DE SEGURANÇA.
        """
        print("\n" + "=" * 70)
        print("\n")
        print("TESTE DE SEGURANÇA: delete_task com usuário intruso")
        print("=" * 70)

        # Login como intruso
        logged = self.client.login(username="intruso", password="senha123")
        print(f"Login como 'intruso' bem-sucedido? {logged}")
        print("\n")

        url = reverse("delete_task", args=[self.task.id])

        print(f"ID da task alvo: {self.task.id}")
        print("\n")
        print(f"Dono real da task: {self.task.owner.username}")
        print("\n")
        print("Usuário logado tentando deletar: intruso")
        print("\n")

        # Simula envio de POST para deletar
        response = self.client.post(url)

        # Verifica se a task ainda existe
        ainda_existe = Task.objects.filter(id=self.task.id).exists()

        print("Status HTTP da resposta:", response.status_code)
        print("\n")
        print("A task ainda existe no banco após tentativa de delete?", ainda_existe)
        print("\n")

        if not ainda_existe:
            print("❌ RESULTADO: FALHA DE SEGURANÇA!")
            print("\n")
            print("⚠️ O usuário 'intruso' conseguiu deletar uma task que não é dele.")
            print("\n")
            self.fail("Usuário não dono conseguiu deletar a task.")
        else:
            print("✅ RESULTADO: COMPORTAMENTO SEGURO.")
            print("\n")
            print("O usuário 'intruso' NÃO conseguiu deletar a task do outro usuário.")