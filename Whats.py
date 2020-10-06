from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


uri = 'https://web.whatsapp.com/'

driver = Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
lista = (By.ID, 'pane-side')
nome_contato = 'Dojo-Bot-Whats'
grupo = (By.XPATH,f"//*[@title='{nome_contato}']")
envia_mensagem = (By.CLASS_NAME,'_3uMse')
envia_botao = (By.XPATH,f"//*[@data-icon='send']")
ler_mensagem = (By.XPATH, 'div[contains(@class, "message-in focusable-list-item")]')
driver.get(uri)

def grupos():
    sleep(10)
    for box in driver.find_elements(*lista):
        box.find_element(*grupo).click()
        # sleep(10)

def Ler_mensagem():
    conv = list()
    for msg in driver.find_elements(*ler_mensagem):
        conv.append(msg.text.split('\n'))
    # conv[-1].pop()
    print(conv)


def envia_msg(mensagem = None):
    if mensagem != None or mensagem != '':
        box = driver.find_element(*envia_mensagem)
        box.click()
        box.send_keys(mensagem+'\n')
        print(mensagem)
    else:
        pass

def conversa():
    conversas = set()
    grupos()
    conversas.add('Iniciando o Bot')
    envia_msg('Iniciando o Bot')
    while True:
        texto = Ler_mensagem()
        if texto not in conversas:
            envia_msg(input())

grupos()
Ler_mensagem()
# conversa()

sleep(5)
driver.quit()
