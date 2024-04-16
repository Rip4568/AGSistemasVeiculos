
# AGSistemas Veiculos

E é com grande prazer que anuncio mais um desafio feito para a empresa AGSistema como desafio!
A ideia principal é fazer uma gestão de carros e motoristas tendo total controle sobre edição, deletação e criação. Existe alguns pontos que faltou porem como o projeto em si esta feito. O motivo pelo qual não ter terminado. Todas as funcionalidades, como a edição e a exclusão de motorista e veículo é pq isso demandaria mais tempo para ser feito. Coisa que eu não gosto de fazer quando se trata de um projeto de apenas desafio. Caso queira ver o digrama e todas as deciões que tomei na construção de cada campo junto com seus relacionamentos, basta clicar no link: [AGSitemasDiagrama](https://dbdiagram.io/d/AGSistemasVeiculos-661a8ef903593b6b61e7fa7e)


## Rodando localmente

Nesse projeto optei por utilziar o gerenciador _poetry_, o motivo de utilizar é por causa da tecnologia mais robusta no quesito de gestão de dependencias a depender do SO que estiver rodando (diferente do pip, que precisa frequentemente rodar  comandos como freeze, e caso esqueça pode faltar na hora de subir). Não so isso como tambem adicionei o arquivo *docker-compose.yaml* para agilizar no levantamento do banco de dados por contaienr e imagem. OBS: não adicionei o aruqivo dockerFile pois não havera necessidade para hospedar.

Tendo isso em mente segue abaixo passo a passo para rodar e testar;
1) Clonar o repositorio
```bash
  git clone https://github.com/Rip4568/AGSistemasVeiculos
```
2)Entrando na pasta do projeto
```bash
  cd AGSistemasVeiculos
```
3)instalar o poetry na sua maquina (obs: supondo previamente que você ja instalou o python:3.10^ + pip)

```bash
  pip install poetry
```

Inicie o poetry

```bash
  poetry shell
```
instale as dependencias
```bash
  poetry install (ou poetry add)
```

Agora havera duas formas de você levantar o projeto com o banco de dados. A primeira seria você tendo o MySQL workbanch instalado no seu computador e configurar as variaveis de ambiente para configurar com aconexão, a segunda seria usando o docker, caso você esteja usando o windows recomendo instalar o Docker Desktop. se por acaso você queira utilizar o sqlite fique a vontade, basta utilizar o codigo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
no settings.py.

instale as dependencias
```bash
  docker compose up --build
```

inicado o docker, rode o comando para aplicar as migrações:
instale as dependencias
```bash
  python manage.py migrate
```

apos isso, se tudo estiver correto rode o comando para inicializar o servidor:
instale as dependencias
```bash
  python manage.py runserver
```
## Rodando os testes

Durante o processo de desenvolvimento apliquei alguns testes para testar meu raciocinio para aplicação da regra de negocio, caso voce queira fazer o mesmo basta rodar o comando:

```bash
  python manage.py test
```


## Melhorias

O que pode melhorar no projeto?

- Responsividade, telas muito estreitas os elementos acabam ficando sobrepostos
- Mascara. adicionar mascaras no inputs para auxiliar o usuario para preencher corretamente todos os campos e evitar erros
- Autenticação. no momento o projeto se encotnra bem inseguro por não ter nenhum tipo de validação ou regra para determinar que tipo de usuario vai poder usar ou qual campo vai poder modificar.
- Paginação. no momento todos os registros estão sendo mostrados de uma unica vez, isso pode resultar em sobrecarga nos dispositivos que estiverem vizualizando.
- Single Page Aplication. O django Template é otimo, porem para cada alternancia de pagina esta sendo renderizado a pagina inteira de uma vez, uma abordagem melhor seria renderizar somente o conteudo e identificar quais são os elementos que se repetem para não incluir na renderização

