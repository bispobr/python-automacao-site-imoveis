from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import openpyxl

site = 'https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=21&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4'
drive = webdriver.Edge()
drive.get(site)

precos = drive.find_elements(By.XPATH, "//div[@class='card-valores']/div")
link = drive.find_elements(By.XPATH, "//a[@class='carousel-cell is-selected']")

workbook = openpyxl.load_workbook('C:\planilhas\imoveis.xlsx')
pagina = workbook['precos']

for preco, links in zip(precos, link):
    preco_pronto = preco.text.split(' ')[1]
    caminho = links.get_attribute('href')
    data_consulta = datetime.now().strftime('%d/%m/%Y')
    pagina.append([preco_pronto, caminho, data_consulta])

workbook.save('C:\planilhas\imoveis.xlsx')
