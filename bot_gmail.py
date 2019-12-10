from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Send(object):
    def __init__(self, email, senha, assunto, destinatario, mensages,url):
        self.email = email
        self.senha = senha
        self.assunto = assunto
        self.destinatario = destinatario
        self.mensagem = mensagem
        self.url = url



# Atribuição de valores de e-mail
email = 'aqui_vai_o_email'
senha = 'aqui_vai_a_senha'
assunto = 'Teste de envio de email via bot(Gmail)'
destinatario = 'aqui_vai_o_destinatario'
mensagem = 'Primeiro teste de envio de email com meu bot'
url = 'https://accounts.google.com/AccountChooser/signinchooser?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&flowName=GlifWebSignIn&flowEntry=AccountChooser'
gmailbot = Send(email, senha, assunto, destinatario, mensagem,url)



# iniciando o bot
print('Start me bot Mail')

# Setando as configurações do chromedriver
driver = webdriver.Chrome('chromedriver')
driver.get(gmailbot.url)
time.sleep(1)


# Setando os dados para emmail de login no email
login_id = "identifierId"
login = driver.find_element_by_id(login_id)
login.clear()
login.send_keys(gmailbot.email)
login.send_keys(Keys.RETURN)
time.sleep(1)

# Setando os dados de acesso (senha)
password = driver.find_element_by_name('password')
password.clear()
password.send_keys(gmailbot.senha)
password.send_keys(Keys.RETURN)
time.sleep(1)

# Enviando mensagem de sucesso no login do email
print('Logando na conta de email')
print('Abrindo sua caixa de envio')
driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(8)


#Setando os campos de destinatário
print('Buscando destinatario para envio')
para = driver.find_element_by_name('to')
para.clear()
para.send_keys(gmailbot.destinatario)
para.send_keys(Keys.RETURN)
time.sleep(5)


#Setando os campos do assunto
print('Definindo o assunto da mensagem')
titulo =  driver.find_element_by_name('subjectbox')
titulo.clear()
titulo.send_keys(gmailbot.assunto)
titulo.send_keys(Keys.RETURN)
time.sleep(5)


#Setando os campos para o envio da mensagem
print('Escrevendo a mensagem para o envio')
corpo_do_texto = driver.find_element_by_xpath("//div[@role='textbox']")
corpo_do_texto.clear()
corpo_do_texto.send_keys(gmailbot.mensagem)
corpo_do_texto.send_keys(Keys.RETURN)

#Enviando o email
time.sleep(10)
enviar = driver.find_element_by_xpath("//div[@aria-label='Enviar ‪(Ctrl-Enter)‬']")
enviar.click()
driver.close()