#addes new name to localisation file (.yml)
def addLoc(file,tag,name,adj):
    locFile = open(file,"a" )
    writeVal = "\n gov_exile_" + tag + ": \"" + name + "\"\n " + "gov_exile_" + tag + "_adj: \"" + adj + "\""
    print (writeVal)
    locFile.write(writeVal)
    locFile.close

#addes the new name to be associated with the GIE
def addDynName(file,tag):
    dynNameFile = open(file,"r")
    writeVal = "\n\tdynamic_country_name = {" + "\n\t\tname = gov_exile_" + tag + "\n\t\tadjective = gov_exile_" + tag + "_adj" + "\n\t\tpriority = 1000" + "\n\t\ttrigger ={" + "\n\t\t\texists = scope:actor" + "\n\t\t\tscope:actor ?= {" + "\n\t\t\t\thas_variable = gov_exile_" + tag + "\n\t\t\t\thas_journal_entry = je_gie_africa_union" + "\n\t\t\t}" + "\n\t\t}" + "\n\t}\n"
    print(writeVal)
    dynNameFileText = dynNameFile.read()
    finalClose = dynNameFileText.rindex("}")
    dynNameFile.close
    dynNameFile = open(file,"w")
    writeVal = dynNameFileText[0:finalClose] + writeVal + dynNameFileText[finalClose:len(dynNameFileText)]
    dynNameFile.write(writeVal)
    print(writeVal)
    dynNameFile.close

# def freeName(file,tag):
#     name = input("Enter the name for the GIE:")



def readFlags(file,tagToFind):
    flagFile = open(file,"r")
    flagFileText = flagFile.read()

    isComment = True

    endOfVarDef = 0

    #skips var deines
    for z in range (0,len(flagFileText)):
        if (isComment):
            #is start of new line (hence is not a comment for next char)
            if flagFileText[z] == '\n':
                isComment = False
        elif flagFileText[z] == '#' or flagFileText[z] == '@':
            isComment = True
        if (isComment == False and flagFileText[z] != '\n' and flagFileText[z] != ' '):
            endOfVarDef = z
            break
     

    bracketDepth = 0
    isTag = False
    tag = ""

    for i in range (endOfVarDef,len(flagFileText)):
        debugBuff = flagFileText[i:i+100]
        debugChar = flagFileText[i]
        if (isComment):
            #is start of new line (hence is not a comment for next char)
            if flagFileText[i] == '\n':
                isComment = False
        # # is the comments it is skiped until new line
        elif flagFileText[i] == '#':
            isComment = True
        elif flagFileText[i] == '{':
            bracketDepth = bracketDepth + 1
        elif flagFileText[i] == '}':
            bracketDepth = bracketDepth - 1
        # this means the next input text is a countries tag
        elif bracketDepth == 0 and flagFileText[i] != ' ' and flagFileText[i] != '=' and flagFileText[i] != '\n':
            tag = tag + flagFileText[i]
            isTag = True
        elif flagFileText[i] == '=' and isTag == True:
            #found
            if tag.strip() == tagToFind:

                returnVal = ""
                intial0 = True
                for y in range (i,len(flagFileText)):
                    if flagFileText[y] == "\n":
                        isComment = False
                    elif flagFileText[y] == '#':
                        isComment = True
                    elif flagFileText[y] == '{':
                        bracketDepth += 1
                        intial0 = False
                    elif flagFileText[y] == '}':
                        bracketDepth -= 1 
                    if bracketDepth == 0 and intial0 == False:
                        return returnVal
                    else:
                        returnVal = returnVal + flagFileText[y]
            else:
                tag = ""
                isTag = False
addLoc("testLoc.yml","PRU","Free Prussia","Free Prussian")
addDynName("testDynName.txt","pru")
#print(readFlags("c:/Program Files (x86)/Steam/steamapps/common/Victoria 3/game/common/flag_definitions/00_flag_definitions.txt","GBR"))