import os

# --- BANCO DE DADOS TEMPORÁRIO ---
pecas_cadastradas = []
caixas_fechadas = []
caixa_atual = []
numero_caixa_atual = 1  # Rastreador do número da caixa

# --- FUNÇÕES DE UTILIDADE ---
def limpar_entrada(texto, unidade):
    return texto.lower().replace(unidade, "").strip()

def id_ja_existe(novo_id):
    for peca in pecas_cadastradas:
        if peca['id'] == novo_id and peca['id'] != "S/ID (Reprovada)":
            return True
    return False

def validar_qualidade(peso, cor, comprimento):
    motivos = []
    if not (95 <= peso <= 105):
        motivos.append("Peso fora da faixa")
    if cor not in ['azul', 'verde']:
        motivos.append("Cor inválida")
    if not (10 <= comprimento <= 20):
        motivos.append("Comprimento fora da faixa")
    return ("Aprovada", "") if not motivos else ("Reprovada", ". ".join(motivos))

# --- FUNÇÕES DO MENU ---
def cadastrar_peca():
    global numero_caixa_atual
    print("\n" + "-"*30 + "\n   NOVO CADASTRO\n" + "-"*30)
    id_temp = input("ID da peça: ").strip()
    
    if id_ja_existe(id_temp):
        print(f"⚠️ Erro: ID '{id_temp}' já em uso!")
        return
        
    try:
        peso = float(limpar_entrada(input("Peso (g): "), "g"))
        comp = float(limpar_entrada(input("Comprimento (cm): "), "cm"))
        cor = input("Cor (azul/verde): ").lower().strip()
    except ValueError:
        print("❌ Erro: Use apenas números!")
        return

    status, motivo = validar_qualidade(peso, cor, comp)
    
    # Se reprovada, não tem número de caixa (0)
    id_final = id_temp if status == "Aprovada" else "S/ID (Reprovada)"
    n_caixa = numero_caixa_atual if status == "Aprovada" else 0
    
    peca = {
        "id": id_final, 
        "peso": peso, 
        "cor": cor, 
        "comprimento": comp, 
        "status": status, 
        "motivo": motivo,
        "caixa": n_caixa # NOVO CAMPO
    }
    pecas_cadastradas.append(peca)

    if status == "Aprovada":
        caixa_atual.append(peca)
        print(f"✅ Peça {id_final} APROVADA e guardada na CAIXA {numero_caixa_atual}.")
        
        if len(caixa_atual) == 10:
            caixas_fechadas.append(caixa_atual.copy())
            caixa_atual.clear()
            print(f"📦 LOTE COMPLETO: Caixa {numero_caixa_atual} fechada!")
            numero_caixa_atual += 1 # Próxima caixa
    else:
        print(f"❌ REPROVADA: {motivo}")
        print(f"   (Dados digitados: {peso}g, {cor}, {comp}cm)")

def listar_pecas():
    print("\n" + "="*105)
    print(f"{'ID':<18} | {'STATUS':<10} | {'CAIXA':<7} | {'DADOS / MOTIVO'}")
    print("-" * 105)
    for p in pecas_cadastradas: 
        caixa_str = str(p['caixa']) if p['caixa'] > 0 else "-"
        if p['status'] == "Aprovada":
            detalhe = f"{p['peso']}g, {p['cor']}, {p['comprimento']}cm"
        else:
            detalhe = f"{p['motivo']} (Digitado: {p['peso']}g, {p['cor']}, {p['comprimento']}cm)"
        
        print(f"{p['id']:<18} | {p['status']:<10} | {caixa_str:<7} | {detalhe}")

def listar_caixas():
    print("\n" + "="*40 + "\n   INVENTÁRIO DE CAIXAS FECHADAS\n" + "="*40)
    if not caixas_fechadas:
        print("Nenhuma caixa foi fechada ainda.")
        return
    for i, caixa in enumerate(caixas_fechadas, 1):
        ids = [p['id'] for p in caixa]
        print(f"📦 CAIXA #{i}: {', '.join(ids)}")

def remover_peca():
    global pecas_cadastradas, caixa_atual
    aprovadas = [p for p in pecas_cadastradas if p['status'] == "Aprovada"]
    if not aprovadas:
        print("⚠️ Nenhum item no inventario.")
        return
    
    print("\nPeças Aprovadas no Sistema:")
    for p in aprovadas:
        print(f" -> ID: {p['id']} (Caixa: {p['caixa']})")
        
    alvo = input("\nID para remover: ").strip()
    inicial = len(pecas_cadastradas)
    pecas_cadastradas = [p for p in pecas_cadastradas if p['id'] != alvo]
    
    if len(pecas_cadastradas) < inicial:
        caixa_atual = [p for p in caixa_atual if p['id'] != alvo]
        print(f"✅ Registro {alvo} removido com sucesso.")
    else:
        print("⚠️ ID não encontrado.")

def gerar_relatorio():
    aprov = sum(1 for p in pecas_cadastradas if p['status'] == "Aprovada")
    repr = sum(1 for p in pecas_cadastradas if p['status'] == "Reprovada")
    print("\n" + "!"*45 + "\n      RELATÓRIO FINAL\n" + "!"*45)
    print(f"Registros: {len(pecas_cadastradas)}")
    print(f"Aprovadas: {aprov} | Reprovadas: {repr}")
    print(f"Caixas Despachadas: {len(caixas_fechadas)}")
    print(f"Peças na Caixa Atual ({numero_caixa_atual}): {len(caixa_atual)}/10")
    print("!"*45)

# --- LOOP PRINCIPAL ---
while True:
    print("\n" + "#"*40 + "\n   INVENTÁRIO DE QUALIDADE\n" + "#"*40)
    print("1. Cadastrar Peça")
    print("2. Listar Histórico (Ver Caixas)")
    print("3. Remover Peça")
    print("4. Ver Conteúdo das Caixas Fechadas")
    print("5. Relatório Geral")
    print("0. Sair")
    
    op = input("\nEscolha: ")
    if op == "1": cadastrar_peca()
    elif op == "2": listar_pecas()
    elif op == "3": remover_peca()
    elif op == "4": listar_caixas()
    elif op == "5": gerar_relatorio()
    elif op == "0": 
        print("Saindo... Bom trabalho!")
        break
    else:
        print("Opção inválida.")