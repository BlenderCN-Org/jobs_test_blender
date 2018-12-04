
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	Scenename = bpy.context.scene.name

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.use_nodes = True
	nodes = bpy.data.scenes[0].node_tree.nodes

	file_output = nodes["File Output"]
	file_output.base_path = r"{work_dir}" + "/Color"
	#file_output.file_slots[0].path = test_list[0]

	render_layer = nodes["Render Layers"]

	bpy.context.scene.render.layers.active.rpr_data.passes_aov.enable = True
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[test_list[4]] = True

	bpy.context.scene.node_tree.links.new(render_layer.outputs[test_list[3]], file_output.inputs[test_list[4]])

	render(test_list[0], test_list[1])
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[test_list[4]] = False
	bpy.context.scene.render.layers.active.rpr_data.passes_aov.passesStates[0] = True

	os.remove(r"{work_dir}" + "/Color/" + test_list[0] + '.jpg')
	os.rename(r"{work_dir}" + "/Color/" + test_list[0] + '0001.jpg', \
		r"{work_dir}" + "/Color/" + test_list[0] + '.jpg')

	return 1
	
if __name__ == "__main__":

	list_tests = [
	["BL_RS_AOV_001", ["AOV: Combined"], "AOV.blend", 'Image', 0], 
	["BL_RS_AOV_002", ["AOV: Depth"], "AOV.blend", 'Depth', 1], 
	["BL_RS_AOV_003", ["AOV: UV"], "AOV.blend", 'UV', 2], 
	["BL_RS_AOV_004", ["AOV: Object Index"], "AOV.blend", 'Object Index', 3], 
	["BL_RS_AOV_005", ["AOV: Material Index"], "AOV.blend", 'Material Index', 4], 
	["BL_RS_AOV_006", ["AOV: World Coordinate"], "AOV.blend", 'World Coordinate', 5],
	["BL_RS_AOV_007", ["AOV: Geometric Normal"], "AOV.blend", 'Geometric Normal', 6], 
	["BL_RS_AOV_008", ["AOV: Shading Normal"], "AOV.blend", 'Shading Normal', 7], 
	["BL_RS_AOV_009", ["AOV: Group Index"], "AOV.blend", 'Group Index', 8],
	["BL_RS_AOV_010", ["AOV: Shadow Catcher"], "AOV.blend", 'Shadow Catcher', 9], 
	["BL_RS_AOV_011", ["AOV: Background"], "AOV.blend", 'Background', 10], 
	["BL_RS_AOV_012", ["AOV: Emission"], "AOV.blend", 'Emission', 11],
	# ["BL_RS_AOV_013", ["AOV: Velocity"], "AOV.blend", 'Velocity', 12], 
	["BL_RS_AOV_014", ["AOV: Direct Illumination"], "AOV.blend", 'Direct Illumination', 13], 
	["BL_RS_AOV_015", ["AOV: Indirect Illumination"], "AOV.blend", 'Indirect Illumination', 14],
	["BL_RS_AOV_016", ["AOV: Ambient Occlusion"], "AOV.blend", 'Ambient Occlusion', 15], 
	["BL_RS_AOV_017", ["AOV: Direct Diffuse"], "AOV.blend", 'Direct Diffuse', 16], 
	["BL_RS_AOV_018", ["AOV: Direct Reflection"], "AOV.blend", 'Direct Reflection', 17], 
	["BL_RS_AOV_019", ["AOV: Indirect Diffuse"], "AOV.blend", 'Indirect Diffuse', 18], 
	["BL_RS_AOV_020", ["AOV: Indirect Reflection"], "AOV.blend", 'Indirect Reflection', 19], 
	["BL_RS_AOV_021", ["AOV: Refraction"], "AOV.blend", 'Refraction', 20],
	["BL_RS_AOV_022", ["AOV: Volume"], "AOV.blend", 'Volume', 21], 
	["BL_RS_AOV_023", ["AOV: Opacity"], "AOV.blend", 'Opacity', 22]
	]

	launch_tests()
