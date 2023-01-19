###############
# LV Color    #
# By Luke Van #
###############
"""
Modify by Angèle Sionneau in november 2022
""" 

nodes = hou.selectedNodes()

if nodes :
     
    sCol = hou.selectedNodes()[0].color()
     
    color = sCol
     
    def handleColorChange(color, alpha):
        color = color
        
        nodes = hou.selectedNodes()
        
        for index, n in enumerate(nodes):
            node = n
            if(color):   
                n.setColor(color)
            else:
                pass
     
    hou.ui.openColorEditor(
        handleColorChange,
        include_alpha=False,
        initial_color=sCol)
 