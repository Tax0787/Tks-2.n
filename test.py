from tks import Tks as T
class Test():
    def __init__(self):
        RO = T(name = 'self.root', sose = 'self.root.geometry("250x100")\nself.text = StringVar()\nself.text.set("Original Text")')
        exec(RO.sose(RO.wiget('self.buttonA', 'Button', ', textvariable=self.text') + RO.wiget('self.buttonB', 'Button', ',text="Click to change text", command=self.changeText')))
    def changeText(self):
        self.text.set(input('업대이트할 택스트 : '))

app=Test()