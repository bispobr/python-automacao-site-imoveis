from selenium import webdriver
from selenium.webdriver.common.by import By

site = 'https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=21&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4'
drive = webdriver.Edge()
drive.get(site)


precos = drive.find_elements(By.XPATH,"//div[@class='card-valores']/div")
link = drive.find_elements(By.XPATH,"//a[@class='carousel-cell is-selected']")