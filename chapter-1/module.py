# what is module in python?
#! A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.
# Description: This module is used to get a joke from the pyjokes library.

import pyjokes

joke = pyjokes.get_joke()
print(joke)