CellSize-Calc
=============

This simple ArcMap addin contains a toolbar with three button commands that helps to quickly convert between map scale and cell size.

The combo box/text box reports the cell size of the current scale when the button is clicked.  The user can also manually type a cell size value to zoom to the corresponding map scale.  Keeps a history of recently viewed cell sizes which can be cleared with the second button.  Some logging messages can be found if the python window is open.

Useful for working with [Mosaic Datasets](http://resources.arcgis.com/en/help/main/10.2/index.html#//009t00000042000000).

The formula used is: 

Cell Size = Scale * 0.0254 / 96
Scale = Cell Size * 96 / 0.0254

See details page on ArcGIS Online: [CellSize Calculator](http://www.arcgis.com/home/item.html?id=749fc5ac2f884b16a8edefb5c14873ba)

####Quick Start
- [Download](https://github.com/EsriCanada/CellSize-Calc/archive/master.zip) the repo zip file and extract to your machine
- Double-click the *CellSize.esriaddin* file to install
- In ArcMap, see Customize menu > Add-In Manager...
- Add the toolbar from the Customize menu > Customize Mode... > Toolbars > Cell Size

####Source code
The addin was built using the [Python Add-In Wizard](http://www.arcgis.com/home/item.html?id=5f3aefe77f6b4f61ad3e4c62f30bff3b)
- Edit the [*CellSize_addin.py*](https://github.com/EsriCanada/CellSize-Calc/blob/master/Install/CellSize_addin.py) file as you see fit
- re-create the .esriaddin file by double clicking *makeaddin.py* in the root directory (or run it from cmd if your .py file association is not pointing to 2.x python install)

#####Version
Currently at version 1.0
Tested at ArcGIS Desktop 10.2.2.

#####Future Improvements
- Report the Cell Size automatically when the map scale changes without the need for the button click
