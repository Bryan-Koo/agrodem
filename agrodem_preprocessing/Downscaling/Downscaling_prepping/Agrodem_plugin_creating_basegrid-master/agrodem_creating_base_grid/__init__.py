# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Agrodem_creating_base_grid
                                 A QGIS plugin
 TO BE ADDED
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2019-10-01
        copyright            : (C) 2019 by KTH-dESA
        email                : khavari@kth.se
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
    """Load Agrodem_creating_base_grid class from file Agrodem_creating_base_grid.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .Agrodem_creating_base_grid import Agrodem_creating_base_grid
    return Agrodem_creating_base_grid(iface)
