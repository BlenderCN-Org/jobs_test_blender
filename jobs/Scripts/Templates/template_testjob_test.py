import random

def prerender(test_list):

	Scenename = bpy.context.scene.name

	bpy.data.scenes[Scenename].rpr.render.rendering_limits.iterations = test_list[4]
	bpy.data.scenes[Scenename].render.image_settings.file_format = 'JPEG'

	if ({resolution_x} and {resolution_y}):
		bpy.data.scenes[Scenename].render.resolution_x = {resolution_x}
		bpy.data.scenes[Scenename].render.resolution_y = {resolution_y}

	if (bpy.path.basename(bpy.context.blend_data.filepath) == test_list[3]):

		if (test_list[2] != "pass"):
			test_list[2]()
	
		render(test_list[0], test_list[1])

		if (test_list[2] == "pass"):
			if not os.path.exists("{work_dir}" + "/Color"):
   				os.makedirs("{work_dir}" + "/Color")
			copyfile("{work_dir}" + "/../../../../jobs/Tests/pass.jpg", "{work_dir}/Color/" + test_list[0] + ".jpg")
			return 1

		return 1

def delete_hierarchy(obj):

	names = set([obj.name])
	def get_child_names(obj):
		for child in obj.children:
			names.add(child.name)
			if child.children:
				get_child_names(child)

	get_child_names(obj)

	print(names)
	objects = bpy.data.objects
	[setattr(objects[n], 'select', True) for n in names]
	bpy.ops.object.delete()

def empty():
	pass

def test_IES():

	ies = os.path.join("{res_path}", "Candle.fbm", "PD6R12ED010- PDM6835-694SNB.ies")
	bpy.data.lamps["Lamp"].rpr_lamp.ies_file_name = ies

def test_base_light():

	bpy.context.scene.world.rpr_data.environment.enable = False

def test_IBL_on():

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'COLOR'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = False

def test_IBL_exr():

	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
	ibl_map = os.path.join("{res_path}", "ibl_test.exr")
	bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)

def test_IBL_hdr():

	bpy.context.scene.world.rpr_data.environment.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.type = 'IBL'
	bpy.context.scene.world.rpr_data.environment.ibl.use_ibl_map = True
	ibl_map = os.path.join("{res_path}", "Tropical_Beach_3k.hdr")
	bpy.context.scene.world.rpr_data.environment.ibl.ibl_image = bpy.data.images.load(ibl_map, True)

def test_IBL_off():

	bpy.context.scene.world.rpr_data.environment.enable = False

def test_Sun():

	bpy.context.scene.world.rpr_data.environment.enable = True
	bpy.context.scene.world.rpr_data.environment.type = 'SUN_SKY'
	bpy.context.scene.world.rpr_data.environment.sun_sky.altitude = 1.5708

def import_fbx_test():

	bpy.context.scene.render.engine = 'RPR'
	bpy.context.scene.world.rpr_data.environment.enable = True

	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects['Cube'].select = True
	bpy.ops.object.delete()

	file_loc = os.path.join("{res_path}", "wmill.fbx")
	imported_object = bpy.ops.import_scene.fbx(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0]
	bpy.data.objects["Default"].scale = (0.002, 0.002, 0.002)
	bpy.data.objects["Default"].location = (0.3, 0.3, -1)

def import_obj_test():

	bpy.context.scene.render.engine = 'RPR'
	bpy.context.scene.world.rpr_data.environment.enable = True

	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects["Default"].select = True
	bpy.context.scene.objects.active = bpy.data.objects["Default"]
	delete_hierarchy(bpy.context.active_object)

	file_loc = os.path.join("{res_path}", "globe.obj")
	imported_object = bpy.ops.import_scene.obj(filepath=file_loc)
	obj_object = bpy.context.selected_objects[0]
	bpy.data.objects["Sphere001"].rotation_euler[2] = 1.30
	bpy.data.objects["Sphere001"].dimensions = (5, 5, 5)
	bpy.data.objects["Sphere001"].location = (0.2, 0.2, -0.5)


def test_Uber2():

	if((addon_utils.check("rprblender"))[0] == False) :
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)

	bpy.ops.object.select_all(action='DESELECT')
	bpy.context.scene.objects.active = bpy.data.objects['Sphere001']
	bpy.context.scene.objects['Sphere001'].select = True

	material = bpy.data.materials.new('Shader_mat')
	mesh = bpy.context.object.data

	override = bpy.context.copy()
	override['material'] = material
	bpy.ops.rpr.op_material_add_nodetree(override)
	tree = material.node_tree

	output = node_editor.find_node_in_nodetree(tree, node_editor.shader_node_output_name)
	uber2 = tree.nodes.new(type='rpr_shader_node_uber2')
	tree.links.new(uber2.outputs[uber2.shader_out], output.inputs[output.shader_in])

	uber2.diffuse = True
	uber2.inputs[uber2.diffuse_color].default_value = (0.12, 1.66, 0.12, 1.0)
	uber2.inputs[uber2.diffuse_weight].default_value = 1

	bpy.data.objects['Sphere001'].material_slots[0].material = bpy.data.materials['Shader_mat']

def create_spheres_test():

	bpy.context.scene.render.engine = 'RPR'
	bpy.context.scene.world.rpr_data.environment.enable = True

	bpy.ops.object.select_all(action='DESELECT')
	bpy.data.objects["Sphere001"].select = True
	bpy.context.scene.objects.active = bpy.data.objects["Sphere001"]
	delete_hierarchy(bpy.context.active_object)

	bpy.context.scene.objects.active = bpy.data.objects["Lamp"]
	bpy.context.object.location[0] = 0
	bpy.context.object.location[1] = 0
	bpy.context.object.location[2] = 5

	bpy.context.scene.objects.active = bpy.data.objects["Camera"]
	bpy.context.object.location[0] = 0
	bpy.context.object.location[1] = 0
	bpy.context.object.location[2] = 10
	bpy.context.object.rotation_euler[0] = 0
	bpy.context.object.rotation_euler[2] = 0

	for n in range(300):
		bpy.ops.mesh.primitive_uv_sphere_add(size=0.1, location=(
			random.uniform(-4.5, 4.5),
			random.uniform(-2.5, 2.5),
			random.uniform(0.0, 3.0)))


if __name__ == '__main__':

	list_tests = [
	['BL_TJ_001', ["Install RPR"], "pass", "default.blend", 1],
	['BL_TJ_002', ["Open empty scene"], "pass", "default.blend", 1],
	['BL_TJ_003', ["Render empty scene", "Pass Limit: 50"], empty, "default.blend", 50],
	['BL_TJ_004', ["Open rpr empty scene"], "pass", "rpr_default.blend", 1],
	['BL_TJ_005', ["Render empty scene with RPR parameters", "Pass Limit: 50"], empty, "rpr_default.blend", 50],
	["BL_TJ_006", ["Import FBX", "Pass Limit: 50"], import_fbx_test, "rpr_default.blend", 50],
	["BL_TJ_007", ["Import OBJ", "Pass Limit: 50"], import_obj_test, "rpr_default.blend", 50],
	['BL_TJ_008', ["Open Mat edit"], "pass", "rpr_default.blend", 1],
	['BL_TJ_009', ["Create an Uber material"], "pass", "rpr_default.blend", 1],
	["BL_TJ_010", ["Assign Uber material", "Pass Limit: 50"], test_Uber2, "rpr_default.blend", 50],
	["BL_TJ_011", ["Testing base light", "Pass Limit: 50"], test_base_light, "rpr_default.blend", 50],
	# ["BL_TJ_012", ["Testing IES light", "Pass Limit: 50"], test_IES, "rpr_default.blend", 50],
	# ["BL_TJ_013", ["Testing Sun and Sky System", "Pass Limit: 50"], test_Sun, "rpr_default.blend", 50],
	# ["BL_TJ_014", ["Testing IBL", "Pass Limit: 50"], test_IBL_on, "rpr_default.blend", 50],
	# ["BL_TJ_015", ["Testing IBL with hdr", "Pass Limit: 50"], test_IBL_hdr, "rpr_default.blend", 50],
	# ["BL_TJ_016", ["Testing IBL with exr", "Pass Limit: 50"], test_IBL_exr, "rpr_default.blend", 50],
	["BL_TJ_017", ["Import OBJ", "Pass Limit: 50"], create_spheres_test, "rpr_default.blend", 50]
	]

	launch_tests()

