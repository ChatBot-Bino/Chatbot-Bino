Este é um documento para orientação em como contribuir para o repositório do Chatbot Bino. Antes de começar a contribuir veja as [issues já abertas](https://github.com/ChatBot-Bino/Bot-Bino/issues), e principalmente o funcionamento de nossa [arquitetura](https://github.com/ChatBot-Bino/Bot-Bino/blob/master/README.md).

Veja as orientações abaixo para cada tipo de contribuição:
- [Comece a contribuir](#comece-a-contribuir)
- [Encontrou um Bug?](#encontrou-um-bug)
- [Consertou um Bug?](#consertou-um-bug)
- [Quer contribuir para a nossa Documentação?](#quer-contribuir-para-a-nossa-documentação)
- [Quer adicionar uma funcionalidade nova?](#quer-adicionar-uma-funcionalidade-nova)

### Comece a contribuir
Quer começar a contribuir para o Chatbot Bino? O processo em geral é bem simples:

- Crie uma issue descrevendo uma funcionalidade que você queira trabalhar ou entre em issues já abertas (caso comece por uma issue já existente comente na issue que você está desenvolvendo).
- Escreva seu código, testes e documentação
- Abra um pull request descrevendo as suas alterações propostas
- Seu pull request será revisado por um dos mantenedores, que pode levantar questões para você sobre eventuais mudanças necessárias ou questões.

Veja nossa [documentação](https://github.com/ChatBot-Bino/Bot-Bino/wiki) para entender um pouco melhor sobre nosso código e [arquitetura](https://github.com/ChatBot-Bino/Bot-Bino/blob/master/README.md), veja nossas issues, principalmente as com as tags `Ajuda` e `Tutorial`, que são as ideais para começar a contribuir para o projeto.


### Encontrou um Bug?
Caso tenha encontrado algum erro, nos informe por uma issue, assim poderemos estar sempre melhorando. Pedimos que seja descritivo, dessa forma poderemos identificar e reproduzir o erro para ser possível consertá-lo.

Antes de reportar o Bug, veja as issues com a tag `bug` e verifique se o erro identificado já não possui uma issue criada.

Para uma boa documentação:
* Nomeie a issue com um nome claro e descritivo de acordo com o problema;
* Descreva o passo a passo para chegar no erro encontrado;
* Mostre exemplos do erro ocorrido;
* Descreva o comportamento esperado e o comportamento obtido;
* Marque a issue criada com a tag `bug`.

Veja a seguinte estrutura de issue:

``` markdown


**Descreva o erro**
Um relatório limpo e conciso sobre o erro encontrado. 

**Para refazer o error**
Passos para reproduzir o comportamento:
1. Vai em '...'
2. Click em '....'
3. Desça até '....'
4. Veja o error

**Comportamento esperado**
Uma descrição limpa a concisa do que se era esperado.

**Screenshots**
Se possível, adicione screenshots para ajudar a explicar o seu problema.

**Descrição do ambiente utilizado**
OS: "..."
Versão: "..."
Etc ...
```

### Consertou um Bug?
Para enviar a sua solução e consertar um bug existente, fork nosso repositório e crie um Pull Request descrevendo o problema e como ele foi corrigido.

Para uma bom Pull Request:
* Nomeie o Pull Request de forma descritiva e clara de acordo com o problema resolvido;
* Descreva o problema e a sua solução;
* Marque a issue que o Pull Request soluciona.

Veja o exemplo abaixo:

``` markdown
**Descrição da mudança**  
<!-- Descreva de forma simples e concisa sobre a mudança feita. -->

**Tipo da mudança**  
<!-- Marque o checkbox correspondente a mudança. -->
- [ ] Correção de bug.
- [ ] Adição de nova fucionalidade.

**Issue relacionada**  
<!-- Link com a isse -->

**Screenshots**  
<!-- Se aplicável, adicione imagens da tela para ajudar a explicar a mudança feita. -->

**Informações adicionais**  
<!-- Comente outra informação relevante sobre o seu problema aqui. -->

**Checklist**  
- [ ] O pull request possui nome significativo.
- [ ] O pull request possui descrição significativa.
- [ ] O pull request possui a marcação correspondente ao tipo da mudança.
- [ ] O pull request possui screenshots quando necessário.
- [ ] O pull request possui labels.


```

### Quer contribuir para a nossa Documentação?
Para contribuir com a documentação, veja a documentação já existente, e as issues pendentes para documentação marcadas com a tag `documentação`.

Caso queira resolver uma issue já existente, comente na issue que está trabalhando, caso ainda não exista uma issue crie uma nova issue descrevendo o problema encontrado e marque com a tag `documentação`.

Para solucionar faça um Pull Request com a descrição do que foi feito e a referência a issue que está resolvendo.

### Quer adicionar uma funcionalidade nova?

``` markdown
**Sua nova funcionalidade é relacionada com algum problema?**
Uma explicação limpa e concisa sobre o problema. Ex. Eu sempre fico frustrado com [...]

**Descreva solução para o problema**
Uma descrição rápida e simples de o que você queira que aconteça.
```
