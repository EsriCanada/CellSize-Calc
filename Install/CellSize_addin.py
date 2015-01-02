import arcpy
import pythonaddins

"""
Thanks for using the Cell Size Calculator. Suggestions?
Formula:  [  Scale = Cell Size * 96 / 0.0254  ]
"""

class CSCalc(object):
    """Implementation for CellSize_addin.button (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        if combobox.check_coord():
            combobox.value = combobox.calc_cell()
            combobox.print_value()
            combobox.add_item()
            combobox.refresh()
        else:
            print "Unknown Coordinate System: Dataframe coordinate system must be defined to use this tool"
            pythonaddins.MessageBox('Dataframe coordinate system must be defined to use this tool', 'Unknown Coordinate System', 0)

class CSRemove(object):
    """Implementation for CellSize_addin.button_1 (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        combobox.remove_items()
        combobox.remove_value()
        combobox.refresh()

class CSCombo(object):
    """Implementation for CellSize_addin.combobox (ComboBox)"""
    def __init__(self):
        self.editable = True
        self.enabled = True
        self.dropdownWidth = 'WWWWWWWWW'
        self.width = 'WWWWWWWWW'
        self.items = []
        self.dec = 6 # number of decimal places for rounding purposes
        
    def onSelChange(self, selection):
        self.set_scale()        
    
    def onEditChange(self, text):
        pass
    
    def onFocus(self, focused):
        pass
    
    def onEnter(self):
        if self.check_cell():
            if self.check_coord():
                if self.check_value():
                    self.set_scale()
                    self.add_item()
                    self.refresh()
                else:
                    print "Invalid cell size: Cell Size must be greater than 0"
                    pythonaddins.MessageBox('Cell Size must be greater than 0', 'Invalid cell size', 0)                
                    self.value = self.calc_cell()
            else:
                print "Unknown Coordinate System: Dataframe coordinate system must be defined to use this tool"
                pythonaddins.MessageBox('Dataframe coordinate system must be defined to use this tool', 'Unknown Coordinate System', 0)
        else:
            print "Cell size value error: Cell Size must be numeric value"
            pythonaddins.MessageBox('Cell size must be numeric value', 'Cell Size value error', 0)
        
    def refresh(self):        
        self.items = list(set(self.items))        
        self.items.sort()        
        arcpy.RefreshActiveView()    
    
    def add_item(self):
        self.value = round(float(self.value), self.dec)
        if self.value not in self.items:
            self.items.append(round(float(self.value), self.dec))        

    def remove_items(self):
        self.items = []

    def remove_value(self):
        self.value = ""

    def check_value(self):
        return False if float(self.value) <=0 else True

    def check_cell(self):
        try:
            float(self.value)
            return True
        except ValueError:
            return False

    def check_coord(self):
        df = self.dataframe()        
        if str(df.mapUnits) == "Unknown":            
            return False
        else:            
            return True
        
    def dataframe(self):
        mxd = arcpy.mapping.MapDocument('CURRENT')
        return arcpy.mapping.ListDataFrames(mxd, mxd.activeView)[0]

    def calc_scale(self):
        return float(self.value)*96/0.0254
    
    def calc_cell(self):
        return round((self.get_scale()*0.0254)/96, self.dec)
        
    def get_scale(self):
        df = self.dataframe() # returns float
        return df.scale
    
    def set_scale(self):
        df = self.dataframe()         
        df.scale = self.calc_scale()
        self.refresh()
        
    def print_value(self):
        print "Cell Size for current scale (1:%s) = %s" % (float(self.get_scale()), float(self.calc_cell()))
        
