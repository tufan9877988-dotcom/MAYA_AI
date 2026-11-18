from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    MDLabel:
        text: "MAYA AI Initialized"
        halign: "center"
'''

class MayaAI(MDApp):
    def build(self):
        return Builder.load_string(KV)

if __name__ == '__main__':
    MayaAI().run()
