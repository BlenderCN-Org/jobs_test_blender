import bpy
import addon_utils
import datetime
import sys
import json
import os
from rprblender import node_editor
from rprblender import material_browser
from rprblender import helpers
from pyrpr import API_VERSION

def core_ver_str():
    core_ver = API_VERSION
    mj = (core_ver & 0xFFFF00000) >> 28
    mn = (core_ver & 0xFFFFF) >> 8
    return "%x.%x" % (mj, mn)

def render(*argv):

	#get scene name
	Scenename = bpy.context.scene.name

	# RPR Settings
	if((addon_utils.check("rprblender"))[0] == False) : 
	    addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	bpy.data.scenes[Scenename].render.engine = "RPR"

	device_name = ""
	# Render device in RPR
	if '{render_mode}' == 'dual':
		device_name = "CPU0" + " + " + helpers.render_resources_helper.get_used_devices()
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type_plus_cpu = True
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type = 'gpu'
	elif '{render_mode}' == 'cpu':
		device_name = "CPU0"
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type = '{render_mode}'
		bpy.context.user_preferences.addons["rprblender"].preferences.settings.device_type_plus_cpu = False
	elif '{render_mode}' == 'gpu':
		device_name = helpers.render_resources_helper.get_used_devices()
	bpy.context.user_preferences.addons["rprblender"].preferences.settings.include_uncertified_devices = True

	# frame range
	bpy.data.scenes[Scenename].frame_start = 1
	bpy.data.scenes[Scenename].frame_end = 1

	# image format
	bpy.data.scenes[Scenename].render.image_settings.quality = 100
	bpy.data.scenes[Scenename].render.image_settings.color_mode = 'RGB'

	name_scene = ""
	if (len(argv) == 1):
		name_scene = argv[0]
		test_case = argv[0]
	else:
		name_scene = bpy.path.basename(bpy.context.blend_data.filepath).split('.')[0]
		test_case = "None"
		for arg in argv:
			name_scene += "_"
			name_scene += str(arg)

	# output
	output = r"{work_dir}" + "/Color/" + name_scene
	bpy.data.scenes[Scenename].render.filepath = output 
	bpy.data.scenes[Scenename].render.use_placeholder = True
	bpy.data.scenes[Scenename].render.use_file_extension = True
	bpy.data.scenes[Scenename].render.use_overwrite = True

	# start render animation
	TIMER = datetime.datetime.now()
	bpy.ops.render.render(write_still=True,scene=Scenename)
	Render_time = datetime.datetime.now() - TIMER

	# get version of rpr addon
	for mod_name in bpy.context.user_preferences.addons.keys():
	    if (mod_name == 'rprblender') : 
	        mod = sys.modules[mod_name]
	        ver = mod.bl_info.get('version')
	        version = str(ver[0]) + "." + str(ver[1]) + "." + str(ver[2])
	    
	image_format = (bpy.data.scenes[Scenename].render.image_settings.file_format).lower()
	if (image_format == 'jpeg'):
		image_format = 'jpg'

	# LOG
	name_scene_for_json = name_scene + "_RPR"
	log_name = os.path.join(r'{work_dir}', name_scene_for_json + ".json")
	report = {{}}
	report['render_version'] = version
	report['render_mode'] = '{render_mode}'
	report['core_version'] = core_ver_str()
	report['render_device'] = device_name
	report['test_group'] = "{package_name}"
	report['tool'] = "Blender " + bpy.app.version_string.split(" (")[0]
	report['file_name'] = name_scene + "." + image_format
	report['scene_name'] = bpy.path.basename(bpy.context.blend_data.filepath)
	report['render_time'] = Render_time.total_seconds()
	report['render_color_path'] = r"Color/" + name_scene + "." + image_format
	report['date_time'] = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
	report['difference_color'] = "not compared yet"
	report['test_case'] = test_case


	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')

