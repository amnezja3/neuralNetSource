def brain(witch):
    witch = str(witch)
    if witch == 'brain': 
        MAIN_FILE_BRAIN = 'brain.neural'
        return MAIN_FILE_BRAIN
    if witch == 'wiki': 
        TMP_FILE_WIKI = 'filter_wiki.recognizer'
        return TMP_FILE_WIKI

def clearCharacters(quest):
    quest = str(quest)
    quest = quest.replace('?', '').replace('.', '').replace('..', '').replace('...', '').replace(',', '').replace('!', '').replace('$', '').replace('\r', '').replace('\t', '').replace('\n', '').replace('-', ' ').replace('+', ' ').replace('*', ' ').replace('/', ' ').replace('#', '').replace('@', '').replace(':', ' ').replace(';', '').replace("'", '').replace("(", '').replace(")", '').replace("[", '').replace("]", '').replace("{", '').replace("}", '').replace("«", '').replace("»", '').replace('\xe0', '').replace('\xc5', '').replace('\u03bc', '').replace('\u03bc', '').lower()
    return quest