# Automação de Consulta de Imóveis

Automação desenvolvida em Python para acessar um site de imóveis utilizando o navegador Microsoft Edge, realizar consultas e coletar informações dos resultados encontrados.

Os dados coletados incluem informações como links dos imóveis, preços e a data da consulta, sendo posteriormente armazenados em uma planilha.

## Funcionalidades

- Acesso automatizado ao site de imóveis
- Execução de buscas
- Coleta de links dos imóveis
- Coleta de preços
- Registro da data da consulta
- Exportação dos dados para planilha
- Automação do navegador Microsoft Edge

## Tecnologias

- Python
- Selenium
- OpenPyXL
- Microsoft Edge

## Requisitos

- Python 3+
- Microsoft Edge
- WebDriver compatível com a versão do navegador, conforme a configuração utilizada pela automação
- Bibliotecas Python utilizadas pelo projeto

## Instalação

Clone o repositório:

```bash
git clone https://github.com/bispobr/python-automacao-site-imoveis.git
cd python-automacao-site-imoveis
```

Instale as dependências:

```bash
pip install selenium openpyxl
```

## Configuração

Antes de executar a automação, configure o local onde a planilha com os resultados será salva, conforme a implementação do projeto.

Também é necessário garantir que o ambiente do Microsoft Edge esteja configurado para execução da automação com Selenium.

## Execução

Execute o arquivo principal da aplicação:

```bash
python app.py
```

Durante a execução, a automação acessará o site configurado, realizará as buscas e armazenará os dados coletados na planilha definida na configuração.

## Fluxo simplificado

```text
Início
  │
  ▼
Abrir navegador Edge
  │
  ▼
Acessar site de imóveis
  │
  ▼
Realizar busca
  │
  ▼
Coletar dados dos imóveis
  │
  ├── Link
  ├── Preço
  └── Data da consulta
  │
  ▼
Salvar dados em planilha
  │
  ▼
Fim
```

## Status

Projeto de automação desenvolvido em Python para prática de automação web, coleta de dados e geração de planilhas.
