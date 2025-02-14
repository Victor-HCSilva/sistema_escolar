from django.test import TestCase, Client
from django.urls import reverse
from .models import Aluno
from .forms import AlunoForm
from django.contrib.auth.hashers import check_password

class AlunoViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index') # Correção: "home" -> "index"
        self.list_url = reverse('list')
        self.cadastro_url = reverse('cadastro')
        self.teste_url = reverse('teste')

        # Cria um aluno para usar nos testes de edição e deleção
        self.aluno = Aluno.objects.create(nome="Teste Aluno", senha="senha123", telefone="123456789", nota1=7.0, nota2=7.0, nota3=7.0, nota4=7.0, rec=0.0, observacao="Observação inicial")
        self.edit_url = reverse('edit', args=[self.aluno.id])
        self.delete_url = reverse('delete', args=[self.aluno.id])

    def test_index_view(self): # Correção: "home_view" -> "index_view"
        response = self.client.get(self.index_url) # Correção: "home_url" -> "index_url"
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_cadastro_view_get(self):
        response = self.client.get(self.cadastro_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')
        self.assertIsInstance(response.context['form'], AlunoForm)

    def test_cadastro_view_post_valid(self):
        data = {
            'nome': 'Novo Aluno',
            'senha': 'nova_senha',
            'telefone': '999999999',
            'nota1': 8.0,
            'nota2': 7.5,
            'nota3': 6.0,
            'nota4': 9.0,
            'rec': 7.0,
            'observacao': 'Observações do novo aluno'
        }
        response = self.client.post(self.cadastro_url, data)
        self.assertEqual(response.status_code, 302)  # Redirecionamento
        self.assertRedirects(response, self.list_url)
        self.assertEqual(Aluno.objects.count(), 2) # Contando com o aluno do setUp
        novo_aluno = Aluno.objects.get(nome='Novo Aluno')
        self.assertTrue(check_password('nova_senha', novo_aluno.senha))  # Verificando a senha hasheada
        self.assertEqual(novo_aluno.telefone, '999999999')
        self.assertEqual(novo_aluno.nota1, 8.0)
        self.assertEqual(novo_aluno.nota2, 7.5)
        self.assertEqual(novo_aluno.nota3, 6.0)
        self.assertEqual(novo_aluno.nota4, 9.0)
        self.assertEqual(novo_aluno.rec, 7.0)
        self.assertEqual(novo_aluno.observacao, 'Observações do novo aluno')

    def test_cadastro_view_post_invalid(self):
        data = {
            'nome': '',
            'senha': '',
            'telefone': '',
            'nota1': 'abc',  # Inválido
            'nota2': '',
            'nota3': '',
            'nota4': '',
            'rec': '',
            'observacao': ''
        }
        response = self.client.post(self.cadastro_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cadastro.html')
        self.assertIsInstance(response.context['form'], AlunoForm)
        self.assertTrue(response.context['form'].errors)
        self.assertIn('nome', response.context['form'].errors)
        self.assertIn('senha', response.context['form'].errors)
        self.assertIn('nota1', response.context['form'].errors)  # Verificando se o erro de nota1 está presente

    def test_list_view(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'list.html')
        self.assertEqual(len(response.context['alunos']), 1) # Contando o aluno do setUp
        self.assertEqual(response.context['quantidade'], 1) # Contando o aluno do setUp

    def test_edit_view_get(self):
        response = self.client.get(self.edit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')
        self.assertIsInstance(response.context['form'], AlunoForm)
        self.assertEqual(response.context['aluno'], self.aluno)

    def test_edit_view_post_valid(self):
        data = {
            'nome': 'Aluno Editado',
            'senha': 'senha_editada',
            'telefone': '111111111',
            'nota1': 9.0,
            'nota2': 8.5,
            'nota3': 7.0,
            'nota4': 10.0,
            'rec': 8.0,
            'observacao': 'Observações editadas do aluno'
        }
        response = self.client.post(self.edit_url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)
        self.aluno.refresh_from_db()
        self.assertEqual(self.aluno.nome, 'Aluno Editado')
        self.assertTrue(check_password('senha_editada', self.aluno.senha))
        self.assertEqual(self.aluno.telefone, '111111111')
        self.assertEqual(self.aluno.nota1, 9.0)
        self.assertEqual(self.aluno.nota2, 8.5)
        self.assertEqual(self.aluno.nota3, 7.0)
        self.assertEqual(self.aluno.nota4, 10.0)
        self.assertEqual(self.aluno.rec, 8.0)
        self.assertEqual(self.aluno.observacao, 'Observações editadas do aluno')

    def test_edit_view_post_invalid(self):
        data = {
            'nome': '',
            'senha': '',
            'telefone': '',
            'nota1': 'abc',
            'nota2': '',
            'nota3': '',
            'nota4': '',
            'rec': '',
            'observacao': ''
        }
        response = self.client.post(self.edit_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit.html')
        self.assertIsInstance(response.context['form'], AlunoForm)
        self.assertTrue(response.context['form'].errors)
        self.assertIn('nome', response.context['form'].errors)
        self.assertIn('senha', response.context['form'].errors)
        self.assertIn('nota1', response.context['form'].errors)


    def test_delete_view_get(self):
        response = self.client.get(self.delete_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')
        self.assertEqual(response.context['aluno'], self.aluno)

    def test_delete_view_post(self):
        response = self.client.post(self.delete_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.list_url)
        self.assertEqual(Aluno.objects.count(), 0)

    def test_teste_view(self):
        response = self.client.get(self.teste_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'teste.html')