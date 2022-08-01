class Ide:
    def functionalities(self):
        funcs=["create_file","rename","delete"]
        return funcs
class Pycharm(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("execute")
        funcs.append("debug")
        return funcs
class vscode(Pycharm):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("vcs")
        funcs.append("formatting")
        return funcs
py=Pycharm()

print(py.functionalities())
vsc=vscode()
print(vsc.functionalities())