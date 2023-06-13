def exists_word(word, instance):
    word = word.lower()
    exist = []

    for item in range(len(instance._data)):
        file = instance.search(item)
        filename = file["nome_do_arquivo"]
        lines = file["linhas_do_arquivo"]
        occurrences = []

        for line in range(len(lines)):
            if word in lines[line].lower():
                occurrences.append(line)

        if len(occurrences) > 0:
            exist.append(
                {
                    "palavra": word,
                    "nome_do_arquivo": filename,
                    "ocorrencias": occurrences,
                }
            )

    return exist


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
