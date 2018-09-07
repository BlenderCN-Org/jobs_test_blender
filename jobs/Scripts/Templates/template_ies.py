
def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = {pass_limit}
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	
	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.object.data.type = 'POINT'
	bpy.data.lamps["Lamp"].rpr_lamp.intensity = 50
	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = os.path.join("{res_path}", "ies" , test_list[2])

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":
	
	list_tests = [
	["BL_L_IES_001", ["IES file: 1.ies", "Intensity: 50"], "1.ies"], 
	["BL_L_IES_002", ["IES file: 2.ies", "Intensity: 50"], "2.ies"],
	["BL_L_IES_003", ["IES file: 3.ies", "Intensity: 50"], "3.ies"], 
	["BL_L_IES_004", ["IES file: 4.ies", "Intensity: 50"], "4.ies"], 
	["BL_L_IES_005", ["IES file: 5.ies", "Intensity: 50"], "5.ies"], 
	["BL_L_IES_006", ["IES file: 6.ies", "Intensity: 50"], "6.ies"],
	["BL_L_IES_007", ["IES file: 7.ies", "Intensity: 50"], "7.ies"], 
	["BL_L_IES_008", ["IES file: 8.ies", "Intensity: 50"], "8.ies"], 
	["BL_L_IES_009", ["IES file: 9.ies", "Intensity: 50"], "9.ies"], 
	["BL_L_IES_010", ["IES file: 10.ies", "Intensity: 50"], "10.ies"]
	]
	
	launch_tests()

