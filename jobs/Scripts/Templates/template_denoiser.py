def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = 100
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	bpy.context.scene.rpr.render.denoiser.enable = True

	if (test_list[2] == "bilateral" and test_list[3] == -1):
		return test_bilateral(test_list[0], test_list[1], test_list[4], test_list[5])

	elif (test_list[2] == "lwr" and test_list[3] == -1):    
		return test_lwr(test_list[0], test_list[1], test_list[4], test_list[5])

	elif (test_list[2] == "eaw" and test_list[3] == -1):
		return test_eaw(test_list[0], test_list[1], test_list[4])

	elif (test_list[3] != -1):
		return test_aov_denoiser(test_list[0], test_list[1], test_list[2], test_list[3])
		

def test_bilateral(test_case, script_info, radius, sigma):

	bpy.context.scene.rpr.render.denoiser.filter_type = "bilateral"

	bpy.context.scene.rpr.render.denoiser.color_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.normal_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.p_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.trans_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.radius = radius

	render(test_case, script_info)
	return 1

def test_eaw(test_case, script_info, sigma):

	bpy.context.scene.rpr.render.denoiser.filter_type = 'eaw'

	bpy.context.scene.rpr.render.denoiser.color_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.normal_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.depth_sigma = sigma
	bpy.context.scene.rpr.render.denoiser.trans_sigma = sigma

	render(test_case, script_info)
	return 1

def test_lwr(test_case, script_info, param1, param2):

	bpy.context.scene.rpr.render.denoiser.filter_type = 'lwr'

	bpy.context.scene.rpr.render.denoiser.samples = param1
	bpy.context.scene.rpr.render.denoiser.half_window = param1
	bpy.context.scene.rpr.render.denoiser.bandwidth = param2

	render(test_case, script_info)
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_DEN_001", ["Filter type: Bilateral", "Radius: 1", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "bilateral", -1, 1, 0.1],
	["BL_RS_DEN_002", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "bilateral", -1, 25, 0.1],
	["BL_RS_DEN_003", ["Filter type: Bilateral", "Radius: 50", "Color sigma: 0.1", "Normal sigma: 0.1", "ID sigma: 0.1"], "bilateral", -1, 50, 0.1],
	["BL_RS_DEN_004", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 0.5", "Normal sigma: 0.5", "ID sigma: 0.5"], "bilateral", -1, 25, 0.5],
	["BL_RS_DEN_005", ["Filter type: Bilateral", "Radius: 25", "Color sigma: 1", "Normal sigma: 1", "ID sigma: 1"], "bilateral", -1, 25, 1.0],
	["BL_RS_DEN_006", ["Filter type: Local Weighted Regression", "Samples: 4", "Filter radius: 4", "Bandwidth: 0.1"], "lwr", -1, 4, 0.1],
	["BL_RS_DEN_007", ["Filter type: Local Weighted Regression", "Samples: 10", "Filter radius: 10", "Bandwidth: 10"], "lwr", -1, 10, 10 ],
	["BL_RS_DEN_008", ["Filter type: Local Weighted Regression", "Samples: 2.0", "Filter radius: 2.0", "Bandwidth: 1"], "lwr", -1, 2, 1],
	["BL_RS_DEN_009", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 0.1", "Normal sigma: 0.1", "Depth sigma: 0.1", "ID sigma: 0.1"], "eaw", -1, 0.1],
	["BL_RS_DEN_010", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 0.5", "Normal sigma: 0.5", "Depth sigma: 0.5", "ID sigma: 0.5"], "eaw", -1, 0.5],
	["BL_RS_DEN_011", ["Filter type: Edge Avoiding Wavelets", "Color sigma: 1.0", "Normal sigma: 1.0", "Depth sigma: 1.0", "ID sigma: 1.0"], "eaw", -1, 1.0]
	]

	launch_tests()
