# WeaterBOT discord
Sistema para visualizar o clima e temperatura de um local integrado em um BOT para o Discord.

![](https://cdn.discordapp.com/attachments/1150272954005979156/1150579030899302480/screenshot_weatherbot.png)

# Como rodar o bot localmente:

### Instalando o pycord
para instalar o pycord em sua máquina abra o seu terminal e digite o seguinte comando
```pip install py-cord```.

### Criando uma aplicação BOT para o discord

![](https://gblobscdn.gitbook.com/assets%2F-MjPk-Yu4sOq8KGrr_yG%2F-MjdW3OQnwUhacopqSWw%2F-Mjd_-mxrJCrzmaXrAg8%2Fimage.png?alt=media&token=b8e2ae6c-2290-4d37-ad7c-eb412f3fb00e)

para criar uma aplicação no discord siga os seguintes passos:
1. Vá para o [Discord Developer Portal](https://discord.com/developers/applications) e clique em ```New application```.
2. Dê seu bot um nome, e clique em ```Create```.
3. Clique na aba ```Bot``` no canto esquerdo da tela.
4. Clique em ```Add Bot```.
5. Agora você pode trocar o nome, icone e descrição de seu bot de como desejar.

### Convidando o BOT para um servidor

Agora, vamos adicionar o bot a alguns servidores. Vá para a aba ```OAuth2``` no painel esquerdo e selecione ```bot``` e ```applications.commands``` como escopos.

Você pode querer que seu bot tenha comandos de aplicação, que é o que o escopo ```applications.commands``` permite que seu bot faça.

Em seguida, você deseja escolher quais permissões o bot terá e selecioná-las. Por enquanto, você pode simplesmente dar ao seu bot a permissão de ```administrator```, que concede todas as permissões ao seu bot. Assim que você selecionar as permissões do seu bot, clique em ```Copy``` para obter o link de convite para o bot.

![](https://gblobscdn.gitbook.com/assets%2F-MjPk-Yu4sOq8KGrr_yG%2F-Mk6tNY3LfDkjd6pqdpL%2F-Mk6tkdpddEWoa2jczZk%2Fimage.png?alt=media&token=52c8a29f-a798-48f8-a8c7-4ecca2681f79)

Você pode agora usar este link gerado para convidar o seu bot em algum servidor.

### Tokens

Agora que você tem uma aplicação para seu BOT, você precisa logar, para logar, precisamos da senha do BOT. Todos os "users" e BOTs têm um ```Token```. Um token é como uma senha, que permite logar o BOT no Discord.
Para usar o token do seu BOT você precisa:

1. Ir para a aba ```BOT```
2. Clicar no botão ```Copy``` na seção de token.

![](https://gblobscdn.gitbook.com/assets%2F-MjPk-Yu4sOq8KGrr_yG%2F-MjdbU12JISJorAZxrKH%2F-MjdbpUsapzb5n15Po5P%2Fimage.png?alt=media&token=118e259f-940a-4f6c-b3a3-c29f3a54100d)

### Passos Finais

Para rodar o BOT, você vai precisar baixar os arquivos deste repositório e editar algumas linhas de código.

![](https://media.discordapp.net/attachments/1150272954005979156/1150586332717006858/image.png)

Para isso, substitua essa parte do código com o seguinte código:
```
import requests
import discord
from discord.ext import commands

token = ("TOKEN")
```
