import maya.cmds as cmds

def change_object_color(color_index):
    selected_objects = cmds.ls(selection=True, long=True)

    if not selected_objects:
        cmds.warning("No objects selected.")
        return

    for obj in selected_objects:
        # Check if the object has a shading group
        shading_group = cmds.listConnections(obj, type="shadingEngine")

        if not shading_group:
            # If the object doesn't have a shading group, create a Lambert material
            lambert_shader = cmds.shadingNode('lambert', asShader=True)
            # Set the color using colorIndex
            cmds.setAttr(lambert_shader + ".color", *cmds.colorIndex(color_index, q=True), type="double3")
            
            # Assign the Lambert shader to the object
            cmds.select(obj)
            shading_group = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=lambert_shader + 'SG')
            cmds.hyperShade(assign=lambert_shader)
            
            print(f"Lambert material created and assigned to {obj}.")

        # Set the color using colorIndex
        cmds.setAttr(lambert_shader + ".color", *cmds.colorIndex(color_index, q=True), type="double3")
        print(f"Color changed to {color_index} for {obj}.")

def create_color_change_ui():
    if cmds.window("colorChangeUI", exists=True):
        cmds.deleteUI("colorChangeUI", window=True)

    color_change_ui = cmds.window("colorChangeUI", title="Color Change UI", widthHeight=(200, 100))
    cmds.columnLayout(adjustableColumn=True)

    color_slider = cmds.intSliderGrp(field=True, label="Color Index", min=0, max=31, value=0)
    change_color_button = cmds.button(label="Change Color", command=lambda x: change_object_color(cmds.intSliderGrp(color_slider, q=True, value=True)))

    cmds.showWindow(color_change_ui)
