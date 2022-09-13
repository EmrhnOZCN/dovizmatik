


from ast import For
from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import sys
from PyQt5.QtGui import QIcon

class Ui_Form(object):
    def setupUi(self, Form):
        url = "https://api.exchangerate.host/latest?"
        response = requests.get(url)
        jsonveri = response.json()
        
        

        Form.setObjectName("Form")
        Form.resize(719, 372)
        
     
        
        self.tarih = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tarih.setFont(font)
        self.tarih.setGeometry(QtCore.QRect(455, 20, 601, 18))
        self.tarih.setText("")
        self.tarih.setObjectName("tarih")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 140, 241, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.miktar_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.miktar_label.setFont(font)
        self.miktar_label.setAutoFillBackground(False)
        self.miktar_label.setObjectName("miktar_label")
        self.horizontalLayout_2.addWidget(self.miktar_label)
        self.miktar_edit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.miktar_edit.setFont(font)
        self.miktar_edit.setObjectName("miktar_edit")
        self.horizontalLayout_2.addWidget(self.miktar_edit)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 240, 240, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.iki_deger_label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.iki_deger_label.setFont(font)
        self.iki_deger_label.setAutoFillBackground(False)
        self.iki_deger_label.setObjectName("iki_deger_label")
        self.horizontalLayout_3.addWidget(self.iki_deger_label)
        self.ikinci_doviz = QtWidgets.QComboBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ikinci_doviz.setFont(font)
        self.ikinci_doviz.setObjectName("ikinci_doviz")
        self.horizontalLayout_3.addWidget(self.ikinci_doviz)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(40, 40, 240, 80))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bir_deger_label = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.bir_deger_label.setFont(font)
        self.bir_deger_label.setAutoFillBackground(False)
        self.bir_deger_label.setObjectName("bir_deger_label")
        self.horizontalLayout_4.addWidget(self.bir_deger_label)
        self.birinci_doviz = QtWidgets.QComboBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.birinci_doviz.setFont(font)
        self.birinci_doviz.setObjectName("birinci_doviz")
        self.horizontalLayout_4.addWidget(self.birinci_doviz)
        self.cevir_buton = QtWidgets.QPushButton(Form)
        self.cevir_buton.setGeometry(QtCore.QRect(550, 305, 111, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.cevir_buton.setFont(font)
        self.cevir_buton.setObjectName("cevir_buton")
        
        self.sonuc = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setPointSize(14)
        self.sonuc.setFont(font)
        self.sonuc.setGeometry(QtCore.QRect(385, 148, 301, 61))
        self.sonuc.setText("")
        self.sonuc.setObjectName("sonuc")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        

        tarih_veri = (jsonveri["date"])
        self.tarih.setText( " Şu tarihteki dövizler: "+ tarih_veri)


        bir_doviz_veri = (jsonveri["rates"].keys())
        self.birinci_doviz.addItems(bir_doviz_veri)

        ikinci_doviz_veri = (jsonveri["rates"].keys())
        self.ikinci_doviz.addItems(ikinci_doviz_veri)

        self.cevir_buton.clicked.connect(self.doviz_hesapla)


    def doviz_hesapla(self):
        url1 = "https://api.exchangerate.host/latest?"
        response = requests.get(url1)
        jsonveri2 = response.json()

        secilen_birinci_doviz = self.birinci_doviz.currentText()
        doviz_deger_bir = (jsonveri2["rates"][secilen_birinci_doviz])

        secilen_ikinci_doviz = self.ikinci_doviz.currentText()
        doviz_deger_iki = (jsonveri2["rates"][secilen_ikinci_doviz])

        mktr = float(self.miktar_edit.text())
        sonuc_deger = mktr*doviz_deger_iki / doviz_deger_bir

        sonuc_deger=round(sonuc_deger,2)

        
        self.sonuc.setText(" {}, {} {} yapar.".format(secilen_birinci_doviz,sonuc_deger,secilen_ikinci_doviz))        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dövizmatik                                               EMİRHAN ÖZCAN"))
        
        self.miktar_label.setText(_translate("Form", "Miktar:"))
        self.iki_deger_label.setText(_translate("Form", "İkinci Döviz:"))
        self.bir_deger_label.setText(_translate("Form", "Birinci Döviz:"))
        self.cevir_buton.setText(_translate("Form", "ÇEVİR"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QIcon('dovizmatik/pngwing2.png'))
   
    
    Form = QtWidgets.QWidget() 
    
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
