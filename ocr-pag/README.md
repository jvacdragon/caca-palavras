# Caça palavras utilizando OCR

Neste projeto é feito a leitura de um caça palavras em formato de imagem usando OCR com a biblioteca pythesseract. O código recebe de inicio a quantidade de linhas, colunas, um array com as palavras que devem ser encontradas e o caminho para o arquivo da imagem.

## Requisitos

As principais bibliotecas utilizadas são:

- opencv-python
- pythesseract
- re

Para instala-las no terminal, basta utilizar:

```bash
pip install opencv-python pytesseract numpy
```

## Como funciona

Além do código principal(main), também há três funções principais que estão no arquivo helpers, são elas:

- cut: Função que recebe a imagem e a quantidade de linhas, devolvendo como resposta um array com a imagem em tons de cinza e valores usados para poder cortar a imagem de forma correta para que seja feita a leitura das linhas

- find: Recebe um array duplo com as letras por linha e letras por coluna do caça palavras. Também recebe um array com as palavras que devem ser encontradas. No fim ela retorna um array de objetos que indicam o nome da palavras, em qual linha ou coluna foi encontrada e com o index de inicio de onde foi achada na linha ou coluna

- process_image_text: Função que recebe uma imagem e a configuração de leitura para o tesseract. Aqui é feita a leitura da imagem e retornada as letras encontradas

## Como usar

1. Carregue a imagem do caça-palavras: O caminho da imagem deve ser passado como parâmetro.

2. Defina as palavras a serem encontradas: Você pode configurar uma lista com as palavras que deseja procurar.

3. Defina o número de linhas e colunas: O número de linhas e colunas do caça-palavras é importante para a divisão da imagem em partes, permitindo que as palavras sejam lidas corretamente.

4. Execute o código: O código processará a imagem, buscará as palavras e retornará suas posições.

No repositório ja deixei um exemplo sendo usado e há duas imagens também para se testar. Caso queira utilizar o código e testar também com imagens diferentes, lembre-se de utilizar imagens padronizadas como essas de exemplo que tem ena pasta ./src/

## Estrutura dos diretórios

```bash
.
├── src/
│   └── caca_palavras.jpg   # Imagem 1 do caça-palavras
│   └── caca_palavras2.jpg  # Imagem 2 do caça-palavras
├── helpers.py              # Funções auxiliares
├── main.py                 # Arquivo principal
├── README.md               # Documentação do projeto
└── requirements.txt        # Dependências do projeto
```