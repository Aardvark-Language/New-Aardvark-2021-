class Place:
    def __init__(self, file=None, block=None):
        self.file = file
        self.block = block
        if self.file != None and self.block != None:
            self.type = "local"
        elif self.file != None:
            self.type == "global"
        else:
            self.type = "universal"

    def eval(self, file=None, block=None):
        pass


class Variable:  #This is for Variables
    def __init__(self, language, name, value, place, t=""):
        self.name = name
        self.language = language
        self.value = value
        if t == "": t = type(value)
        self.type = t
        self.place = place

    def get(self):  #For getting the variables so you get accurate info
        if self.type == "stream":  #A new type of variable I invented, makes 2 variables always equal
            return self.language.gettype(self.value)[1]
        return self.value


class DType:  #This is used for Data Types
    def __init__(self):
        self.attributes = {}
        self.check = lambda x: False

    def getattr(self, attrname):
        return self.attributes[attrname]


class Language:  #The language class
    def __init__(self, lexer=lambda x: []):
        self.variables = {}
        self.tokens = []
        self.lexer = lexer
        #make @language.type(name, class) work, require class to inherit DType with __bases__
    def Variable(self, name, value, file=None, block=None):#For making variables
        self.variables[name] = Variable(self, name, value, Place())

    def Type(self, name):#Making types
        def wrapper(call):
            self.variables[name] = Variable(self, name, call, Place(), t=DType)#Types are variables and have a type of DType

            def repeat(what):
                a = call(what)
                if a == None: a = False
                return a

            return repeat

        return wrapper

    def Function(self, name, file=None, block=None):
        def wrapper(call):
            self.variables[name] = Variable(
                self, name, call, Place(file, block), t='Function')#I still need to make a function type

            def repeat(*args, **kwargs):
                return call(*args, **kwargs)

            return repeat

        return wrapper

    def gettype(self, what, nolex=False):#Gets the type of something
        print(self.variables)
        if what in self.variables:
            var = self.variables[what]
            return (var.type, var.get())
        for ty in self.variables:
            ty = self.variables[ty]
            if ty.type != DType: continue
            check = ty.value.check(ty.value, what)
            if check != False:
                return ty.value, check
