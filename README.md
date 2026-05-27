# Agente Inteligente de Triagem com Gemini API 
Este projeto consiste em um protótipo de agente inteligente voltado para a automação e otimização de processos internos de negócio. O script recebe e-mail de texto corrido (dados não estruturados), utilizando IA Generativa para interpretar o conexto e devolve um output estruturado em formato JSON contendo a prioridade do problema, o departamento de destino e um resumo executivo. 

## Tecnologias e Ferramentas 
- **Python 3**
- **Google GenAI SDK:** Biblioteca oficial para conexão com o modelo `gemini-2.5-flash`.
- **Variáveis de Ambiente (`os`):** Prática aplicada para gerenciamento seguro de credenciais.

## Boas Práticas e Segurança (Variáveis de Ambiente)
Visando seguir os padrões de seguranca de desenvolvimento e evitar o vazamento de credenciais em repositórios públicos, a chave de API da Google **não foi exposta de forma estática ( hardcoded) no código**. O script utiliza o método `os.environ.get()` para buscar a credencial diretamente da memória do sistema operacional em tempo de execução. 

## Como Executar o Projeto

1. Certifique-se de instalar a biblioteca oficial da Google:
```bash
pip install google-genai
```

2. Configure a sua chave de API temporária no terminal ( substituindo pelo seu token do Google AI Studio):
* No PowerShell: $env:GEMINI_API_KEY="SUA_CHAVE_AQUI"
* No Prompt de Comando (CMD): set GEMINI_API_KEY=SUA_CHAVE_AQUI
  
3. Execute a aplicação:
```bash
python app_agente.py
```




