def readFlags(file,tagToFind):
    flagFile = open(file,"r")
    flagFileText = flagFile.read()

    bracketDepth = 0
    isComment = True
    isTag = False
    tag = ""

    for i in range (0,len(flagFileText)):
        if (isComment):
            #is start of new line (hence is not a comment for next char)
            if flagFileText[i] == "\n":
                isComment = False
        elif flagFileText[i] == '#':
            isComment = True
        elif isComment == True:
            pass
        elif flagFileText[i] == '{':
            bracketDepth += 1
        elif flagFileText[i] == '}':
            bracketDepth -= 1
        # this means the next input text is a countries tag
        elif bracketDepth == 0 and flagFileText[i] != ' ' and flagFileText != '=' :
            tag = tag + flagFileText[i]
            isTag = True
        elif flagFileText[i] == '=':
            #found
            if tag.strip() == tagToFind:
                returnVal = ""
                for y in range (i,len(flagFileText)):
                    intial0 = True
                    if flagFileText[i] == "\n":
                        isComment = False
                    elif flagFileText[i] == '#':
                        isComment = True
                    elif flagFileText[i] == '{':
                        bracketDepth += 1
                        returnVal = returnVal + flagFile[i]
                        intial0 = False
                    elif flagFileText[i] == '}':
                        bracketDepth -= 1 
                        returnVal = returnVal + flagFile[i]
                    if bracketDepth == 0 and intial0 == False:
                        return returnVal
                    else:
                        returnVal = returnVal + flagFile[i]
            else:
                tag = ""
                isTag = False

print(readFlags("c:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game/common/flag_definitions/00_flag_definitions.txt","GBR"))