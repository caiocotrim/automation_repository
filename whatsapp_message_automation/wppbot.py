from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time 
import schedule

class Whatsappbot: 
    def __init__(self):
        #Mensagem que será enviada
        self.mensagem = "E aí, amor, como tá? To acabando meu treino aqui agora. Umas 8h já estou em casa."
        
        #Nome do contato que será buscado
        self.contatos = ["Vida"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')

        service = Service(executable_path = r'C:\Eu\Estudos\AutoDidata\Automações\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service = service, options = options)

        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)

    def enviarMensagens(self):
        
        #Comentários abaixo são marcações HTML (via DevTools) usadas para identificar os elementos corretos
        # (Localizar Contato) <span dir="auto" title="Vida" class="x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1rg5ohu _ao3e" style="min-height: 0px;">Vida</span>
        # (Campo de Digitação da Mensagem) <div aria-activedescendant="" aria-autocomplete="list" -label="Digite uma mensagem"
        # (Botão de Envio) <span aria-hidden="true" data-icon="send" class="">

        for contato in self.contatos:
            contato_element = self.driver.find_element(By.XPATH, f"//span[@title='{contato}']")
            time.sleep(5)
            contato_element.click()
            
            chat_box = self.driver.find_element(By.XPATH, "//div[@aria-label='Digite uma mensagem']")
            time.sleep(5)
            chat_box.click()

            chat_box.send_keys(self.mensagem) 
            send_button = self.driver.find_element(By.XPATH, "//span[@data-icon='send']")
            time.sleep(5)

            send_button.click()
            time.sleep(5)

            self.driver.quit()

bot = Whatsappbot()

#Agenda o horário de envio da mensagem
schedule.every().day.at("07:40").do(bot.enviarMensagens)    

#Loop contínuo que verifica se está na hora de enviar a mensagem
while True:
    schedule.run_pending()
    time.sleep(1)        
