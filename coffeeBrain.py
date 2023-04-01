def coffeePls(update = True):
    import config

    BRAIN_FILE_ADDRESS = str(config.brain('brain'))

    try:brainFile = open(BRAIN_FILE_ADDRESS, 'r+')
    except:brainFile = open(BRAIN_FILE_ADDRESS, 'a+')
    finally:brainFile = open(BRAIN_FILE_ADDRESS, 'r+')
    allBrain = brainFile.readlines()
    brainFile.close()

    questionBase = {}
    explainBase = {}
    commandBase = {}
    wordBase = {}
    meaningBase = {}


    SEP_GENERAL = ':'
    SEP_SPLIT = ';'
    SEP_PART = '|'
    SEP_NUM = '^'
    SEP_TITLE = '#'

    INDEX_QUESTION = 'question:'
    INDEX_EXPLAIN = 'explain:'
    INDEX_COMMAND = 'command:'
    INDEX_WORD = 'word:'
    INDEX_MEANING = 'meaning:'

    for a in allBrain:
        a = a.strip()
        question = a.startswith('question:')
        explain = a.startswith('explain:')
        command = a.startswith('command:')
        word = a.startswith('word:')
        meaning = a.startswith('meaning:')

        if question:
            a = str(a).strip().replace('question:', '')
            aa = a.split(SEP_PART)
            questionBase[aa[0]] = aa[1]
        if explain:
            print('explain: ');print(a)
        if command:
            a = str(a).strip().replace('command:', '')
            aa = a.split(SEP_PART)
            commandBase[aa[0].strip()] = aa[1]            
        if word:
            a = str(a).strip().replace('word:', '')
            aa = a.split(SEP_PART)
            wordBase[aa[0].strip()] = aa[1]
        if meaning:        
            a = str(a).strip().replace('meaning:', '')
            aa = a.split(SEP_PART)
            meaningBase[aa[0].strip()] = aa[1]


    if update:
        file = open(BRAIN_FILE_ADDRESS, 'w+')
        for k1, v1 in commandBase.items():
            file.write(INDEX_COMMAND + str(k1) + SEP_PART + str(v1) + '\n')
        file.close()

        file = open(BRAIN_FILE_ADDRESS, 'a+')
        for k2, v2 in questionBase.items():
            file.write(INDEX_QUESTION + str(k2) + SEP_PART + str(v2) + '\n')
        file.close()

        file = open(BRAIN_FILE_ADDRESS, 'a+')
        for k1, v1 in wordBase.items():
            file.write(INDEX_WORD + str(k1) + SEP_PART + str(v1) + '\n')
        file.close()

        file = open(BRAIN_FILE_ADDRESS, 'a+')
        for k, v in meaningBase.items():
            file.write(INDEX_MEANING + str(k) + SEP_PART + str(v) + '\n')
        file.close()
    

    return commandBase, questionBase, wordBase, meaningBase
    # print(meaningBase['co'])
    


# coffeePls()