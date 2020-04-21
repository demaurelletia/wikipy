from PyQt5 import QtWidgets, uic
import wikipedia

app=QtWidgets.QApplication([])
#chargement du fichier ui
dlg=uic.loadUi("wiki.ui")

def recherche():
  print(dlg.rech.text())
  dlg.stackedWidget.setCurrentIndex(1)
  
def init():
    #si on click sur le bouton historique la page se deplace a l'indice 2
    dlg.btn_historique.clicked.connect(lambda: dlg.stackedWidget.setCurrentIndex(2))
    #si on click sur le bouton accueil la page se deplace a l'indice 0
    dlg.accueil.clicked.connect(lambda: dlg.stackedWidget.setCurrentIndex(0))

    dlg.rech.returnPressed.connect(recherche)
  
init() #appel de le fonction init

dlg.show() #affichage de la fenetre
app.exec() #pour la fermeture de l'app
