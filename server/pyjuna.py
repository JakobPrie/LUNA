import traceback

try:
    import juna
except ImportError:
    juna = None


class JavaModule:
    def __init__(self, junaModule):
        self.mod = junaModule
        self.PRIORITY = junaModule.PRIORITY
        self.WORDS = junaModule.WORDS
        self.__name__ = junaModule.MODNAME

    def isValid(self, text):
        return juna.javaModuleIsValid(self.mod, text)

    def telegram_isValid(self, text):
        return juna.javaModuleIsValidTelegram(self.mod, text)

    def handle(self, text, luna, profile):
        return juna.javaModuleHandle(self.mod, text, luna, profile)


class JavaModuleContinuous:
    def __init__(self, junaModule):
        self.mod = junaModule
        self.PRIORITY = junaModule.PRIORITY
        self.INTERVAL = junaModule.INTERVAL
        self.INTERVALL = junaModule.INTERVAL
        self.__name__ = junaModule.MODNAME

    def start(self, luna, profile):
        return juna.javaContinuousModuleStart(self.mod, luna, profile)

    def run(self, luna, profile):
        return juna.javaContinuousModuleRun(self.mod, luna, profile)

    def stop(self, luna, profile):
        return juna.javaContinuousModuleStop(self.mod, luna, profile)


def loadModules(path):
    if juna is not None:
        try:
            mods = juna.loadModules(path)
            wrappedMods = []
            for x in mods:
                if x is not None: # Wenn das Modul von Java aus deaktiviert wurde gibt es einen None-Eintrag.
                    wrappedMods.append(JavaModule(x))
                    print("[INFO] Java-Modul " + x.MODNAME + " geladen")
            return wrappedMods
        except:
            traceback.print_exc()
            print("Konnte JAVA-Module nicht laden.")
    return []


def loadModulesContinuous(path):
    if juna is not None:
        try:
            mods = juna.loadModulesContinuous(path)
            wrappedMods = []
            for x in mods:
                if x is not None: # Wenn das Modul von Java aus deaktiviert wurde gibt es einen None-Eintrag.
                    wrappedMods.append(JavaModuleContinuous(x))
                    print("[INFO] Fortlaufendes Java-Modul " + x.MODNAME + " geladen")
            return wrappedMods
        except:
            traceback.print_exc()
            print("Konnte JAVA-Module nicht laden.")
    return []

def createJavalogger(logging):
    if juna is not None:
        try:
            juna.createLogger(logging)
        except:
            traceback.print_exc()
            print("Der JAVA-Logger konnte nicht instanziiert werden.")

def setSignalHandlers():
    if juna is not None:
        juna.setSignalHandlers()

def shouldStop():
    if juna is not None:
        return juna.shouldStop()
    else:
        return False