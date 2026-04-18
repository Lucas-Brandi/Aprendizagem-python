import statistics

# Definição do local dos arquivos
FOLDER = "swimdata/"

def read_swim_data(filename):
    """
    Lê os dados do arquivo especificado, converte os tempos,
    calcula a média e formata o resultado.
    """
    # Extrai os dados do nome do arquivo (Darius, 13, 100m, Fly)
    swimmer, age, distance, stroke = filename.removesuffix(".txt").split("-")

    # Abre o arquivo dentro da pasta definida e lê a primeira linha
    with open(FOLDER + filename) as file:
        lines = file.readlines()
        times = lines[0].strip().split(",")

    # Converte os tempos (M:SS.hh) para centésimos de segundo (total_centis)
    converts = []
    for t in times:
        minutes, rest = t.split(":")
        seconds, hundredths = rest.split(".")
        # Cálculo: (minutos * 6000) + (segundos * 100) + centésimos
        total_centis = (int(minutes) * 6000) + (int(seconds) * 100) + int(hundredths)
        converts.append(total_centis)

    # Calcula a média aritmética dos tempos convertidos
    average_raw = statistics.mean(converts)

    # Converte a média de volta para o formato M:SS.hh
    # 1. Calcula os minutos
    minutes_avg = int(average_raw // 6000)
    # 2. Calcula os segundos restantes
    seconds_avg = int((average_raw % 6000) // 100)
    # 3. Calcula os centésimos restantes
    hundredths_avg = int(average_raw % 100)

    # Formata a string final garantindo dois dígitos para segundos e centésimos
    average_str = f"{minutes_avg}:{seconds_avg:02d}.{hundredths_avg:02d}"

    # Retorna um dicionário ou tupla com os resultados processados
    return {
        "Atleta": swimmer,
        "Idade": age,
        "Prova": f"{distance} {stroke}",
        "Tempos": times,
        "Media": average_str
    }


FN = "Darius-13-100m-Fly.txt"
resultado = read_swim_data(FN)


print(f"Nadador: {resultado['Atleta']}")
print(f"Prova: {resultado['Prova']}")
print(f"Tempos registrados: {resultado['Tempos']}")
print(f"Tempo Médio calculado: {resultado['Media']}")