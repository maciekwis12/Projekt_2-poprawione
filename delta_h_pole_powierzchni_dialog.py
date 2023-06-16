# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DeltaH_PolePowDialog
                                 A QGIS plugin
 Delta H Pole Powierzchni
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-16
        git sha              : $Format:%H$
        copyright            : (C) 2023 by Maciej Wiśniewski, Aleksandra Krogulska
        email                : maciek.wis12@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.utils import iface
from qgis.core import QgsPointXY, QgsWkbTypes

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'delta_h_pole_powierzchni_dialog_base.ui'))


class DeltaH_PolePowDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(DeltaH_PolePowDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.pushButton_oblicz_roznice_wysokosci.clicked.connect(self.oblicz_roznice_wys)
        self.pushButton_oblicz_pole_powierzchni.clicked.connect(self.oblicz_pole_powierzchni_gauss)
        
    def oblicz_roznice_wys(self):
        canvas = iface.mapCanvas()
        warstwa = canvas.currentLayer()
        atrybuty = warstwa.selectedFeatures()
        
        if len(atrybuty) == 2:
            atrybut_h = "Wysokosc"
            wysokosci_punktow = []
            for atrybut in atrybuty:
                wys = atrybut[atrybut_h]
                wysokosci_punktow.append(wys)
    
            # Obliczanie różnicy wysokości między dwoma punktami
            delta_h = wysokosci_punktow[0] - wysokosci_punktow[1]
            self.textEdit_pokaz_roznice_wysokosci.setText(f"Różnica wysokości: {delta_h} [m]")
        else:
            self.textEdit_pokaz_roznice_wysokosci.setText("Zaznacz dokładnie dwa punkty.")


    def oblicz_pole_powierzchni_gauss(self):
        canvas = iface.mapCanvas()
        warstwa = canvas.currentLayer()

        if warstwa.geometryType() == QgsWkbTypes.PointGeometry:
            atrybuty = warstwa.selectedFeatures()

            # Pobieranie współrzędnych punktu
            punkty = []
            for atrybut in atrybuty:
                # Pobieranie geometrii punktu
                geometria = atrybut.geometry()

                # Pobieranie współrzędnych punktu
                punkt = geometria.asPoint()


                # Dodawanie współrzędnych do listy punktów
                punkty.append((punkt.x(), punkt.y()))

            n = len(punkty)

            # Dodajemy pierwszy punkt na koniec listy
            punkty.append(punkty[0])

            suma = 0.0
            for i in range(n):
                suma += (punkty[i+1][0] + punkty[i][0]) * (punkty[i+1][1] - punkty[i][1])

            pole_powierzchni = abs(suma) / 2.0
            self.textEdit_pokaz_pole_powierzchni.setText(f"Pole powierzchni: {pole_powierzchni} [m^2]")
        else:
            self.textEdit_pokaz_pole_powierzchni.setText("Zaznacz dokładnie trzy punkty.")
            self.textEdit_pokaz_pole_powierzchni.setText("Warstwa nie jest warstwą punktową.")

