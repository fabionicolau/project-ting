def exists_word(word, instance):
    processed_datas_with_word = list()
    occurrences = list()
    file_name = ""

    for index in range(0, len(instance.queue) + 1):
        if len(occurrences) > 0:
            processed_datas_with_word.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )
        if index <= len(instance.queue) - 1:
            file = instance.queue[index]
        occurrences = list()
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                file_name = file["nome_do_arquivo"]
                occurrences.append({"linha": index + 1})

    return processed_datas_with_word


def search_by_word(word, instance):
    processed_datas_with_word = list()
    occurrences = list()
    file_name = ""

    for index in range(0, len(instance.queue) + 1):
        if len(occurrences) > 0:
            processed_datas_with_word.append(
                {
                    "palavra": word,
                    "arquivo": file_name,
                    "ocorrencias": occurrences,
                }
            )
        if index <= len(instance.queue) - 1:
            file = instance.queue[index]
        occurrences = list()
        for index, line in enumerate(file["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                file_name = file["nome_do_arquivo"]
                occurrences.append({"linha": index + 1, "conteudo": line})

    return processed_datas_with_word
