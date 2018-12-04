
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

	bpy.context.scene.world.rpr_data.environment.type = 'SUN_SKY'
	bpy.context.scene.world.rpr_data.environment.sun_sky.type = test_list[3]
	bpy.context.scene.world.rpr_data.environment.sun_sky.ground_color = (0.4, 0.00703741, 0.00508468)
	bpy.context.scene.world.rpr_data.environment.sun_sky.texture_resolution = test_list[4]

	if (test_list[3] == 'analytical_sky'):
		bpy.context.scene.world.rpr_data.environment.sun_sky.azimuth = test_list[5]
		bpy.context.scene.world.rpr_data.environment.sun_sky.altitude = test_list[6]
	elif (test_list[3] == 'date_time_location'):
		bpy.ops.rpr.op_get_time_now()

		if (test_list[7] == "Moscow"):
			bpy.context.scene.world.rpr_data.environment.sun_sky.time_zone = 3
			bpy.context.scene.world.rpr_data.environment.sun_sky.latitude = 0.973583
			bpy.context.scene.world.rpr_data.environment.sun_sky.longitude = 0.656516
		elif (test_list[7] == "Canberra"):
			bpy.context.scene.world.rpr_data.environment.sun_sky.time_zone = 11
			bpy.context.scene.world.rpr_data.environment.sun_sky.latitude = -0.615752
			bpy.context.scene.world.rpr_data.environment.sun_sky.longitude = 2.60277
		elif (test_list[7] == "Miami_Beach"):
			bpy.context.scene.world.rpr_data.environment.sun_sky.time_zone = -5
			bpy.context.scene.world.rpr_data.environment.sun_sky.latitude = 0.450131
			bpy.context.scene.world.rpr_data.environment.sun_sky.longitude = -1.39853

		bpy.context.scene.world.rpr_data.environment.sun_sky.time_hours = test_list[5]
		bpy.context.scene.world.rpr_data.environment.sun_sky.time_minutes = test_list[6]

	render(test_list[0], test_list[1])
	return 1


if __name__ == "__main__":

	list_tests = [
	["BL_RS_SS_001", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'analytical_sky', 'normal', 0, 0],
	["BL_RS_SS_002", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 0, 0.785398],
	["BL_RS_SS_003", ["Sun&Sky System: Analytical sky", "Azimuth: 0", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 0, 1.5708],
	["BL_RS_SS_004", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'analytical_sky', 'normal', 1.5708, 0],
	["BL_RS_SS_005", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 1.5708, 0.785398],
	["BL_RS_SS_006", ["Sun&Sky System: Analytical sky", "Azimuth: 90", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 1.5708, 1.5708],
	["BL_RS_SS_007", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'analytical_sky', 'normal', 3.14159, 0],
	["BL_RS_SS_008", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 3.14159, 0.785398],
	["BL_RS_SS_009", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 3.14159, 1.5708],
	["BL_RS_SS_010", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'analytical_sky', 'normal', 4.71239, 0],
	["BL_RS_SS_011", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 4.71239, 0.785398],
	["BL_RS_SS_012", ["Sun&Sky System: Analytical sky", "Azimuth: 270", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 4.71239, 1.5708],
	["BL_RS_SS_013", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'analytical_sky', 'normal', 6.28319, 0],
	["BL_RS_SS_014", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 6.28319, 0.785398],
	["BL_RS_SS_015", ["Sun&Sky System: Analytical sky", "Azimuth: 360", "Altitude: 90", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 6.28319, 1.5708],
	["BL_RS_SS_016", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'date_time_location', 'normal', 0, 1, "Moscow"],
	["BL_RS_SS_017", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 6", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'date_time_location', 'normal', 6, 1, "Moscow"],
	["BL_RS_SS_018", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 12", "Texture Resolution: normal"], "TestSunSky.blend", 'date_time_location', 'normal', 12, 1, "Moscow"],
	["BL_RS_SS_019", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 18", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'date_time_location', 'normal', 18, 1, "Moscow"],
	["BL_RS_SS_020", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 24", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'date_time_location', 'normal', 24, 1, "Moscow"],
	["BL_RS_SS_021", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 12", "Texture Resolution: small"], "TestSunSky.blend", 'date_time_location', 'small', 12, 0, "Moscow"],
	["BL_RS_SS_022", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 12", "Texture Resolution: normal"], "TestSunSky.blend", 'date_time_location', 'normal', 12, 0, "Moscow"],
	["BL_RS_SS_023", ["Sun&Sky System: Date, Time and Location", "Location: Moscow", "Hour: 12", "Texture Resolution: high"], "TestSunSky.blend", 'date_time_location', 'high', 12, 0, "Moscow"],
	["BL_RS_SS_024", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: small"], "TestSunSky.blend", 'analytical_sky', 'small', 3.14159, 0.785398],
	["BL_RS_SS_025", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: normal"], "TestSunSky.blend", 'analytical_sky', 'normal', 3.14159, 0.785398],
	["BL_RS_SS_026", ["Sun&Sky System: Analytical sky", "Azimuth: 180", "Altitude: 45", "Texture Resolution: high"], "TestSunSky.blend", 'analytical_sky', 'high', 3.14159, 0.785398],
	["BL_RS_SS_027", ["Sun&Sky System: Date, Time and Location", "Location: Miami Beach", "Hour: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'date_time_location', 'normal', 0, 1, "Miami_Beach"],
	["BL_RS_SS_028", ["Sun&Sky System: Date, Time and Location", "Location: Miami Beach", "Hour: 12", "Texture Resolution: normal"], "TestSunSky.blend", 'date_time_location', 'normal', 12, 1, "Miami_Beach"],
	["BL_RS_SS_029", ["Sun&Sky System: Date, Time and Location", "Location: Miami Beach", "Hour: 24", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'date_time_location', 'normal', 24, 1, "Miami_Beach"],
	["BL_RS_SS_030", ["Sun&Sky System: Date, Time and Location", "Location: Canberra", "Hour: 0", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'date_time_location', 'normal', 0, 1, "Canberra"],
	["BL_RS_SS_031", ["Sun&Sky System: Date, Time and Location", "Location: Canberra", "Hour: 12", "Texture Resolution: normal"], "TestSunSky.blend", 'date_time_location', 'normal', 12, 1, "Canberra"],
	["BL_RS_SS_032", ["Sun&Sky System: Date, Time and Location", "Location: Canberra", "Hour: 24", "Texture Resolution: normal, Expected Black Picture"], "TestSunSky.blend", 'date_time_location', 'normal', 24, 1, "Canberra"]
	]

	launch_tests()

