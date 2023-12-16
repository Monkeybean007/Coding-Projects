import maya.cmds as cmds
import random

def random_placement(num_duplicates, min_x, max_x, min_y, max_y, min_z, max_z):
    selected_objects = cmds.ls(selection=True, long=True)

    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    for _ in range(num_duplicates):
        for obj in selected_objects:
            # Duplicate the selected object
            duplicated_objects = cmds.duplicate(obj)

            # Generate random translation values
            rand_x = random.uniform(min_x, max_x)
            rand_y = random.uniform(min_y, max_y)
            rand_z = random.uniform(min_z, max_z)

            # Move the duplicated object to the random position
            cmds.move(rand_x, rand_y, rand_z, duplicated_objects)

def execute_random_placement(num_duplicates_field, x_range_field, y_range_field, z_range_field):
    num_duplicates = cmds.intFieldGrp(num_duplicates_field, q=True, value1=True)
    x_range = cmds.floatFieldGrp(x_range_field, q=True, value=True)
    y_range = cmds.floatFieldGrp(y_range_field, q=True, value=True)
    z_range = cmds.floatFieldGrp(z_range_field, q=True, value=True)

    random_placement(num_duplicates, x_range[0], x_range[1], y_range[0], y_range[1], z_range[0], z_range[1])

def create_random_placement_ui():
    if cmds.window("randomPlacementUI", exists=True):
        cmds.deleteUI("randomPlacementUI", window=True)

    random_placement_ui = cmds.window("randomPlacementUI", title="Random Placement UI", widthHeight=(300, 150))
    cmds.columnLayout(adjustableColumn=True)

    num_duplicates_field = cmds.intFieldGrp(numberOfFields=1, label="Number of Duplicates:", value1=1)
    x_range_field = cmds.floatFieldGrp(numberOfFields=2, label="X Range (Min/Max):", value1=0.0, value2=10.0)
    y_range_field = cmds.floatFieldGrp(numberOfFields=2, label="Y Range (Min/Max):", value1=0.0, value2=10.0)
    z_range_field = cmds.floatFieldGrp(numberOfFields=2, label="Z Range (Min/Max):", value1=0.0, value2=10.0)

    random_placement_button = cmds.button(label="Random Placement", command=lambda x: execute_random_placement(num_duplicates_field, x_range_field, y_range_field, z_range_field))

    cmds.showWindow(random_placement_ui)
