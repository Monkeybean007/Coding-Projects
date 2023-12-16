import maya.cmds as cmds
from random_placement_generator_ui import RandomPlacementGeneratorUI
from color_control_changer_ui import ColorControlChangerUI

class App:
    @classmethod
    def create(cls):
        root = cmds.dockControl(area='right', content=cls.create_main_layout, allowedArea='right', label='Main Window')
        cls.root = root

    @staticmethod
    def create_main_layout():
        cmds.columnLayout(adjustableColumn=True)

        # Create and run the Random Placement Generator UI
        random_placement_ui = RandomPlacementGeneratorUI()
        random_placement_ui.create()

        # Create and run the Color Control Changer UI
        color_control_ui = ColorControlChangerUI()
        color_control_ui.create()

if __name__ == "__main__":
    App.create()
