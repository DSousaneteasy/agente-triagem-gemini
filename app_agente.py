#chamando as ferramentas do google para executar os comandos 
import os 
from google import genai 
from google.genai import types

API_KEY = os.environ.get("GEMINI_API_KEY","") #busca a variavel localmente (no os)

if not API_KEY:
    print("ERRO CRÍTICO: A variável de ambiente 'GEMINI_API_KEY' não foi encontrada!")
    print("Por favor, configure a variável no seu terminal antes de rodar o script.")
    exit(1)
  #Conexão  com o serviço do google 
  
client = genai.Client(api_key=API_KEY)

def triagem_automacao_chamado(texto_chamado): #Regras de funcionalidade ( limitação da funcionalidade da IA)
    contexto_agente = (
        "Você é um agente inteligente de triagem de processos internos de uma empresa."
        "Sua função é ler o chamado de um cliente ou funcionário e retornar um JSON estrito com três campos: "
        "1. 'prioridade': (valores possíveis: Alta, Média, Baixa)"
        "2. 'departamento_destino': (valores possíveis: Tech, RH, Comercial, Financeiro, Marketing)."
        "3. 'resumo_executivo': um resumo de apenas uma frase sobre o problema."
        "Seja estrito, retorne APENAS o JSON, sem textos adicionais antes ou depois"
    )
    try:
        #CHAMANDO A API USANDO A GEMINI MODELO FLASH 2.5
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=texto_chamado,
            config=types.GenerateContentConfig(
                system_instruction=contexto_agente,
                response_mime_type="application/json" 
                # me certificando do retorno em JSON
            ),
        )
        return response.text
    except Exception as e:
        return f"Erro ao conectar com a API: {e}"
#SIMULANDO A AUTOMAÇÃO 
if __name__ == "__main__":
    print("\n==============================================")
    print("INICIANDO AGENTE INTELIGENTE DE TRIAGEM")
    print("==============================================\n")

    #SIMULANDO UM CHAMADO REAL COM PROBLEMAS 
    chamado_exemplo = (
        "Prezado, sou do setor Comercial e estou desde ontem tentando acessar o sistema"
        "de identificação dos profissionais para fechar um contrato importante com um cliente, mas a página fica dando"
        "erro de conexão de banco de dados e preciso disso resolvido urgentemente!"
    )

    print(f"[Texto Recebido do Cliente]:\n\"{chamado_exemplo}\"\n")
    print("Enviando para análise de IA Gemini...")
    print("-"*46)

    #CHAMANDO A FUNÇÃO CRIADA ANTERIOMENTE  
    resultado_json = triagem_automacao_chamado(chamado_exemplo)

    print("\n[resultado Estruturado (JSON) retornando para o sistema]:")
    print(resultado_json)
    print("==============================================")
