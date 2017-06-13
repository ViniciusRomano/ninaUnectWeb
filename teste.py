import django, os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nina.settings")
django.setup()

from hello.models import Funcionario

try:
    Funcionario.objects.get(ra=1430581).marcar_saida()
except Funcionario.DoesNotExist:
    print ("Funcionario nao encontrado")
