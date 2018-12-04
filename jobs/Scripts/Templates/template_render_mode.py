
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

	bpy.context.scene.rpr.render.render_mode = test_list[3]

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_RM_001", ["Render mode: Wireframe"], "ComplexTestUber.blend", 'WIREFRAME'], 
	["BL_RS_RM_002", ["Render mode: Texcoord"], "ComplexTestUber.blend", 'TEXCOORD'],
	["BL_RS_RM_003", ["Render mode: Position"], "ComplexTestUber.blend", 'POSITION'], 
	["BL_RS_RM_004", ["Render mode: Normal"], "ComplexTestUber.blend", 'NORMAL'], 
	#["BL_RS_RM_005", ["Render mode: Material index"], "ComplexTestUber.blend", 'MATERIAL_INDEX'], 
	["BL_RS_RM_006", ["Render mode: Global illumination"], "ComplexTestUber.blend", 'GLOBAL_ILLUMINATION'],
	["BL_RS_RM_007", ["Render mode: Direct illumination no shadow"], "ComplexTestUber.blend", 'DIRECT_ILLUMINATION_NO_SHADOW'],
	["BL_RS_RM_008", ["Render mode: Direct illumination"], "ComplexTestUber.blend", 'DIRECT_ILLUMINATION'], 
	# ["BL_RS_RM_009", ["Render mode: Diffuse"], "ComplexTestUber.blend", 'DIFFUSE'],
	["BL_RS_RM_010", ["Render mode: Ambient occlusion"], "ComplexTestUber.blend", 'AMBIENT_OCCLUSION']
	]
	
	launch_tests()

