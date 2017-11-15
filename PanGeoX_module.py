# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PanGeoX
                                 A QGIS plugin
 Panoramic Geodata eXtractor
                              -------------------
        begin                : 2015-07-08
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Klas Karlsson, Enrico Ferreguti
        email                : enricofer@gmail.com
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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtWebKit import *
from qgis.core import *
from qgis.utils import *
from qgis.gui import *

from PyQt4.QtCore import pyqtSignal

# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from PanGeoX_module_dialog import PanGeoXDialog
import os.path
import json

class myWebPage(QWebPage):

    
    fileChoosed = pyqtSignal(str)
    
    def __init__(self):
        QWebPage.__init__(self)
        self.file_name = 'test.png'  # file name we want to be choosed

    def chooseFile(self, frame, suggested_file):
        self.fileChoosed.emit(suggested_file)
        return self.file_name  # file will be choosen after click on input type=file


class PanGeoX:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'PanGeoX_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        #self.dlg = PanGeoXDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&PanGeoX')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'PanGeoX')
        self.toolbar.setObjectName(u'PanGeoX')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('PanGeoX', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = os.path.join(self.plugin_dir,"icon.png")
        self.add_action(
            icon_path,
            text=self.tr(u'PanGeoX'),
            callback=self.run,
            parent=self.iface.mainWindow())
            
        self.wdg = PanGeoXDialog()
        self.apdockwidget=QDockWidget("PanGeoX" , self.iface.mainWindow() )
        self.apdockwidget.setObjectName("PanGeoX")
        self.apdockwidget.setWidget(self.wdg)
        self.apdockwidget.setAllowedAreas(Qt.TopDockWidgetArea | Qt.BottomDockWidgetArea)
        self.iface.addDockWidget( Qt.TopDockWidgetArea, self.apdockwidget)
        self.apdockwidget.update()
        
        self.wdg.webView.settings().setAttribute(QWebSettings.LocalContentCanAccessRemoteUrls, True)
        self.wdg.webView.settings().setAttribute(QWebSettings.LocalContentCanAccessFileUrls, True)
        self.wdg.webView.settings().setAttribute(QWebSettings.LocalStorageEnabled, True)
        self.wdg.webView.settings().setAttribute(QWebSettings.AutoLoadImages, True)
        self.wdg.webView.settings().setAttribute(QWebSettings.DeveloperExtrasEnabled, True)
        self.wdg.webView.settings().setAttribute(QWebSettings.AcceleratedCompositingEnabled, True)
        self.wdg.webView.page().mainFrame().setScrollBarPolicy( Qt.Vertical, Qt.ScrollBarAlwaysOff )
        self.wdg.webView.page().mainFrame().setScrollBarPolicy( Qt.Horizontal, Qt.ScrollBarAlwaysOff )

        self.wdg.webView.load(QUrl.fromLocalFile(os.path.join(self.plugin_dir,"lib","index.html")))
        
        self.wdg.webView.page().statusBarMessage.connect(self.collect)

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&PanGeoX'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar

    def transformToWGS84(self, pPoint):
        # transformation from the current SRS to WGS84
        crcMappaCorrente = iface.mapCanvas().mapRenderer().destinationCrs() # get current crs
        crsSrc = crcMappaCorrente
        crsDest = QgsCoordinateReferenceSystem(4326)  # WGS 84
        xform = QgsCoordinateTransform(crsSrc, crsDest)
        return xform.transform(pPoint) # forward transformation: src -> dest

    def transformToCurrentSRS(self, pPoint):
        # transformation from the current SRS to WGS84
        crcMappaCorrente = iface.mapCanvas().mapRenderer().destinationCrs() # get current crs
        crsDest = crcMappaCorrente
        crsSrc = QgsCoordinateReferenceSystem(4326)  # WGS 84
        xform = QgsCoordinateTransform(crsSrc, crsDest)
        return xform.transform(pPoint) # forward transformation: src -> dest

    def transformFromUTMToCurrentSRS(self,utmZone, pPoint):
        # transformation from UTMzone to currentSrs - WGS 84 / UTM zone 
        crcMappaCorrente = iface.mapCanvas().mapRenderer().destinationCrs() # get current crs
        crsDest = crcMappaCorrente
        crsSrc = QgsCoordinateReferenceSystem("WGS 84 / UTM zone "+utmZone)  # UTM zone
        
        xform = QgsCoordinateTransform(crsSrc, crsDest)
        return xform.transform(pPoint) # forward transformation: src -> dest
        
    def transformFromUTMToLayerSRS(self,utmZone,layer, pPoint):
        #csrs = iface.mapCanvas().mapRenderer().destinationCrs()
        #print csrs.isValid(),csrs.description(),csrs.projectionAcronym(),csrs.srsid() 
        # transformation from UTMzone to currentSrs - WGS 84 / UTM zone 
        crsDest = layer.crs() # get layer crs
        if utmZone[-1] == "N":
            utmCrsId = 32600 + int(utmZone[:-1])
        elif utmZone[-1] == "S":
            utmCrsId = 32700 + int(utmZone[:-1])
        crsSrc = QgsCoordinateReferenceSystem(utmCrsId)  # UTM CRS
        #print crsSrc.isValid(),crsSrc.description(),crsSrc.projectionAcronym(),crsSrc.srsid() 
        xform = QgsCoordinateTransform(crsSrc, crsDest)
        return xform.transform(pPoint) # forward transformation: src -> dest
        
    def transformToLayerSRS(self,layer, pPoint):
        # transformation from project SRS the provided layer SRS
        crsDest = layer.crs() # get layer crs
        crsSrc = iface.mapCanvas().mapRenderer().destinationCrs()  # project srs
        xform = QgsCoordinateTransform(crsSrc, crsDest)
        return xform.transform(pPoint) # forward transformation: src -> dest

    def collect(self,status):
        #print status
        try:
            collected = json.JSONDecoder().decode(status)
        except:
            return
        print collected
        pangeoxLayerList = QgsMapLayerRegistry.instance().mapLayersByName("PanGeoX_objects")
        print pangeoxLayerList
        if not pangeoxLayerList:
            hem = collected["utmZone"][-1]
            print hem
            if hem == 'N':
                utm_authid = 32600 + int(collected["utmZone"][:-1])
            elif hem == 'S':
                utm_authid = 32700 + int(collected["utmZone"][:-1])
            print int(collected["utmZone"][:-1])
            pangeoxLayer = QgsVectorLayer("Point?crs=EPSG:"+str(utm_authid), "PanGeoX_objects", "memory")

            pangeoxLayer.startEditing()
            pangeoxLayer.addAttribute(QgsField("utmZone",QVariant.Int))
            pangeoxLayer.addAttribute(QgsField("x",QVariant.Double))
            pangeoxLayer.addAttribute(QgsField("y",QVariant.Double))
            pangeoxLayer.addAttribute(QgsField("objName",QVariant.String))
            pangeoxLayer.addAttribute(QgsField("angle",QVariant.Double))
            pangeoxLayer.commitChanges()
            pangeoxLayer.loadNamedStyle(os.path.join(self.plugin_dir,"lib","pangeox.qml"))
            QgsMapLayerRegistry.instance().addMapLayer(pangeoxLayer)
        else:
            pangeoxLayer = pangeoxLayerList[0]
        
        newgeom = QgsGeometry.fromPoint(self.transformFromUTMToLayerSRS(collected["utmZone"],pangeoxLayer,QgsPoint(collected["objEast"],collected["objNorth"])))
        #print newgeom.exportToWkt()
        newfeat = QgsFeature()
        newfeat.setGeometry(newgeom)
        newfeat.setAttributes([collected["utmZone"],collected["objEast"],collected["objNorth"],collected["objName"],collected["angle"]])
        pangeoxLayer.startEditing()
        pangeoxLayer.addFeatures([newfeat])
        pangeoxLayer.commitChanges()
        pangeoxLayer.setSelectedFeatures ([])

    def run(self):
        # called by click on toolbar icon
        if self.apdockwidget.isVisible():
            self.apdockwidget.hide()
        else:
            self.apdockwidget.show()
