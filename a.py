eleitores = []


while True:
    nome = input("Digite o nome do eleitor: ")
    cpf = input("Digite o CPF do eleitor (somente números): ")
    if len(cpf) != 11:
        print("Número de CPF inválido, tente novamente.")
        cpf = input("Digite o CPF do eleitor (somente números): ")
        eleitores.append({'Eleitor': nome, 'CPF': cpf})
    else:
        eleitores.append({'Eleitor': nome, 'CPF': cpf})

    opcao = input("Deseja cadastrar outro eleitor? (S/N) ")
    if opcao.upper() == "N" or opcao.lower() == "n":
        break


candidatos_presidente = []
candidatos_governador = []
candidatos_prefeito = []


while True:
    nome = input("Digite o nome do candidato: ")
    numero = input("Digite o número do candidato: ")
    partido = input("Digite o partido do candidato: ")
    cargo = input("Digite o cargo que o candidato disputa (P = Presidente, G = Governador, F = Prefeito): ")

    if cargo.upper() == "P" or cargo.lower() == "p":
        candidatos_presidente.append({"Nome": nome, "Numero": numero, "Partido": partido, "Votos": 0})
    elif cargo.upper() == "G" or cargo.lower() == "g":
        candidatos_governador.append({"Nome": nome, "Numero": numero, "Partido": partido, "Votos": 0})
    elif cargo.upper() == "F" or cargo.lower() == "f":
        candidatos_prefeito.append({"Nome": nome, "Numero": numero, "Partido": partido, "Votos": 0})
    else:
        print("Cargo inválido. Tente novamente.")
        continue

    continuar = input("Deseja cadastrar outro candidato? (S/N) ")
    if continuar.upper() == "N" or continuar.lower() == "n":
        break

    votos_branco_pref = 0
    votos_nulo_pref = 0

    votos_nulo_gov = 0
    votos_branco_gov = 0

    votos_nulo_pres = 0
    votos_branco_pres = 0

while True:
    votos = 0
    votou = False
    print("---- Voto para Prefeito ----")
    voto = int(input("Digite o número do candidato \n"
                     "-1 para voto branco\n"
                     "-2 para voto nulo\n"
                     " "))
    if not (voto == -1 or voto == -2):
        for candidato in candidatos_prefeito:
            if voto == int(candidato["Numero"]):
                print("Candidato:", candidato["Nome"])
                print("Partido:", candidato["Partido"])
                conf_pref = input(f"Digite S para confirmar seu voto no candidato apresentado\n"
                                  f"ou N para retornar a votação de Prefeito. ")
                if conf_pref.upper() == "S":
                    candidato["Votos"] += 1
                    votos += 1
                    votou = True
                    break
                else:
                    break
    elif voto == -1:
           conf_pref_branco = input("Digite S para confirmar seu voto em branco\n"
                                    "ou N para retornar a votação de Prefeito.")
        if conf_pref_branco.upper() == "S":
            votos_branco_pref += 1
            votou = True
            break
    elif voto == -2:
        conf_pref_nulo = input(("Digite S para confirmar seu voto nulo\n"
                                    "ou N para retornar a votação de Prefeito. "))
        if conf_pref_nulo.upper() == "S":
            votos_nulo_pref += 1
            votou = True
            break

    if votou:
        break
    else:
        print("Voto inválido. Tente novamente.")

while True:
    votos = 0
    votou = False
    print("---- Voto para Governador ----")
    voto = int(input("Digite o número do candidato \n"
                        "-1 para voto branco\n"
                        "-2 para voto nulo\n"
                        " "))
    if not (voto == -1 or voto == -2):
        for candidato in candidatos_governador:
            if voto == int(candidato["Numero"]):
                print("Candidato:", candidato["Nome"])
                print("Partido:", candidato["Partido"])
                conf_gov = input(f"Digite S para confirmar seu voto no candidato apresentado\n"
                                        f"ou N para retornar a votação de Governador. ")
                if conf_gov.upper() == "S":
                    candidato["Votos"] += 1
                    votos += 1
                    votou = True
                    break
                else:
                    break
    elif voto == -1:
        conf_gov_branco = input("Digite S para confirmar seu voto em branco\n"
                                        "ou N para retornar a votação de Governador. ")
        if conf_gov_branco.upper() == "S":
            votos_branco_gov += 1
            votou = True
            break
    elif voto == -2:
        conf_gov_nulo = input(("Digite S para confirmar seu voto nulo\n"
                                    "ou N para retornar a votação de Governador. "))
        if conf_gov_nulo.upper() == "S":
            votos_nulo_gov += 1
            votou = True
            break

    if votou:
        break
    else:
        print("Voto inválido. Tente novamente.")

while True:
    votos = 0
    votou = False
    print("---- Voto para Presidente ----")
    voto = int(input("Digite o número do candidato \n"
                        "-1 para voto branco\n"
                        "-2 para voto nulo\n"
                        " "))
    if not (voto == -1 or voto == -2):
        for candidato in candidatos_presidente:
            if voto == int(candidato["Numero"]):
                print("Candidato:", candidato["Nome"])
                print("Partido:", candidato["Partido"])
                conf_pres = input(f"Digite S para confirmar seu voto no candidato apresentado\n"
                                    f"ou N para retornar a votação de Presidente. ")
                if conf_pres.upper() == "S":
                    candidato["Votos"] += 1
                    votos += 1
                    votou = True
                    break
                else:
                    break
    elif voto == -1:
        conf_pres_branco = input("Digite S para confirmar seu voto em branco\n"
                                "ou N para retornar a votação de Presidente. ")
        if conf_pres_branco.upper() == "S":
            votos_branco_pres += 1
            votou = True
            break
    elif voto == -2:
        conf_pres_nulo = input(("Digite S para confirmar seu voto nulo\n"
                                "ou N para retornar a votação de Presidente. "))
        if conf_pres_nulo.upper() == "S":
            votos_nulo_pres += 1
            votou = True
            break

    if votou:
        break
    else:
        print("Voto inválido. Tente novamente.")


vencedor_presidente = None
vencedor_governador = None
vencedor_prefeito = None


resultado_presidente = []
resultado_governador = []
resultado_prefeito = []


total_votos_presidente = sum([candidato["Votos"] for candidato in candidatos_presidente])
total_votos_governador = sum([candidato["Votos"] for candidato in candidatos_governador])
total_votos_prefeito = sum([candidato["Votos"] for candidato in candidatos_prefeito])

for candidato in candidatos_presidente:
    percentual_votos = candidato["Votos"] / total_votos_presidente * 100 if total_votos_presidente > 0 else 0
    resultado_presidente.append((candidato["Nome"], candidato["Votos"], percentual_votos))

for candidato in candidatos_governador:
    percentual_votos = candidato["Votos"] / total_votos_governador * 100 if total_votos_governador > 0 else 0
    resultado_governador.append((candidato["Nome"], candidato["Votos"], percentual_votos))

for candidato in candidatos_prefeito:
    percentual_votos = candidato["Votos"] / total_votos_prefeito * 100 if total_votos_prefeito > 0 else 0
    resultado_prefeito.append((candidato["Nome"], candidato["Votos"], percentual_votos))

resultado_presidente = sorted(resultado_presidente, key=lambda x: x[1], reverse=True)
vencedor_presidente = resultado_presidente[0][0] if resultado_presidente else None

resultado_governador = sorted(resultado_governador, key=lambda x: x[1], reverse=True)
vencedor_governador = resultado_governador[0][0] if resultado_governador else None

resultado_prefeito = sorted(resultado_prefeito, key=lambda x: x[1], reverse=True)
vencedor_prefeito = resultado_prefeito[0][0] if resultado_prefeito else None

print("Resultados da Eleição")

# Vencedores
print("Vencedor da Eleição para Presidente:", vencedor_presidente)
print("Vencedor da Eleição para Governador:", vencedor_governador)
print("Vencedor da Eleição para Prefeito:", vencedor_prefeito)

# Ranking
print("Ranking da Eleição")

if resultado_presidente:
    print("\nPresidente")
    print("{:<20} {:<15} {:<15} {:<15}".format("Nome", "Total de votos", "Votos válidos", "% Válidos"))
    for candidato in resultado_presidente:
        total_votos = candidato['votos'] + votos_branco_pres + votos_nulo_pres
        votos_validos = candidato['votos']
        perc_validos = votos_validos / (total_votos - votos_branco_pres) * 100 if total_votos - votos_branco_pres > 0 else 0
        print("{:<20} {:<15} {:<15} {:.2f}%".format(candidato['nome'], total_votos, votos_validos, perc_validos))
    print("\nTotal de votos =", total_votos)
    print("Total de votos válidos e % = {} {:.2f}%".format(votos_validos, perc_validos))
    print("Total de brancos e % =", votos_branco_pres, "{:.2f}%".format(votos_branco_pres / total_votos * 100))
    print("Total de nulos e % =", votos_nulo_pres, "{:.2f}%".format(votos_nulo_pres / total_votos * 100))

if resultado_governador:
    print("\nGovernador")
    print("{:<20} {:<15} {:<15} {:<15}".format("Nome", "Total de votos", "Votos válidos", "% Válidos"))
    for candidato in resultado_governador:
        total_votos = candidato['votos'] + votos_branco_gov + votos_nulo_gov
        votos_validos = candidato['votos']
        perc_validos = votos_validos / (total_votos - votos_branco_gov) * 100 if total_votos - votos_branco_gov > 0 else 0
        print("{:<20} {:<15} {:<15} {:.2f}%".format(candidato['nome'], total_votos, votos_validos, perc_validos))
    print("\nTotal de votos =", total_votos)
    print("Total de votos válidos e % = {} {:.2f}%".format(votos_validos, perc_validos))
    print("Total de brancos e % =", votos_branco_gov, "{:.2f}%".format(votos_branco_gov / total_votos * 100))
    print("Total de nulos e % =", votos_nulo_gov, "{:.2f}%".format(votos_nulo_gov/ total_votos * 100))

if resultado_prefeito:
    print("\nPrefeito")
    print("{:<20} {:<15} {:<15} {:<15}".format("Nome", "Total de votos", "Votos válidos", "% Válidos"))
    for candidato in resultado_prefeito:
        total_votos = candidato['votos'] + votos_branco_pref + votos_nulo_pref
        votos_validos = candidato['votos']
        perc_validos = votos_validos / (total_votos - votos_branco_pref) * 100 if total_votos - votos_branco_pref > 0 else 0
print("{:<20} {:<15} {:<15} {:.2f}%".format(candidato['nome'], total_votos, votos_validos, perc_validos))
print("\nTotal de votos =", total_votos)
print("Total de votos válidos e % = {} {:.2f}%".format(votos_validos, perc_validos))
print("Total de brancos e % =", votos_branco_pref, "{:.2f}%".format(votos_branco_pref / total_votos * 100))
print("Total de nulos e % =", votos_nulo_pref, "{:.2f}%".format(votos_nulo_pref / total_votos * 100))




