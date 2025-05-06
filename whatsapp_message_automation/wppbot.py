from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time 
import schedule

class Whatsappbot: 
    def __init__(self):
        self.mensagem = "Tô almoçando, mo. Quando terminar de almoçar eu te respondo e escuto seu áudio direitinho. Te amo!"
        self.contatos = ["Vida"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')

        service = Service(executable_path = r'C:\Eu\Estudos\AutoDidata\Automações\chromedriver-win64\chromedriver.exe')
        self.driver = webdriver.Chrome(service = service, options = options)

        self.driver.get('https://web.whatsapp.com')
        time.sleep(30)

    def enviarMensagens(self):
        #<span dir="auto" title="Vida" class="x1iyjqo2 x6ikm8r x10wlt62 x1n2onr6 xlyipyv xuxw1ft x1rg5ohu _ao3e" style="min-height: 0px;">Vida</span>
        #<div aria-activedescendant="" aria-autocomplete="list" -label="Digite uma mensagem"
        #<span aria-hidden="true" data-icon="send" class="">

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

schedule.every().day.at("13:10").do(bot.enviarMensagens)

while True:
    schedule.run_pending()
    time.sleep(1)        
