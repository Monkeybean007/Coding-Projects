# run_both.py
import maya.cmds as cmds
from random_placement_generator import RandomPlacementGenerator
from color_control_changer import ColorControlChanger

class App:
    @classmethod
    def create(cls):
        root = cmds.dockControl(area='right', content=cls.create_main_layout(), allowedArea='right', label='Main Window')
        cls.root = root

    @staticmethod
    def create_main_layout():
        # Create a unique name for the layout
        layout_name = cmds.columnLayout(adjustableColumn=True)

        # Create and run the Random Placement Generator
        num_elements = 5  # Set your desired number of elements
        placements = RandomPlacementGenerator.generate_random_placement(num_elements)
        for placement in placements:
            cmds.polySphere(radius=0.1, center=placement)

        # Create and run the Color Control Changer
        selected_objects = cmds.ls(selection=True)
        new_value = 0.5  # Set your desired new color control value
        ColorControlChanger.change_color_control(selected_objects, new_value)

        return layout_name

if __name__ == "__main__":
    App.create()
