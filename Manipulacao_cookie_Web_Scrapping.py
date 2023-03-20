from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pickle


class Acesso:
    '''
        Observações:
        
            INSTRUÇÕES PARA CAPTURAR COOKIE 
                - USE A FUNÇÃO 'Acesso.abre_html' -> FAÇA LOGIN DO SITE, APÓS PÁGINA SER ABERTA, E ABRA ALGUM DIRETÓRIO DENTRO DA PÁGINA LOGADA
                - APÓS ISSO, CHAME A FUNÇÃO 'Acesso.salva_cookies' -> APÓS ISSO, FECHA A PÁGINA 

            PRÓXIMOS USOS:
                - USE A FUNÇÃO 'Acesso.abre_html'
                - COM A PÁGINA ABERTA, REQUISITANDO LOGIN, CHAME 'Acesso.aplica_cookies'
                - APÓS ISSO, CHAME A FUNÇÃO 'Acesso.abre_html' NOVAMENTE, PARA A PÁGINA CARREGAR COM OS COOKIES APLICADOS

        '''
    # -------------------------------------------------------------------------------------------------------- #
    # Função: salva_cookies
    #
    # Descrição: Salva Cookies da seesão por extensão pickle
    #
    # Parâmetros: 1) Driver: com a página já na sessão logada
    #             2) Dir: diretório que será salvo o cookie 
    #
    # --------------------------------------------------------------------------------------------------------- #
    def salva_cookies(driver, dir):

        '''
            Parâmetros:
                1) driver: driver retornado pela função 'abre_html'
                2) dir: Diretório onde será salvo o cookie 
        
        '''

        try:
            pickle.dump(driver.get_cookies(), open(fr'{dir}\cookies.pkl', "wb"))
            print("Cookie novo foi atualizado!")
        except:
            print("O novo cookie não foi salvo!")


    # -------------------------------------------------------------------------------------------------------- #
    # Função: abre_html
    #
    # Descrição: Realiza a instalação do chromedrivemanager para abertura da página no google
    #
    # Parâmetros: 1) Options = opções para alterar as configurações do google na página aberta 
    #
    # --------------------------------------------------------------------------------------------------------- #
    def abre_html(pagina, options = None):

        '''
            Parâmetros:
                1) pagina: página de interesse em scrapping, que requer login
            
            Retorno:
                1) driver: driver que sustenta a página 
        '''

        # ---------------------Outros parâmetros que são de extrema valia para uma melhor aplicação do scrapping automático-------------------#
                ## Explicita opções de parâmetros que serão passados para o selenium 
        #options = Options()
        
                ## Acrescenta um parâmetro de diretório para salvar o dowload realizado no controle do selenium (ele realiza o dowload já para a pasta de destino colocada, ao invés da pasta de dowloads do google)
        #options.add_experimental_option("prefs", {
        #    "download.default_directory": fr"{dir_pasta}",
        #})

                ## Acrescenta parâmetro para realizar o Scrapping em background
        #options.add_argument("--headless")

        ## Instalo o driver manager que será responsável pela sustentação da aplicação
        s = Service(ChromeDriverManager().install())
        ## Explicito o driver 
        driver = webdriver.Chrome(service= s, chrome_options= options)
        ## Seto a página em janela cheia
        driver.maximize_window()
        ## Abro a página
        driver.get(pagina)
        
        return driver


    # -------------------------------------------------------------------------------------------------------- #
    # Função: aplica_cookies
    #
    # Descrição: Realiza o delete dos cookies da página aberta na função acima e realiza o import dos cookies que já possuem liberação de acesso
    #
    # Parâmetros: 1) driver = driver já aberto na página de login 
    #             2) dir = mesmo diretório que foi salvo o cookie
    #
    # --------------------------------------------------------------------------------------------------------- #
    def aplica_cookies(driver, dir):

        '''
            Parâmetros:
                1) driver: driver retornado pela função 'abre_html'
                2) dir: diretório onde foi salvo o cookie na primeira função

        '''

        try:
            ## Carrego os cookies
            cookies = pickle.load(open(fr'{dir}\cookies.pkl', "rb"))
            ## Deleto os cookies da página
            driver.delete_all_cookies()

            for cookie in cookies:
                ## Verifico a chave 'expiry' do cookie (que é um dicionário)
                if isinstance(cookie.get('expiry'), float):
                    cookie['expiry'] = int(cookie['expiry']) 

                ## Aplico o valor da chave no driver da página
                driver.add_cookie(cookie)
            print("Os cookies foram aplicados com sucesso!")

        except:
            print("Houve um problema ao aplicar os cookies")
            raise Exception
        return driver

