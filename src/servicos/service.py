import json
import os
from datetime import datetime


DATA_FILE = "pacientes.json"


# ESSA FUNCAO É RESPONSÁVEL POR CARREGAR OS DADOS DO ARQUIVO JSON E FORMATAR A DATA DE ACORDO COM O PADRÃO ISO
def formatar_data(data_str):   

    try:
        return datetime.strptime(data_str, "%d/%m/%Y").date().isoformat()
    except Exception:
        return "Data inválida"






# Função para salvar os dados no arquivo JSON . # FORMATANDO DE MANEIRA QUE ESTA NÃO QUEBRE A ESTRUTURA DO JSON  A PARTIR DO ARQUIVO FICHAADD
def formatar_paciente(
    nome,
    data_admissao,
    data_nasc,
    idade,
    escola,
    endereco,
    responsavel,
    contato,
    respostas
):
    paciente = {
        "nome": nome.strip(),
        "data_admissao": formatar_data(data_admissao),
        "data_nascimento": formatar_data(data_nasc),
        "idade_cronologica": idade.strip(),
        "escola": escola.strip(),
        "endereco": endereco.strip(),
        "responsavel": responsavel.strip(),
        "contato": contato.strip(),
        "referencias_musicais": {
            "preferencias_responsaveis": respostas.get("q1", "").strip(),
            "vivencias_gestacao": respostas.get("q2", "").strip(),
            "vivencias_pos_nascimento": respostas.get("q3", "").strip(),
            "preferencias_crianca": respostas.get("q4", "").strip(),
            "experiencia_musical": respostas.get("q5", "").strip(),
            "familiares_musicistas": respostas.get("q6", "").strip(),
            "instrumentos_em_casa": respostas.get("q7", "").strip(),
            "envolvimento_musical": respostas.get("q8", "").strip(),
        },
        "referencias_gerais": {
            "deficiencia_ou_doenca": respostas.get("q9", "").strip(),
            "uso_medicamento": respostas.get("q10", "").strip(),
            "alergia": respostas.get("q11", "").strip(),
            "dificuldade": respostas.get("q12", "").strip(),
            "intervencoes": respostas.get("q13", "").strip(),
            "hiperfoco": respostas.get("q14", "").strip(),
        },
        "data_registro": datetime.now().isoformat()
    }
    return paciente    


def salvar_paciente(paciente):
    pacientes = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            try:
                pacientes = json.load(file)  # possivel erro aqui
            except Exception:
                pacientes = []
    pacientes.append(paciente)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(pacientes, file, ensure_ascii=False, indent=2)

def listar_pacientes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except Exception:
            return []


def buscar_paciente(nome):
    pacientes = listar_pacientes()
    for paciente in pacientes:
        return[p for p in pacientes if p["nome"].lower() == nome.lower()]              


    