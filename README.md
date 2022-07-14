# case-stone
Desafio Observabilidade Pagar.me

Primeiro passo, baixar a imagem que está no docker hub 

$ docker pull jbcurty/desafio-stone:latest

Segundo passo, executar a imagem baixada

$ docker run -p 5000:5000 -d jbcurty/desafio-stone

Basta abrir o navegador e inserir 127.0.0.1:5000

![image](https://user-images.githubusercontent.com/45775861/179020811-f199ff56-c3b2-4362-8060-7cc98ee66049.png)

Para validar a aplicação conforme solicitado, colocar /api na URI

Com a aplicação em execução, já é possível realizar um curl ou utilizar aplicativos que realizam consultas via HTTP, como Insomnia ou Postman.

Em nível de observabilidade, para esse caso de uso, a aplicação está sendo executada em um container local, mas poderiamos ter enviado a imagem para um ECR e subir em um k8s. O próximo passo seria colocar ele como target de um prometheus, e utilizar o grafana como visualização das métricas.
