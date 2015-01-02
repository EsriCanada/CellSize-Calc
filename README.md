CellSize-Calc
=============

This simple ArcMap addin contains a toolbar with three button commands that helps to quickly convert between map scale and cell size.

The combo box/text box reports the cell size of the current scale when the button is clicked.  The user can also manually type a cell size value to zoom to the corresponding map scale.  Keeps a history of recently viewed cell sizes which can be cleared with the second button.  Some logging messages can be found if the python window is open.

Useful for working with [Mosaic Datasets](http://resources.arcgis.com/en/help/main/10.2/index.html#//009t00000042000000).

The formula used is: 

Cell Size = Scale * 0.0254 / 96
Scale = Cell Size * 96 / 0.0254

Currently at version 1.0

Tested at ArcGIS Desktop 10.2.2.
