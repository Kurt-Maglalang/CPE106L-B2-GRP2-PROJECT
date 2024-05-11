from flet_mvc import FletController
#from mvc.Model.CreateProjM import CreateProjModel as CreateM
from mvc.View.CreateProjV import CreaterProjView as CreateV

class CreateProjController(FletController):
    def __init__(self):
        #self.model = CreateM()
        self.view = CreateV(self)
    
    def main(self):
        self.view.main()