
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

	bpy.context.scene.objects.active = bpy.data.objects['Point']

	if (test_list[3] == "POINT"):
		return point_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6])

	elif (test_list[3] == "SUN"):    
		return sun_light(test_list[0], test_list[1], test_list[4], test_list[5])

	elif (test_list[3] == "SPOT"):
		return spot_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7])

	elif (test_list[3] == "AREA"):
		return area_light(test_list[0], test_list[1], test_list[4], test_list[5], test_list[6], test_list[7], test_list[8])


def point_light(test_case, script_info, intensity, temperature, ies):

	bpy.context.object.data.type = 'POINT'

	bpy.context.object.data.rpr_lamp.intensity = intensity

	if temperature != "default":
		bpy.context.object.data.rpr_lamp.use_temperature = True
		bpy.context.object.data.rpr_lamp.temperature = temperature
	else:
		bpy.context.object.data.rpr_lamp.use_temperature = False
		bpy.context.object.data.rpr_lamp.temperature = 6500

	if ies:
		ies_path = os.path.join("{res_path}", "ies", ies)
		bpy.context.object.data.rpr_lamp.ies_file_name = ies_path
	else:
		bpy.context.object.data.rpr_lamp.ies_file_name = ""

	render(test_case, script_info)
	return 1


def sun_light(test_case, script_info, intensity, temperature):

	bpy.context.object.data.type = 'SUN'

	bpy.context.object.data.rpr_lamp.intensity = intensity

	if temperature != "default":
		bpy.context.object.data.rpr_lamp.use_temperature = True
		bpy.context.object.data.rpr_lamp.temperature = temperature
	else:
		bpy.context.object.data.rpr_lamp.use_temperature = False
		bpy.context.object.data.rpr_lamp.temperature = 6500

	render(test_case, script_info)
	return 1


def spot_light(test_case, script_info, intensity, temperature, angle, fallof):

	bpy.context.object.data.type = 'SUN'

	bpy.context.object.data.rpr_lamp.intensity = intensity

	if temperature != "default":
		bpy.context.object.data.rpr_lamp.use_temperature = True
		bpy.context.object.data.rpr_lamp.temperature = temperature
	else:
		bpy.context.object.data.rpr_lamp.use_temperature = False
		bpy.context.object.data.rpr_lamp.temperature = 6500

	if angle != "default":
		bpy.context.object.data.rpr_lamp.spot_size = True
	else:
		bpy.context.object.data.rpr_lamp.spot_size = 1.309

	if fallof != "default":
		bpy.context.object.data.rpr_lamp.spot_blend = True
	else:
		bpy.context.object.data.rpr_lamp.spot_blend = 0.15

	render(test_case, script_info)
	return 1


def area_light(test_case, script_info, intensity, temperature, size, visible, mesh_type):

	bpy.context.object.data.type = 'AREA'

	bpy.context.object.data.rpr_lamp.intensity = intensity
	bpy.context.object.data.rpr_lamp.visible = visible

	if temperature != "default":
		bpy.context.object.data.rpr_lamp.use_temperature = True
		bpy.context.object.data.rpr_lamp.temperature = temperature
	else:
		bpy.context.object.data.rpr_lamp.use_temperature = False
		bpy.context.object.data.rpr_lamp.temperature = 6500

	if size != "default":
		bpy.context.object.data.rpr_lamp.size_1 = size
		bpy.context.object.data.rpr_lamp.size_2 = size
	else:
		bpy.context.object.data.rpr_lamp.size_1 = 0.1
		bpy.context.object.data.rpr_lamp.size_2 = 0.1

	if mesh_type != "default":
		bpy.context.object.data.rpr_lamp.shape = mesh_type
		if mesh_type == "MESH":
			bpy.context.object.data.rpr_lamp.mesh_obj = bpy.data.objects["Shaders"]
	else:
		bpy.context.object.data.rpr_lamp.shape = 'RECTANGLE'

	render(test_case, script_info)
	return 1



if __name__ == "__main__":

	list_tests = [
	["BL_L_PL_001", ["Type: Point", "Intensity: 1000"], "Physical_Lights.blend", 'POINT', 1000, "default", ""], 
	["BL_L_PL_002", ["Type: Point", "Intensity: 0, Expected Black Picture"], "Physical_Lights.blend", 'POINT', 0, "default", ""], 
	["BL_L_PL_003", ["Type: Point", "Intensity: 5000"], "Physical_Lights.blend", 'POINT', 5000, "default", ""],
	["BL_L_PL_004", ["Type: Point", "Intensity: 1000", "Temperature: 6500"], "Physical_Lights.blend", 'POINT', 1000, 6500, ""],   
	["BL_L_PL_005", ["Type: Point", "Intensity: 1000", "Temperature: 0"], "Physical_Lights.blend", 'POINT', 1000, 0, ""], 
	["BL_L_PL_006", ["Type: Point", "Intensity: 1000", "Temperature: 40 000"], "Physical_Lights.blend", 'POINT', 1000, 40000, ""], 
	["BL_L_PL_007", ["Type: Point", "Intensity: 1000", "IES file: 2.ies"], "Physical_Lights.blend", 'POINT', 1000, "default", "2.ies"], 
	["BL_L_PL_008", ["Type: SUN", "Intensity: 50"], "Physical_Lights.blend", 'SUN', 50, "default"], 
	["BL_L_PL_009", ["Type: SUN", "Intensity: 1000"], "Physical_Lights.blend", 'SUN', 1000, "default"], 
	["BL_L_PL_010", ["Type: SUN", "Intensity: 0, Expected Black Picture"], "Physical_Lights.blend", 'SUN', 0, "default"],
	["BL_L_PL_011", ["Type: SUN", "Intensity: 5000"], "Physical_Lights.blend", 'SUN', 5000, "default"],  
	["BL_L_PL_012", ["Type: SUN", "Intensity: 1000", "Temperature: 6500"], "Physical_Lights.blend", 'SUN', 1000, 6500], 
	["BL_L_PL_013", ["Type: SUN", "Intensity: 1000", "Temperature: 0"], "Physical_Lights.blend", 'SUN', 1000, 0], 
	["BL_L_PL_014", ["Type: SUN", "Intensity: 1000", "Temperature: 40 000"], "Physical_Lights.blend", 'SUN', 1000, 40000], 
	["BL_L_PL_015", ["Type: SPOT", "Intensity: 2000"], "Physical_Lights.blend", 'SPOT', 2000, "default", "default", "default"], 
	["BL_L_PL_016", ["Type: SPOT", "Intensity: 1000"], "Physical_Lights.blend", 'SPOT', 1000, "default", "default", "default"],
	["BL_L_PL_017", ["Type: SPOT", "Intensity: 0, Expected Black Picture"], "Physical_Lights.blend", 'SPOT', 0, "default", "default", "default"],
	["BL_L_PL_018", ["Type: SPOT", "Intensity: 5000"], "Physical_Lights.blend", 'SPOT', 5000, "default", "default", "default"],
	["BL_L_PL_019", ["Type: SPOT", "Intensity: 1000", "Temperature: 6500"], "Physical_Lights.blend", 'SPOT', 1000, 6500, "default", "default"],
	["BL_L_PL_020", ["Type: SPOT", "Intensity: 1000", "Temperature: 0"], "Physical_Lights.blend", 'SPOT', 1000, 0, "default", "default"],
	["BL_L_PL_021", ["Type: SPOT", "Intensity: 1000", "Temperature: 40 000"], "Physical_Lights.blend", 'SPOT', 1000, 40000, "default", "default"],
	["BL_L_PL_022", ["Type: SPOT", "Intensity: 1000", "Angle: 1"], "Physical_Lights.blend", 'SPOT', 1000, "default", 1, "default"],
	["BL_L_PL_023", ["Type: SPOT", "Intensity: 1000", "Angle: 180"], "Physical_Lights.blend", 'SPOT', 1000, "default", 180, "default"],
	["BL_L_PL_024", ["Type: SPOT", "Intensity: 1000", "Falloff: 0"], "Physical_Lights.blend", 'SPOT', 1000, "default", "default", 0],
	["BL_L_PL_025", ["Type: SPOT", "Intensity: 1000", "Falloff: 1"], "Physical_Lights.blend", 'SPOT', 1000, "default", "default", 1],
	["BL_L_PL_026", ["Type: AREA", "Intensity: 300"], "Physical_Lights.blend", 'AREA', 300, "default", "default", 0, "default"],
	["BL_L_PL_027", ["Type: AREA", "Intensity: 1000"], "Physical_Lights.blend", 'AREA', 1000, "default", "default", 0, "default"],
	["BL_L_PL_028", ["Type: AREA", "Intensity: 0, Expected Black Picture"], "Physical_Lights.blend", 'AREA', 0, "default", "default", 0, "default"],
	["BL_L_PL_029", ["Type: AREA", "Intensity: 5000"], "Physical_Lights.blend", 'AREA', 5000, "default", "default", 0, "default"],
	["BL_L_PL_030", ["Type: AREA", "Intensity: 1000, Expected Black Picture", "Width, Height: 0"], "Physical_Lights.blend", 'AREA', 1000, "default", 0, 0, "default"],
	["BL_L_PL_031", ["Type: AREA", "Intensity: 1000", "Width, Height: 100"], "Physical_Lights.blend", 'AREA', 1000, "default", 100, 0, "default"],
	["BL_L_PL_032", ["Type: AREA", "Intensity: 1000", "Width, Height: 100", "Visible: active"], "Physical_Lights.blend", 'AREA', 1000, "default", 100, 1, "default"],
	["BL_L_PL_033", ["Type: AREA", "Intensity: 1000", "Mesh type: Cylinder"], "Physical_Lights.blend", 'AREA', 1000, "default", "default", 0, "CYLINDER"],
	["BL_L_PL_034", ["Type: AREA", "Intensity: 1000", "Mesh type: Sphere"], "Physical_Lights.blend", 'AREA', 1000, "default", "default", 0, "SPHERE"],
	["BL_L_PL_035", ["Type: AREA", "Intensity: 1000", "Mesh type: Disc"], "Physical_Lights.blend", 'AREA', 1000, "default", "default", 0, "DISC"],
	["BL_L_PL_036", ["Type: AREA", "Intensity: 1000", "Mesh type: Mesh"], "Physical_Lights.blend", 'AREA', 1000, "default", "default", 0, "MESH"],
	["BL_L_PL_037", ["Type: AREA", "Intensity: 1000", "Temperature: 0"], "Physical_Lights.blend", 'AREA', 1000, 0, "default", 0, "default"],
	["BL_L_PL_038", ["Type: AREA", "Intensity: 1000", "Temperature: 40 000"], "Physical_Lights.blend", 'AREA', 1000, 40000, "default", 0, "default"],
	]

	launch_tests()
