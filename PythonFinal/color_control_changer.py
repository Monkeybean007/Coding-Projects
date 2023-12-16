# color_control_changer.py
import maya.cmds as cmds

class ColorControlChanger:
    @staticmethod
    def change_color_control(objects, new_value):
        for obj in objects:
            cmds.setAttr(obj + ".color", new_value, new_value, new_value, type="double3")

# Example usage in Maya:
selected_objects = cmds.ls(selection=True)
new_value = 0.5  # Set your desired new color control value
ColorControlChanger.change_color_control(selected_objects, new_value)
