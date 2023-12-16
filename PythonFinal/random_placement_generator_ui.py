import maya.cmds as cmds
from random_placement_generator import RandomPlacementGenerator

class RandomPlacementGeneratorUI:
    def __init__(self):
        self.window_name = "randomPlacementGeneratorUI"

    def create(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name, window=True)

        cmds.window(self.window_name, title="Random Placement Generator UI")
        cmds.columnLayout(adjustableColumn=True)

        num_elements_field = cmds.intFieldGrp(label="Number of Elements", value1=5)
        btn_generate = cmds.button(label="Generate", command=lambda x: self.generate_callback(num_elements_field))

        cmds.showWindow(self.window_name)

    def generate_callback(self, num_elements_field):
        num_elements = cmds.intFieldGrp(num_elements_field, query=True, value1=True)
        
        # Call the generate_random_placement function and store the result in a variable
        placements = RandomPlacementGenerator.generate_random_placement(num_elements)

        # Now, you can use the placements variable as needed, for example, printing the result
        print("Generated random placements:", placements)

# Example usage in Maya:
ui = RandomPlacementGeneratorUI()
ui.create()
