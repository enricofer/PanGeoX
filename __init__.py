# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PanGeoX
                                 A QGIS plugin
 Panoramic Geodata eXtractor
                             -------------------
        begin                : 2015-07-08
        copyright            : (C) 2015 by Klas Karlsson, Enrico Ferreguti
        email                : enricofer@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PanGeoX class from file PanGeoX.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .PanGeoX_module import PanGeoX
    return PanGeoX(iface)
