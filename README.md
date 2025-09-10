📊 Analisador de Texto Simples
Um analisador de texto básico em Python que fornece estatísticas textuais de maneira rápida e eficiente.

✨ Funcionalidades
✅ Contagem de palavras - Quantidade total de palavras no texto

✅ Contagem de caracteres - Total de caracteres (incluindo espaços)

✅ Contagem de frases - Identifica frases baseado em pontuação (. ! ?)

✅ Palavra mais frequente - Encontra a palavra que mais aparece no texto

🚀 Como Usar
Pré-requisitos
Python 3.6 ou superior instalado

Git para clonar o repositório

Instalação e Execução
Clone este repositório:

bash
git clone https://github.com/DavidMiguelvs/analisador-texto.git
Acesse a pasta do projeto:

cd analisador-texto
Execute o analisador:

python analisador.py
Como Usar em Seu Próprio Código
python
from analisador import analisar_texto

seu_texto = "Olá! Este é um texto de exemplo. O analisador vai processar este texto."
resultado = analisar_texto(seu_texto)

print(f"Palavras: {resultado['palavras']}")
print(f"Caracteres: {resultado['caracteres']}")
print(f"Frases: {resultado['frases']}")
print(f"Palavra mais frequente: '{resultado['palavra_mais_frequente']}'")
print(f"Frequência: {resultado['frequencia']} vezes")
📝 Exemplo de Saída
text
📊 RESULTADO DA ANÁLISE:
► Palavras: 15
► Caracteres: 78
► Frases: 3
► Palavra mais frequente: 'texto' (3 vezes)
🛠️ Tecnologias Utilizadas
Python 3.x - Linguagem de programação principal

Git - Controle de versão

GitHub - Hospedagem do repositório

📦 Estrutura do Projeto
text
analisador-texto/
├── analisador.py    # Código principal do analisador
├── README.md        # Documentação do projeto

🤝 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para:

Fazer um fork do projeto

Criar uma branch para sua feature (git checkout -b feature/nova-feature)

Commitar suas mudanças (git commit -m 'Adiciona nova feature')

Fazer push para a branch (git push origin feature/nova-feature)

Abrir um Pull Request

Melhorias Possíveis
Adicionar interface gráfica

Implementar análise de sentimentos

Adicionar suporte a mais idiomas

Criar interface web com Flask

Adicionar estatísticas avançadas

📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

👨‍💻 Autor
DAVID MIGUEL - davidmiguel.vs@gmail.com

⭐️ Se este projeto foi útil, deixe uma estrela no repositório!
