import maya.cmds as cmds
from color_control_changer import ColorControlChanger

class ColorControlChangerUI:
    def __init__(self):
        self.window_name = "colorControlChangerUI"

    def create(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name, window=True)

        cmds.window(self.window_name, title="Color Control Changer UI")
        cmds.columnLayout(adjustableColumn=True)

        new_value = cmds.floatSliderGrp(label="New Color Control Value", field=True, minValue=0.0, maxValue=1.0, value=0.5)
        btn_change_color = cmds.button(label="Change Color Control", command=lambda x: self.change_color_callback(new_value))

        cmds.showWindow(self.window_name)

    def change_color_callback(self, new_value_field):
        new_value = cmds.floatSliderGrp(new_value_field, query=True, value=True)
        ColorControlChanger.change_color_control(new_value)
        print(f"Changed color control to {new_value}")

# Example usage in Maya:
# ui = ColorControlChangerUI()
# ui.create()
