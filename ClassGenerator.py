''' ----- Imports ----- '''

import sys
from optparse import OptionParser
from JavaClass import javaClassDriver
from CppClass import cppClassDriver

''' ----- Globals ----- '''

languages = ["java", "cpp"]

''' ----- Language validation and choosing ----- '''

def pickLanguage(options, args):
    if options.language == "java":
        javaClassDriver(options, args)
    elif options.language == "cpp":
        cppClassDriver(options, args)

def isLanguage(language):
    if language not in languages:
        print "Exiting: Language, " + language + ", is not a language"
        sys.exit()

''' ----- Parser Rules ----- '''

def buildParser():
    parser = OptionParser()

    parser.add_option("-g", "--getters",
                      action = "store_true", dest = "getters")
    parser.add_option("-s", "--setters",
                      action = "store_true", dest = "setters")
    parser.add_option("-t", "--toString",
                     action = "store_true", dest = "toString")
    parser.add_option("-k", "--clone",
                      action = "store_true", dest = "clone")
    parser.add_option("-e", "--extends",
                      action = "store", type = "string",
                      dest = "extends", default = "has been left out")
    parser.add_option("-i", "--implements",
                      action = "store", type = "string",
                      dest = "implements", default = "has been left out")
    parser.add_option("-c", "--classname",
                     action = "store", type = "string",
                     dest = "classname", default = "has been left out")
    parser.add_option("-l", "--language",
                      action = "store", type = "string",
                      dest = "language", default = "java")

    return parser

''' ----- Main ----- '''

def main(argv):
    parser = buildParser()
    (options, args) = parser.parse_args(argv)

    isLanguage(options.language)

    pickLanguage(options, args)

    print "End of execution"

if __name__ == "__main__":
   main(sys.argv[1:])
