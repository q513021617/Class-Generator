''' ----- Globals ----- '''

folderPath = "./Output/"
fileType = ".java"

keywords = ["boolean", "double", "byte", "int", "short", "char", "long",
            "float", "continue", "break", "class", "enum", "import", "package",
            "super", "switch", "if", "throw", "else", "throws", "case", "try",
            "catch", "finally", "default", "assert", "instanceof", "return",
            "goto", "const", "abstract", "new", "public", "protected",
            "private", "final", "this", "static", "void", "volatile",
            "interface", "implements", "extends", "synchronized", "native",
            "strictfp", "transient", "for", "while", "do"]

variableTypes = ["boolean", "double", "byte", "int", "short", "char", "long",
                "float", "string", "boolean[]", "double[]", "byte[]", "int[]",
                "short[]", "char[]", "long[]", "float[]", "string[]"]

''' ----- Functions to create the class file ----- '''

def closeOffClass():
    return "}\n"

def createClone(classname, args):
    clone = "\tpublic " + classname + " clone()\n\t{\n\t\t" + classname + \
            " new" + classname.title() + " = new " + classname + "("

    for i in range(1, len(args), 2):
        if i + 1 == len(args):
            clone = clone + args[i]
        else:
            clone = clone + args[i] + ", "

    clone = clone + ")\n\t\treturn new" + classname.title() + ";\n\t}\n\n"

    return clone

def createToString(classname, args = None):
    toString = "\tpublic string toString()\n\t{\n\t\treturn \"" + classname + ": "

    if args is not None:
        for i in range(1, len(args), 2):
            if i + 1 == len(args):
                toString = toString + args[i] + " = \" " + "+ " + args[i]
            else:
                toString = toString + args[i] + " = \" " + "+ " + args[i] + " + \", "

    toString = toString + ";\n\t}\n\n"

    return toString

def createGetters(args):
    getters = ""

    for i in range(0, len(args), 2):
        getters = getters + "\tpublic " + args[i] + " get" + \
                            args[i + 1].title() + "()\n\t{\n\t\treturn " + \
                            args[i + 1] + ";\n\t}\n\n"

    return getters

def createSetters(args):
    setters = ""

    for i in range(0, len(args), 2):
        setters = setters + "\tpublic void set" + args[i + 1].title() + "(" + \
                          args[i] + " " + args[i + 1] + ")\n\t{\n\t\tthis." +  \
                          args[i + 1] + " = " + args[i + 1] + ";\n\t}\n\n"

    return setters

def createConstructor(classname, args = None):
    constructor = ""

    if args is None:
        constructor = "\tpublic " + classname + "()\n\t{\n\n"
    else:
        constructor = "\tpublic " + classname + "("

        for i in range(0, len(args)):
            if isVariableType(args[i]):
                constructor = constructor + args[i] + " "
            elif i + 1 == len(args):
                constructor = constructor + args[i]
            else:
                constructor = constructor + args[i] + ", "

        constructor = constructor + ")\n\t{\n"

        for value in args:
            if not isVariableType(value):
                constructor = constructor + "\t\tthis." + value + " = " + value + ";\n"

    constructor = constructor + "\t}\n\n"

    return constructor

def createVariables(args):
    variables = ""

    for value in args:
        if isVariableType(value):
            variables = variables + "\tprivate " + value
        else:
            variables = variables + " " + value + ";\n"

    variables = variables + "\n"

    return variables

def startOffClass(classname, extends, implements):
    start = "public class " + classname

    if extends != "has been left out":
        start = start + " extends " + extends

    if implements != "has been left out":
        start = start + " implements " + implements

    start = start + "\n{\n\n"

    return start

''' ----- Driver for class creation ----- '''

def createClassDriver(options, args):
    classFile = open(folderPath + options.classname + fileType, "w+")

    start = startOffClass(options.classname, options.extends, options.implements)
    classFile.write(start)

    variables = createVariables(args)
    classFile.write(variables)

    constructor = createConstructor(options.classname)
    classFile.write(constructor)

    if len(args) != 0:
        constructor = createConstructor(options.classname, args)
        classFile.write(constructor)

        if options.setters:
            setters = createSetters(args)
            classFile.write(setters)

        if options.getters:
            getters = createGetters(args)
            classFile.write(getters)

        if options.toString:
            toString = createToString(options.classname, args)
            classFile.write(toString)

        if options.clone:
            clone = createClone(options.classname, args)
            classFile.write(clone)

    end = closeOffClass()
    classFile.write(end)

    classFile.close()

''' ----- Input validation ----- '''

def isVariableType(var):
    return var in variableTypes

def isKeyword(word):
    return word in keywords

def argsChecks(args):
    if len(args) == 0:
        return

    if len(args) % 2 != 0:
        print "Exiting: There is an odd amount of arguments"
        sys.exit();

    for i in range(0, len(args)):
        if i % 2 != 0:
            if isKeyword(args[i]):
                print "Exiting: " + args[i] + " is a keyword"
                sys.exit()
        else:
            if not isVariableType(args[i]):
                print "Exiting: " + args[i] + " not a proper variable type"
                sys.exit()

def optionChecks(options):
    if options.classname == "has been left out":
        print "Exiting: Classname has been left out"
        sys.exit()

    if isKeyword(options.classname):
        print "Exiting: Classname, " + options.classname + ", is a keyword"
        sys.exit()

''' ----- Driver ----- '''

def javaClassDriver(options, args):
    argsChecks(args)
    optionChecks(options)

    print "Valid input"

    print "Generating " + options.classname + "." + options.language + " file"

    createClassDriver(options, args)

    print "File, " + folderPath + options.classname + fileType + ", has been created"
