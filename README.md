# WEB SCRAPING

### Sobre

O objetivo deste projeto é desenvolver um scraper para capturar e tratar os dados presente no site [worldometers](https://www.worldometers.info/) a fim de gerar uma API.
<br/>

### 📌 Conteúdo

* [Sobre](#sobre)
* [Status](#status)
* [Características](#características)
* [Requisitos](#requisitos)
* [Tecnologia](#tecnologia)
* [Autor](#autor)
* [Licença](#licença)
<br/>

### Status

Projeto concluído ✅
<br/>

### Características

- [x] **Scraper**
- [x] **Converson dict para json**
<br/>

### Requisitos

1. Para rodar a aplicação é necessário a instalação do [Python 3](https://www.python.org/downloads/).
<br/>

2. O próximo passo é clonar este repositório para algum local do computador
por meio do terminal ou cmd:

```bash
    $ git clone https://github.com/MatheusBibiano/Web-Scraping.git
```
<br/>

3. (Opcional) Navegue para dentro da pasta do projeto e crie um ambiente virtual para instalar as dependências:

* Linux
```bash
    $ python3 -m venv venv && source venv/bin/activate
```

* Windows:
    [Criando ambientes virtuais no Windows](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv)
<br/>

4. Feito isso, instale as dependências:

* Linux & Windows
```bash
    $ pip install -r requirements.txt
```
<br/>

5. Após concluir a instalação, baixe o [ChromeDriver](https://chromedriver.chromium.org/downloads) e copie o caminho até ele para a constante **URL** no arquivo **src/variables.py**.
<br/>

6. Por fim, execute a aplicação:
* Linux
```bash
    $ python3 main.py
```

* Windows
```cmd
    > python main.py
```
<br/>

### Tecnologia

A seguinte tecnologia foi utilizada na construção do projeto:

- [Python 3](https://www.python.org/)
<br/>

### Autor

| Matheus Bibiano                                       |
|-------------------------------------------------------|
| <img src="assets/author.png" width="150" height="150">|
| [<img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/matheus-bibiano-alves)|
<br/>

### Licença

[MIT](https://choosealicense.com/licenses/mit/)
