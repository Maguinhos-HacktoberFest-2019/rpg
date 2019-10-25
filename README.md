# Random CLI-RPG

Olá. Este é um projeto criado para dar suporte ao Workshop de Git Iniciante promovido pelo Leds Serra, para participar do HacktoberFest 2019 e ensinar o básico de Git para os alunos iniciantes do Ifes - Serra.

## Para os participantes

### Rodando o jogo
Já com o Python 3 instalado, abra a raiz do projeto no terminal e execute o comando:
    
- No Windows: `python src/main.py`    
- No Linux: `python3 src/main.py`

### Contribuindo
- Para adicionar fases ao jogo, crie um novo arquivo python na pasta `src/phases/`, com o nome da sua fase.
- No arquivo criado, crie uma função, também com o nome da fase.

- Cada fase do jogo **deve** retornar `True` ou `False`. O meio da fase é completamente livre, apenas ofereça uma experiência legal ao jogador. =)

- Exemplo de fase:

minhaFase.py
```python
# autor: Seu nome aqui =)

def minhaFase():
    print("Olá! =)")
    return True
#
```

- Depois de criar a fase, vá ao arquivo `src/main.py` e faça o seguinte:
1. No início do arquivo, importe a fase que você criou:
```python
...
from phases.velha import velha
from phases.minhaFase import minhaFase  # <-- aqui
```
2. No Array `g_phases`, adicione a fase que você importou:
```python
g_phases = [start, dilema, velha, hangman, minhafase]
```
- Pronto. Agora é só rodar o jogo. =D