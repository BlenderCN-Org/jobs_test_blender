
def prerender(test_list):

	scene = bpy.path.basename(bpy.context.blend_data.filepath)
	if scene != test_list[4]:
		bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{res_path}", test_list[4]))

	Scenename = bpy.context.scene.name

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	bpy.context.scene.rpr.use_render_stamp = False
	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = test_list[5]
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'
	
	if (bpy.path.basename(bpy.context.blend_data.filepath) == test_list[4]):

		if (test_list[2] != "pass"):
			test_list[2]()
			render(test_list[0], test_list[1])
			test_list[3]()			

		else:
			create_report(test_list[0], test_list[1], "pass")

		return 1


def delete_hierarchy(obj):
	names = set([obj.name])
	def get_child_names(obj):
		for child in obj.children:
			names.add(child.name)
			if child.children:
				get_child_names(child)

	get_child_names(obj)
	objects = bpy.data.objects
	[setattr(objects[n], 'select', True) for n in names]
	bpy.ops.object.delete()


def empty():
	pass


def check_rpr_load():
	if((addon_utils.check("rprblender"))[0] == False) : 
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)


def import_fbx():
	bpy.context.scene.render.engine = 'RPR'
	bpy.context.scene.world.rpr_data.environment.enable = True

	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects['Cube'].select = True
	bpy.ops.object.delete() 

	file_loc = os.path.join("{res_path}", "park_bench1.fbx")
	imported_object = bpy.ops.import_scene.fbx(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0] 
	bpy.data.objects["Default"].scale = (0.15, 0.15, 0.15)
	bpy.data.objects["Default"].location = (0, 0, 0)


def delete_fbx():
	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects["Default"].select = True
	bpy.context.scene.objects.active = bpy.data.objects["Default"]
	delete_hierarchy(bpy.context.active_object)


def import_obj():
	file_loc = os.path.join("{res_path}", "example.obj")
	imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0] 
	bpy.data.objects["shader_ball"].dimensions = (3, 3, 3)
	bpy.data.objects["shader_ball"].location = (0, 0, 0)


def delete_obj():
	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects["shader_ball"].select = True
	bpy.context.scene.objects.active = bpy.data.objects["shader_ball"]
	delete_hierarchy(bpy.context.active_object)


def create_IBL():
	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'COLOR'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = False


def update_IBL_hdr():
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
	ibl_map = os.path.join("{res_path}", "Tropical_Beach_3k.hdr")
	bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)


def update_IBL_exr():
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
	ibl_map = os.path.join("{res_path}", "ibl_test.exr")
	bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)


def delete_map_IBL():
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'COLOR'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = False

def create_sun_sky():
	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'SUN_SKY'
	bpy.context.scene.world.rpr_data.environment.sun_sky.altitude = 1.5708


def delete_sun_sky():
	bpy.context.scene.world.rpr_data.environment.enable = False


def create_ies_light():
	ies = os.path.join("{res_path}", "ies", "1.ies")
	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = ies
	bpy.context.object.data.rpr_lamp.intensity = 100


def delete_ies_light():
	bpy.context.object.data.rpr_lamp.ies_file_name = ""


def activate_render_stamp():
	bpy.data.scenes['Scene'].rpr.use_render_stamp = True


def deactivate_render_stamp():
	bpy.data.scenes['Scene'].rpr.use_render_stamp = False


def activate_wireframe_mode():
	bpy.context.scene.rpr.render.render_mode = 'WIREFRAME'


def deactivate_wireframe_mode():
	bpy.context.scene.rpr.render.render_mode = 'GLOBAL_ILLUMINATION'


def change_image_size_hd720():
	bpy.data.scenes['Scene'].render.resolution_x = 1280
	bpy.data.scenes['Scene'].render.resolution_y = 720


def change_image_size_custom():
	bpy.data.scenes['Scene'].render.resolution_x = 1500
	bpy.data.scenes['Scene'].render.resolution_y = 1125


def change_image_size_default():
	bpy.data.scenes['Scene'].render.resolution_x = 1920
	bpy.data.scenes['Scene'].render.resolution_y = 1080


def activate_jpg_format():
	bpy.data.scenes['Scene'].render.image_settings.file_format = 'JPEG'


def activate_png_format():
	bpy.data.scenes['Scene'].render.image_settings.file_format = 'PNG'


def activate_denoiser_bilateral():
	bpy.context.scene.rpr.render.denoiser.enable = True
	bpy.context.scene.rpr.render.denoiser.filter_type = 'bilateral'


def activate_denoiser_lwr():
	bpy.context.scene.rpr.render.denoiser.enable = True
	bpy.context.scene.rpr.render.denoiser.filter_type = 'lwr'


def activate_denoiser_eaw():
	bpy.context.scene.rpr.render.denoiser.enable = True
	bpy.context.scene.rpr.render.denoiser.filter_type = 'eaw'


def deactivate_denoiser():
	bpy.context.scene.rpr.render.denoiser.enable = False


def import_rpr_matlib():
	check_rpr_load()
	material_name= 'Gold.xml'
	matlib_path = os.path.join(material_browser.RPRMaterialLibrary().get_library_path(), material_name.split('.')[0], material_name)
	material = bpy.data.materials['Material']
	material_browser.import_xml_material(matlib_path, material)

	bpy.data.objects['shader_ball'].material_slots[0].material = bpy.data.materials['Material']


def activate_aov():
	pass


def deactivate_aov():
	pass


def create_area_light():
	bpy.context.scene.objects.active = bpy.data.objects['Lamp']
	bpy.context.object.data.type = 'AREA'


def delete_area_light():
	bpy.context.object.data.type = 'POINT'


def activate_medium_quality():
	bpy.context.scene.rpr.render.global_illumination.max_ray_depth = 15
	bpy.context.scene.rpr.render.global_illumination.max_refraction_depth = 10
	bpy.context.scene.rpr.render.global_illumination.use_clamp_irradiance = True
	bpy.context.scene.rpr.render.global_illumination.clamp_irradiance = 1.0


def deactivate_medium_quality():
	bpy.context.scene.rpr.render.global_illumination.max_ray_depth = 8
	bpy.context.scene.rpr.render.global_illumination.max_refraction_depth = 5


def create_and_assign_uber():
	check_rpr_load()

	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = bpy.data.objects['shader_ball']
	bpy.context.scene.objects['shader_ball'].select = True

	material = bpy.data.materials.new('Uber2')
	mesh = bpy.context.object.data
	
	override = bpy.context.copy()
	override['material'] = material
	bpy.ops.rpr.op_material_add_nodetree(override)
	tree = material.node_tree

	output = node_editor.find_node_in_nodetree(tree, node_editor.shader_node_output_name)
	uber2 = tree.nodes.new(type='rpr_shader_node_uber2')
	tree.links.new(uber2.outputs[uber2.shader_out], output.inputs[output.shader_in])

	uber2.diffuse = True
	uber2.inputs[uber2.diffuse_color].default_value = (0.65, 0.2, 0.2, 1.0)
	uber2.inputs[uber2.diffuse_weight].default_value = 1

	bpy.data.objects['shader_ball'].material_slots[0].material = bpy.data.materials['Uber2']



def create_and_assign_pbr():
	check_rpr_load()

	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = bpy.data.objects['shader_ball']
	bpy.context.scene.objects['shader_ball'].select = True

	material = bpy.data.materials.new('PBR')
	mesh = bpy.context.object.data
		
	override = bpy.context.copy()
	override['material'] = material
	bpy.ops.rpr.op_material_add_nodetree(override)
	tree = material.node_tree

	output = node_editor.find_node_in_nodetree(tree, node_editor.shader_node_output_name)
	pbr = tree.nodes.new(type='rpr_shader_node_pbr')
	tree.links.new(pbr.outputs[pbr.shader_out], output.inputs[output.shader_in])

	bpy.data.objects['shader_ball'].material_slots[0].material = bpy.data.materials['PBR']

	
if __name__ == '__main__':

	list_tests = [
	["BL_SM_001", ["Install RPR"], "pass", "pass", "rpr_default.blend", 1],
	["BL_SM_002", ["Select RPR"], "pass", "pass", "rpr_default.blend", 1],
	["BL_SM_003", ["Open RPR scene"], "pass", "pass", "rpr_default.blend", 1],
	["BL_SM_004", ["Render empty scene", "Pass Limit: 50"], empty, empty, "rpr_default.blend", 50],
	["BL_SM_005", ["IES", "Pass Limit: 50"], create_ies_light, delete_ies_light, "IES.blend", 50],
	["BL_SM_006", ["Import FBX", "Pass Limit: 50"], import_fbx, delete_fbx, "default.blend", 50],
	["BL_SM_007", ["Import OBJ", "Pass Limit: 50"], import_obj, empty, "default.blend", 50],
	["BL_SM_008", ["Uber2 material", "Pass Limit: 50"], create_and_assign_uber, empty, "default.blend", 50],
	["BL_SM_009", ["Sun_Sky", "Pass Limit: 50"], create_sun_sky, delete_sun_sky, "default.blend", 50],
	["BL_SM_010", ["IBL", "Pass Limit: 50"], create_IBL, empty, "default.blend", 50],
	["BL_SM_011", ["IBL with HDR", "Pass Limit: 50"], update_IBL_hdr, empty, "default.blend", 50],
	["BL_SM_012", ["IBL with EXR", "Pass Limit: 50"], update_IBL_exr, delete_map_IBL, "default.blend", 50],
	["BL_SM_013", ["Render 1 pass"], empty, empty, "default.blend", 1],
	["BL_SM_014", ["Render 100 pass"], empty, empty, "default.blend", 100],
	["BL_SM_015", ["Render 500 pass"], empty, empty, "default.blend", 500],
	["BL_SM_018", ["Render Stamp", "Pass Limit: 50"], activate_render_stamp, deactivate_render_stamp, "default.blend", 50],
	["BL_SM_019", ["Render mode wireframe", "Pass Limit: 50"], activate_wireframe_mode, deactivate_wireframe_mode, "default.blend", 50],
	["BL_SM_020", ["Image size 720HD", "Pass Limit: 50"], change_image_size_hd720, empty, "default.blend", 50],
	["BL_SM_021", ["Image size 1500 1125", "Pass Limit: 50"], change_image_size_custom, change_image_size_default, "default.blend", 50],
	["BL_SM_022", ["PNG format", "Pass Limit: 50"], activate_png_format, empty, "default.blend", 50],	
	["BL_SM_023", ["JPG format", "Pass Limit: 50"], activate_jpg_format, empty, "default.blend", 50],
	["BL_SM_024", ["Denoiser EAW", "Pass Limit: 50"], activate_denoiser_eaw, deactivate_denoiser, "default.blend", 50],
	["BL_SM_025", ["Denoiser LWR", "Pass Limit: 50"], activate_denoiser_lwr, deactivate_denoiser, "default.blend", 50],
	["BL_SM_026", ["Denoiser Bilateral", "Pass Limit: 50"], activate_denoiser_bilateral, deactivate_denoiser, "default.blend", 50],
	["BL_SM_027", ["PBR", "Pass Limit: 50"], create_and_assign_pbr, empty, "default.blend", 50],
	["BL_SM_028", ["Mat lib", "Pass Limit: 50"], import_rpr_matlib, empty, "default.blend", 50],
	["BL_SM_029", ["AOV Geometric Normal", "Pass Limit: 50"], activate_aov, deactivate_aov, "default.blend", 50],
	["BL_SM_030", ["Area light", "Pass Limit: 50"], create_area_light, delete_area_light, "default.blend", 50],
	["BL_SM_031", ["Instances", "Pass Limit: 50"], empty, empty, "Instances.blend", 50],
	["BL_SM_032", ["5 lights", "Pass Limit: 50"], empty, empty, "5_lights.blend", 50],
	["BL_SM_033", ["AOV SC", "Pass Limit: 50"], empty, empty, "AOV_SC.blend", 50],
	["BL_SM_034", ["SSS", "Pass Limit: 50"], empty, empty, "SSS_Test.blend", 50]
	# ["BL_SM_035", ["Displacement", "Pass Limit: 50"], empty, empty, "Displacement.blend", 50],
	# ["BL_SM_036", ["Quality", "Pass Limit: 50"], activate_medium_quality, deactivate_medium_quality, "WaterInsideGlass.blend", 50]
	]

	launch_tests()

