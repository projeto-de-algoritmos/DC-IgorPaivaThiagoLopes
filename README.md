# Image Manipulator

**Conteúdo da Disciplina**: Greed<br>

## Alunos
| Matrícula | Aluno |
| -- | -- |
| 18/0018728  |  Igor Batista Paiva |
| 18/0028260  |  Thiago Aparecido Lopes Santos |

## Sobre
O Image é um software de manipulação de imagens a partir de multiplicação de matrizes.

No software, existem duas opções de manipulação:
 - Flip:
 Nessa opção, a imagem é espelhada

 - Rotate:
Nessa opção, a imagem é rotacionada 90º à esquerda

## Screenshots
### Rodando o comando flip
![flip](screenshots/command_flip.png)

### Resultado do comando flip
![flip_result](screenshots/result_flip.png)

### Rodando o comando rotate
![all_edges_example](screenshots/command_rotate.png)

### Resultado do comando rotate
![all_edges_example](screenshots/result_rotate.png)

## Instalação
**Linguagem**: Python<br>
Para executar, primeiramente é necessário ter o [pip](https://pypi.org/project/pip/) e o [python](https://www.python.org/downloads/) instalados.

Posteriormente, execute:

```
pip install -r requirements.txt
```

para a instalação das dependências e:

```
python /src/main.py <comando>
```

para rodar programa para o *comando* desejado.

Obs.: *Os comandos disponíveis serão apresentados na seção abaixo*

## Uso

Para espelhar uma imagem:

```
python /src/main.py flip [ filepath ] [ outputpath ] [ --numpy ]
```

Para rotacionar uma imagem:

```
python /src/main.py rotate [ filepath ] [ outputpath ] [ --numpy ]
```

Onde:

filepath = caminho da imagem a ser manipulada <br>
outputpath = caminho de destino da imagem manipulada <br>
--numpy = utilizar algoritmo de multiplicação do numpy <br>

Exemplos:
python /src/main.py rotate pikachu.png . --numpy <br>

python /src/main.py flip pikachu.png . <br>
## Observações

Por razões de escopo, convertemos a imagem para preto e branco para que seja uma representação de uma matriz quadradada com as dimensões da imagem.

Adicionamos uma imagem do pikachu para exemplo.
