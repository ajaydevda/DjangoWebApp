import requests
from myapp.models import Webcontent


class sqlliteDatatBaseHander:
    textToDelete = ""

    def webContentCreate(self):
    
        webcontentToSave = Webcontent( webTextContent = "Help The Children in need")
        webcontentToSave.save()
        
    
    def webContentRead(self):
    
        objects = Webcontent.objects.all()
        return objects
    
    def webCOntentDelete(self):
        objects = Webcontent.objects.all()
        for dele in objects:
            instance = Webcontent.objects.filter(webTextContent = self.textToDelete)
            instance.delete()

    
    # def webCOntentUpdate:
    




