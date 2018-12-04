
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[2]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[2]))

	Scenename = bpy.context.scene.name

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = test_list[3]
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	render(test_list[0], test_list[1])
	return 1
	

if __name__ == "__main__":

	list_tests = [
	["BL_RS_PS_001", ["Pass Limit: 1, Easy Scene"], "ComplexTestUber.blend", 1],
	["BL_RS_PS_002", ["Pass Limit: 100, Easy Scene"], "ComplexTestUber.blend", 100],
	["BL_RS_PS_003", ["Pass Limit: 500, Easy Scene"], "ComplexTestUber.blend", 500],
	["BL_RS_PS_004", ["Pass Limit: 1000, Easy Scene"], "ComplexTestUber.blend", 1000],
	# ["BL_RS_PS_005", ["Pass Limit: 5000, Easy Scene"], "ComplexTestUber.blend", 5000],
	# ["BL_RS_PS_006", ["Pass Limit: 10000, Easy Scene"], "ComplexTestUber.blend", 10000],
	["BL_RS_PS_007", ["Pass Limit: 1, Medium Scene"], "PassLimit_1.blend", 1],
	["BL_RS_PS_008", ["Pass Limit: 100, Medium Scene"], "PassLimit_1.blend", 100],
	["BL_RS_PS_009", ["Pass Limit: 500, Medium Scene"], "PassLimit_1.blend", 500],
	["BL_RS_PS_010", ["Pass Limit: 1000, Medium Scene"], "PassLimit_1.blend", 1000],
	# ["BL_RS_PS_011", ["Pass Limit: 5000, Medium Scene"], "PassLimit_1.blend", 5000],
	# ["BL_RS_PS_012", ["Pass Limit: 10000, Medium Scene"], "PassLimit_1.blend", 10000],
	["BL_RS_PS_013", ["Pass Limit: 1, Complex Scene"], "PassLimit_2.blend", 1],
	["BL_RS_PS_014", ["Pass Limit: 100, Complex Scene"], "PassLimit_2.blend", 100],
	["BL_RS_PS_015", ["Pass Limit: 500, Complex Scene"], "PassLimit_2.blend", 500],
	["BL_RS_PS_016", ["Pass Limit: 1000, Complex Scene"], "PassLimit_2.blend", 1000],
	# ["BL_RS_PS_017", ["Pass Limit: 5000, Complex Scene"], "PassLimit_2.blend", 5000],
	# ["BL_RS_PS_018", ["Pass Limit: 10000, Complex Scene"], "PassLimit_2.blend", 10000],
	]

	launch_tests()