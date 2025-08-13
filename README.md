<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=FF0000&height=120&section=header"/>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=FFFFFF&size=35&center=true&vCenter=true&width=1000&lines=Bem-vindo(a)+ao+nosso+repositório!;Esperamos+que+goste+do+game!+%F0%9F%8E%AE)](https://git.io/typing-svg)

<img width="100%" src="https://capsule-render.vercel.app/api?type=waving&color=FF0000&height=120&section=footer"/>

<p align="center">
  <img src="https://i.pinimg.com/originals/a0/10/d9/a010d97c5a551c1e862b7ff69f294d7a.gif" width="300"/>
</p>

<br>

<h1 align="center" style="margin-top: 20px;">CIn Bizarre Adventures</h1>


### 📌 Descrição
• Este é o relatório do projeto final da disciplina de Introdução a Programação [ IP ] que irá abordar todo o processo de desenvolvimento, desafios, erros e vitórias durante a criação do jogo.


#


### 📌 Equipe
| Nome completo                              | Email     |
|-------------------------------------------|-------------|
| Luiz Philip Santiago da Silva             | `< lpss@cin.ufpe.br >`    |
| Felipe Augusto Lira Dias                  | `< fald@cin.ufpe.br >`    |
| Arthur Dias de Oliveira                   | `< ado@cin.ufpe.br >`     |
| Gabriel André Souza Fernandes da Cunha    | `< gasfc@cin.ufpe.br >`   |
| Andreson Gomes de Lima                    | `< agl4@cin.ufpe.br >`    |


# 


### 📌 Etapa I - *Design*
• Foi realizada a primeira divisão do projeto: *design*. Cada membro - ou dupla - ficou responsável por uma ou mais atribuições do aspecto do design do projeto.

| Responsável(s)                             | Responsabilidade     |
|-------------------------------------------|-------------|
| Luiz Philip Santiago da Silva e Felipe Augusto Lira Dias           | `Criação do mapa`    |
| Arthur Dias de Oliveira                   | `Telas do game`     |
| Gabriel André Souza Fernandes da Cunha    | `Coletáveis`   |
| Andreson Gomes de Lima                    | `Personagens`    |


#


### 📌 Etapa II - *Programação inicial*
• Foi realizada a primeira etapa da programação que estabeleceu 85% dos requisitos mínimos do game.

| Responsável(s)                             | Responsabilidade     |
|-------------------------------------------|-------------|
| Luiz Philip Santiago da Silva e Felipe Augusto Lira Dias           | `movimentação do personagem no mapa`    |
| Arthur Dias de Oliveira                   | `Interface com o o usuário (menu inicial, texto, afins)`     |
| Gabriel André Souza Fernandes da Cunha e Andreson Gomes de Lima    | `Mecânica de colisão com os coletáveis`   |


# 


### 📌 Etapa III - *Programação média*
• Foi realizada a segunda etapa da programação estabeleceu 100% dos requisitos mínimos do game.

| Responsável(s)                             | Responsabilidade     |
|-------------------------------------------|-------------|
| Luiz Philip Santiago da Silva e Felipe Augusto Lira Dias           | `Lógica de colisão com o mapa, iluminação (efeito lanterna)`    |
| Arthur Dias de Oliveira                   | `Inventário, capas de vitória e derrota`     |
| Gabriel André Souza Fernandes da Cunha e Andreson Gomes de Lima    | `Lógica de vitória e derrota`   |


#


### 📌 Etapa IV - *Programação final*
• Foi realizada a terceira etapa de programação do jogo, a qual cada membro ficou livre para corrigir e fazer alterações que considerou necessárias (após aval do grupo). Não foi estabelecido nenhum tipo de divisão, a intenção era simplesmente avaliar as funcionalidades atuais e verificar ocorrências de erros, bugs ou duplicidade nos códigos.


# 


### 📌 Etapa IV - *Programação adicional*
• Nesse ponto cada membro avaliava o que poderiam acrescentar na jogabilidade do game para deixá-lo mais interativo, dinâmico e divertido. Importante ressaltar que essa etapa não significou o necessariamente no incremento dessas ideias, mas sim uma análise que se baseou na dificuldade de execução, experiência do game e tempo, lgumas delas foram:

| Idealizador(s)         | Ideia(s)       | Avaliação           |
|------------------|-----------------|--------------------|
| Gabriel          | Mecânica de tecla para eliminação do player 1         | `Positiva`           |
| Philip           | Mecânica de furto   | `Positiva`     |
| Felipe           | Mecânica de zoom | `Em análise` |
| Andreson | Score com moedas | `Em processamento` |


<br>

<h1 align="center" style="margin-top: 20px;">Arquitetura do Projeto</h1>

```Bash
CIN_BIZARRE_ADVENTURES/
│   ├── buttons/                                  # pasta com a imagem do botão play
│   │   ├── botao_padrao.png
│   ├── coletaveis/                               # pasta com as imagens dos coletáveis
│   │   ├── coin.png
│   │   ├── flashlight.png
│   │   ├── gasoline.png
│   │   ├── generator.png
│   │   ├── heart.png
│   ├── mapa/                                     # pasta com o mapa criado no Tiled    
│   │   ├── assets/                               # subpasta com os assets utilizados
│   │   │   ├── assets_base.png
│   │   │   ├── assets_decorações.png
│   │   │   ├── assets_parede.png
│   │   │   ├── lava.png
│   │   ├── mapa.tiled-project
│   │   ├── mapa.tiled-session
│   │   ├── map.tmx
│   ├── personagens/                              # pasta com os personagens
│   │   ├── player_1/
│   │   │   ├── costas/
│   │   │   │   ├── c1.png
│   │   │   │   ├── c2.png
│   │   │   │   ├── c3.png
│   │   │   ├── direita/
│   │   │   │   ├── d1.png
│   │   │   │   ├── d2.png
│   │   │   │   ├── d3.png
│   │   │   ├── esquerda/
│   │   │   │   ├── e1.png
│   │   │   │   ├── e2.png
│   │   │   │   ├── e3.png
│   │   │   ├── frente/
│   │   │   │   ├── f1.png
│   │   │   │   ├── f2.png
│   │   │   │   ├── f3.png
│   │   ├── player_2/
│   │   │   ├── costasV/
│   │   │   │   ├── cV1.png
│   │   │   │   ├── cV2.png
│   │   │   │   ├── cV3.png
│   │   │   ├── direitaV/
│   │   │   │   ├── dV1.png
│   │   │   │   ├── dV2.png
│   │   │   │   ├── dV3.png
│   │   │   ├── esquerdaV/
│   │   │   │   ├── eV1.png
│   │   │   │   ├── eV2.png
│   │   │   │   ├── eV3.png
│   │   │   ├── frenteV/
│   │   │   │   ├── fV1.png
│   │   │   │   ├── fV2.png
│   │   │   │   ├── fV3.png
│   ├── sons/                              # pasta com os sons utilizados na ambientação                         
│   │   ├── background.ogg
│   │   ├── collectible.ogg
│   │   ├── defeat.ogg
│   │   ├── flashlight.ogg
│   │   ├── victory.ogg
│   ├── telas/                             # pasta com as imagens da tela de início, vitória e derrota
│   │   ├── tela_derrota.ogg
│   │   ├── tela_inicial.ogg
│   │   ├── tela_vitoria.ogg
│   ├── button.py                          # arquivo com a classe: 'class Button' para criar o botão play e iniciar o jogo
│   ├── collision.py                       # arquivo com a classe: 'class Colisao' para definir a lógica de colisão com os coletáveis no mapa
│   ├── inventory.py                       # arquivo com a lógica de inventário na tela do mapa (associada diretamente ao arquivo 'collision.py' e 'screen.py')
│   ├── lighting.py                        # arquivo com a classe: 'class Lighting' responsável por criar o efeito de gradiente de luz (lanterna)
│   ├── player.py                          # arquivo com a classe: 'class Player' responsável pela lógica de criação do player_1, sua movimentação, animação, etc
│   ├── player2.py                         # arquivo com a classe: 'class Player2' responsável pela lógica de criação do player_2, sua movimentação, animação, etc
│   ├── screen.py                          # arquivo responsável por unir os demais arquivos na tela do jogo
│   ├── main.py                            # arquivo responsável por fazer o jogo 'rodar'            

```


<br>

<h1 align="center" style="margin-top: 20px;">Ferramentas</h1>

| Ferramentas, bibliotecas, frameworks          |Justificativa |      
|------------------|-----------------|
| Tiled          | `Recomendação dos monitores na criação do mapa`         | 
| Pytmx           | `Necessário para rodar o mapa feito no Tiled`   | 
| Itch.io           | `Usado para baixar os assets utilizados na criação do mapa e personages. Créditos de criação: Yanin Yunus` | 
| Ezigif.com | `Recorte e rotação de imagens` | 
| Pygame | `Obrigatório usá-lo` |
| GitHub | `Praticidade` |
| Git | `Versionamento dos códigos` |
| VsCode | `Praticidade` |
| Pixilart | `'Foi o primeiro que encontrei para fazer as artes'` |
| Google | `Imagens gerais` |
| Chat GPT | `Estudos, geração de imagem. Observação: também foi utilizado como guia durante o processo de criação, mas não foi responsável por produzir o código de nenhum arquivo; seu uso foi consciente.` |


<br>

<h1 align="center" style="margin-top: 20px;">Conceitos Utilizados</h1>
• Os conceitos utilizados vão desde um simples 'print' para testes quanto POO. Em suma, tudo que foi discutido, estudado e praticado durante o período foi utilizado na criação do jogo. Foram utilizados em praticamente todos os arquivos: print's para testes, listas, dicionários, funções, POO...


<br>

<h1 align="center" style="margin-top: 20px;">Desafios e Erros</h1>

### 📌 Qual foi o maior erro cometido durante o projeto? 
• Acreditamos que começar pelo design do jogo ao invés da programação não foi a melhor das ideias. Julgamos que deveríamos ter começado desde o início com a programação, mesmo que básica, para analisar a fluidez e funcionamento das ideias, haja vista que no decorrer do processo a parte de design teve erros que atrasaram nosso cronograma. Acabamos lidando com isso da seguinte forma: com ou sem design pronto, comece a codar com o que tem. Focar primeiramente no Frontend e só depois do Backend foi o nosso pior erro.

### 📌 Qual foi o maior desafio enfrentado durante o projeto?  
• Houve dois principais desafios durante o projeto: o primeiro foi conciliar o tempo da criação do jogo com os demais projetos e avaliações do final do período, o segundo foi conciliar nossas capacidades, tempo e ideias mirabolantes para o jogo. Mas com planejamento efetivo e bem coordenado conseguimos resolver os problemas que encontramos durante o processo, pois dividimos as tarefas de forma efetiva e prática, ou seja, cada indivíduo sabia o que tinha que fazer e até quando tinha que dar um aval sobre sua responsabilidade.

### 📌 Quais as lições aprendidas durante o projeto?
1. Com ou sem o design, comece a codar; <br>
2. Se está com dificuldade, avise, comunicação em grupo é a chafe de tudo; <br>
3. Delimite não só suas responsabilidades, mas o tempo que você tem para desenvolvê-las; <br>
4. **NUNCA** comece ou espere todo o Frontend para desenvolver o Backend; <br>
5. Não tenha medo de pensar demais, uma ideia 'boba' pode ser genial; <br>
6. Comunique-se; <br>
7. Aprenda a usar Git o mais cedo possível; <br>
8. Organização é tudo; <br>
9. Como disse Arthur: "Primeiro você coda, depois você pensa".


<br>

<h1 align="center" style="margin-top: 20px;">Sobre o Jogo</h1>

<p align="center">
CIn Bizarre Adventures mergulha nas mecânicas clássicas de "Pac-Man" e "Fireboy and Watergirl", mas com uma pegada sombria e aterrorizante. Dois personagens — Vermelho e Amarelo — estão presos em um labirinto escuro, onde a visibilidade é mínima e cada passo é um desafio. Vermelho precisa encontrar lanternas para ampliar sua visão e, mais importante, coletar gasolina suficiente para ligar o gerador e restaurar a luz. Enquanto isso, Amarelo persegue implacavelmente Vermelho, com visão ampliada, velocidade superior e uma única missão: eliminá-lo.
</p>

<p align="center">
A tensão é constante. Cada canto do labirinto pode esconder o perigo, e Vermelho, além de lutar para recuperar o combustível, precisa escapar das garras de seu perseguidor. Felizmente, espalhados pelo caminho, corações de vida oferecem uma segunda — ou até terceira — chance para Vermelho, mas só se ele conseguir alcançá-los a tempo.
</p>

<p align="center">
Prepare-se para um jogo onde a luz é esperança, a escuridão é ameaça, e cada decisão pode ser a diferença entre sobreviver ou ser eliminado.
</p>
