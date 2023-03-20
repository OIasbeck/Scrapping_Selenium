# Trabalho de Web Scrapping com manipulação de Cookie com Selenium (Modelo)

Este repositório é um molde que dispões de módulos para manipulação de cookie no acesso de páginas que requerem login

- Salva Cookies
- Abre Html
- Aplica Cookies

## Salva Cookies

Está função tem como funcionalidade ser utilizada apenas no primeiro acesso (Como explicado no último tópico de "Como utilizar") realizando a captura do cookie com a página já logada 

## Abre Html

Realiza a abertura e a explicitação de parâmetros do driver, necessário ler o script para melhor utilização da função.

## Aplica Cookies

Realiza o delete de cookies da página aberta e a inserção dos cookies já salvo, possuindo as credenciais de acesso do site, para que após recarregada a página com os cookies, ele já te jogue para dentro da página

## Como utilizar
OBS: Leia o scipt que está bem comentado para melhor entendimento e utilização

O framework disposto neste repositório teve como objetivo ultrapassar um problema onde Scrappings usuais não passavam, que é quando a página de login de um html qualquer reconhece o controle de software e pede autenticações humanas para o login, ou até mesmo bloqueiam o usuário quando o login e a senha são colocados por métodos de Selenium.
Visto isso, foi montado o script que tem como objetivo ser utilizado da seguinte maneira:
#### Primeiro uso
 
Abra a página na função 'abre_html', com o driver aberto no monitor, coloque o login, a senha e acesse qualquer diretório página
Chame a função 'salva_cookies', e logo em seguida feche a página.

#### Próximos usos

Abra a página na função 'abre_html'
Chame a função 'aplica_cookies'
Recarregue a página com 'driver.get(html)'
Assim, o cookie da página de login será retirado e será acrescido o cookie já salvo no primeiro acesso, com as credênciais de segurança.

## Problemas e melhorias

A lógica acima nem sempre funciona... Tem cookies que expiram, sendo assim necessário a cada login chamar a função 'salva_cookies' a cada uso, isto é, todo vez que rodar será renovado o cookie sem problemas, é necessário apenas descobrir qual tempo de expiração.
Quando sites barram a utilização de Selenium, é possível utilizar uma biblioteca que simula um usuário, chamada 'user_agents' 

