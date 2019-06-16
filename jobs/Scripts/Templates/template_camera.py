
def prerender(test_list):

	current_scene = bpy.path.basename(bpy.context.blend_data.filepath)
    if current_scene != test_list[2]:
        bpy.ops.wm.open_mainfile(filepath=os.path.join(r"{resource_path}", test_list[2]))

    scene = bpy.context.scene
    enable_rpr_render(scene)

	bpy.context.scene.objects.active = bpy.data.objects['Camera']
	bpy.context.object.select = False
	bpy.context.scene.objects['Camera'].select = True
	bpy.context.object.data.type = test_list[3]

	if test_list[4]:
		bpy.context.scene.rpr.render.camera.override_camera_settings = True
		bpy.context.scene.rpr.render.camera.panorama_type = test_list[4]
		if test_list[5]:
			bpy.context.scene.rpr.render.camera.stereo = True
	else:
		bpy.context.scene.rpr.render.camera.override_camera_settings = False

	render(test_list[0], test_list[1])
	return 1

if __name__ == "__main__":

	list_tests = [
	["BL_RS_CAM_001", ["Camera Type: Persp"], "Camera.blend", 'PERSP', ""], 
	["BL_RS_CAM_002", ["Camera Type: Ortho"], "Camera.blend", 'ORTHO', ""],
	["BL_RS_CAM_003", ["Camera Type: Pano"], "Camera.blend", 'PANO', ""],
	["BL_RS_CAM_004", ["RPR Camera Type: Perspective, Cubemap"], "Camera.blend", 'PERSP', 'CUBEMAP', False],
	["BL_RS_CAM_005", ["RPR Camera Type: Perspective, Cubemap, Use Stereo Camera"], "Camera.blend", 'PERSP', 'CUBEMAP', True],
	["BL_RS_CAM_006", ["RPR Camera Type: Perspective, Spherical Panorama"], "Camera.blend", 'PERSP', 'SPHERICAL_PANORAMA', False],
	["BL_RS_CAM_007", ["RPR Camera Type: Perspective, Spherical Panorama, Use Stereo Camera"], "Camera.blend", 'PERSP', 'SPHERICAL_PANORAMA', True],
	["BL_RS_CAM_008", ["RPR Camera Type: Orthographic, Cubemap"], "Camera.blend", 'ORTHO', 'CUBEMAP', False],
	["BL_RS_CAM_009", ["RPR Camera Type: Orthographic, Cubemap, Use Stereo Camera"], "Camera.blend", 'ORTHO', 'CUBEMAP', True],
	["BL_RS_CAM_010", ["RPR Camera Type: Orthographic, Spherical Panorama"], "Camera.blend", 'ORTHO', 'SPHERICAL_PANORAMA', False],
	["BL_RS_CAM_011", ["RPR Camera Type: Orthographic, Spherical Panorama, Use Stereo Camera"], "Camera.blend", 'ORTHO', 'SPHERICAL_PANORAMA', True],
	["BL_RS_CAM_012", ["RPR Camera Type: Panoramic, Cubemap"], "Camera.blend", 'PANO', 'CUBEMAP', False],
	["BL_RS_CAM_013", ["RPR Camera Type: Panoramic, Cubemap, Use Stereo Camera"], "Camera.blend", 'PANO', 'CUBEMAP', True],
	["BL_RS_CAM_014", ["RPR Camera Type: Panoramic, Spherical Panorama"], "Camera.blend", 'PANO', 'SPHERICAL_PANORAMA', False],
	["BL_RS_CAM_015", ["RPR Camera Type: Panoramic, Spherical Panorama, Use Stereo Camera"], "Camera.blend", 'PANO', 'SPHERICAL_PANORAMA', True]
	]
	
	launch_tests()





