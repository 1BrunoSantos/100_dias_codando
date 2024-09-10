# VARIÁVEIS E CONSTANTES
    
**Variáveis**: são locais na memória onde você pode armazenar dados que podem mudar durante a execução do programa.
**Constantes**: são semelhantes, mas seus valores não mudam após serem definidos.

- **Variável**
```python
idade = 36 # Variável que pode mudar
nome = "Bruno"
```

- **Constante**
```python
PI = 3.14 # Valor imutável
```

# TIPOS DE DADOS

- **Inteiros (int)**: Representa  números inteiros.
```python
idade = 36 # Tipo int
```

- **Float (float)**: Representa números com ponto flutuante.
```python
peso = 85.1 # Tipo float
```

- **String (str)**: Representa texto.
```python
saudacao = "Olá, Mundo!" # Tipo str
```

- **Booleano (boolean)**: Representa valores verdadeiros ou falsos.
```python
verdadeiro  = True # Tipo boolean
falso = False
```
# ESTRUTURA DE DADOS

- **Listas**: Coleções ordenadas de itens que podem ser modificadas.

```python
frutas = ["maça", "banana", "laranja"] # Lista
frutas.append("uva") # Adiciona  "uva" à lista
```
- **Dicionários**: Coleções de pares chave-valor, onde as chaves são únicas.

```python
pessoa = {
    "nome": "Bruno"
    "idade": "36"
    "cidade": "São Paulo"
} # Dicionário
pessoa["idade"] = 37 # Atualiza o valor da chave "idade"
```

# OPERADORES

- **Operadores Matemáticos**: usados para realizar operações aritméticas.
```python
a = 10
b = 15
soma = a + b          # Adição
subtracao = a - b     # Subtração
multiplicacao = a * b # Multiplicação
divisao = a / b       # Divisão
``` 

- **Operadores Lógicos**: usados para comninar condições booleanas.
```python
x = True
y = False
resultado = x and y # AND: False
resultado = x or y # OR: True
resultado = not x # NOT: False
```

- **Operadores Comparativos**: Usados para comparar valores.
``` python
a = 10
b = 20
igual = a == b # Igual a: False
diferente = a != b # Diferente de: True
maior = a > b # Maior que: False
menor = a < b # Menor que: True
```
