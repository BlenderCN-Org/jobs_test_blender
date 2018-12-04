import bpy
import addon_utils
import datetime
import sys
import json
import os
import logging
from rprblender import node_editor
from rprblender import material_browser
from rprblender import helpers
from pyrpr import API_VERSION
from shutil import copyfile


def core_ver_str():
	core_ver = API_VERSION
	mj = (core_ver & 0xFFFF00000) >> 28
	mn = (core_ver & 0xFFFFF) >> 8
	return "%x.%x" % (mj, mn)


def set_value(path, name, value):
	if hasattr(path, name):
		setattr(path, name, value)
	else:
		logging.warning("No attribute found ")


def render(*argv):

	# get scene name
	scene_name, scene = helpers.get_current_scene()

	if ((addon_utils.check("rprblender"))[0] == False):
		addon_utils.enable("rprblender", default_set=True, persistent=False, handle_error=None)
	set_value(scene.render, 'engine', "RPR")

	# Render device in RPR
	set_value(helpers.get_user_settings(), "include_uncertified_devices", True)
	if '{render_mode}' == 'dual':
		helpers.set_render_devices(use_cpu=True, use_gpu=True)
	elif '{render_mode}' == 'cpu':
		helpers.set_render_devices(use_cpu=True, use_gpu=False)
	elif '{render_mode}' == 'gpu':
		helpers.set_render_devices(use_cpu=False, use_gpu=True)
	
	device_name = helpers.render_resources_helper.get_used_devices()

	# image format
	set_value(scene.render.image_settings, 'quality', 100)
	set_value(scene.render.image_settings, 'compression', 0)
	set_value(scene.render.image_settings, 'color_mode', 'RGB')

	name_scene = argv[0]
	script_info = argv[1]

	set_value(scene.render, 'filepath', r"{work_dir}" + "/Color/" + name_scene)
	set_value(scene.render, 'use_placeholder', True)
	set_value(scene.render, 'use_file_extension', True)
	set_value(scene.render, 'use_overwrite', True)

	# start render animation
	TIMER = datetime.datetime.now()
	bpy.ops.render.render(write_still=True, scene=scene_name)
	Render_time = datetime.datetime.now() - TIMER

	# get version of rpr addon
	for mod_name in bpy.context.user_preferences.addons.keys():
		if (mod_name == 'rprblender'):
			mod = sys.modules[mod_name]
			ver = mod.bl_info.get('version')
			version = str(ver[0]) + "." + str(ver[1]) + "." + str(ver[2])


	image_format = bpy.data.scenes[scene_name].render.image_settings.file_format
	if image_format == 'JPEG':
		image_format = 'jpg'
	elif image_format == 'PNG':
		image_format = 'png'
	else:
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
	report['date_time'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
	report['difference_color'] = "not compared yet"
	report['test_case'] = name_scene
	report['script_info'] = script_info
	report['test_status'] = "undefined"

	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')


def create_report(*argv):
	
	# get scene name
	scene_name, scene = helpers.get_current_scene()

	# Render device in RPR
	set_value(helpers.get_user_settings(), "include_uncertified_devices", True)
	if '{render_mode}' == 'dual':
		helpers.set_render_devices(use_cpu=True, use_gpu=True)
	elif '{render_mode}' == 'cpu':
		helpers.set_render_devices(use_cpu=True, use_gpu=False)
	elif '{render_mode}' == 'gpu':
		helpers.set_render_devices(use_cpu=False, use_gpu=True)
	
	device_name = helpers.render_resources_helper.get_used_devices()

	name_scene = argv[0]
	test_case = argv[0]
	script_info = argv[1]
	picture = argv[2]

	# output
	copyfile(r"{work_dir}" + "/../../../../jobs/Tests/" + picture + ".jpg", r"{work_dir}/Color/" + test_case + ".jpg")

	# get version of rpr addon
	for mod_name in bpy.context.user_preferences.addons.keys():
		if (mod_name == 'rprblender'):
			mod = sys.modules[mod_name]
			ver = mod.bl_info.get('version')
			version = str(ver[0]) + "." + str(ver[1]) + "." + str(ver[2])
			
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
	report['render_time'] = 0
	report['render_color_path'] = r"Color/" + name_scene + "." + image_format
	report['date_time'] = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
	report['difference_color'] = "not compared yet"
	report['test_case'] = test_case
	report['script_info'] = script_info
	report['test_status'] = "undefined"

	with open(log_name, 'w') as file:
		json.dump([report], file, indent=' ')

def write_status(directory, status):
	with open(directory, 'r') as w:
		json_report = w.read()
	json_report = json_report.replace("undefined", status)
	json_report = json.loads(json_report)
	with open(directory, 'w') as file:
		json.dump(json_report, file, indent=' ')

def launch_tests():

	files = os.listdir(r"{work_dir}")
	json_files = list(filter(lambda x: x.endswith('RPR.json'), files))
	if not os.path.exists(os.path.join(r"{work_dir}", "Color")):
		os.makedirs(os.path.join(r"{work_dir}", "Color"))

	status = 0

	for i in range(len(json_files), len(list_tests)):

		try:
			rc = prerender(list_tests[i])
			if rc:
				write_status(os.path.join(r"{work_dir}", list_tests[i][0] + "_RPR.json"), 'passed')
				status = 0
		except Exception:
			rc = -1

		if (rc == -1):
			create_report(list_tests[i][0], list_tests[i][1], "failed")
			write_status(os.path.join(r"{work_dir}", list_tests[i][0] + "_RPR.json"), 'failed')
			status -= 1
			if (status == -3):
				files = os.listdir(r"{work_dir}")
				json_files = list(filter(lambda x: x.endswith('RPR.json'), files))
				for i in range(len(json_files), len(list_tests)):
					create_report(list_tests[i][0], list_tests[i][1], "failed")
					write_status(os.path.join(r"{work_dir}", list_tests[i][0] + "_RPR.json"), 'failed')
				exit()
				
		with open(os.path.join(r"{work_dir}", 'log_status.txt'), 'a') as f:
			f.write("Current test: " + str(i) + " | fail count: " + \
				str(status) + " | last_status: " + str(rc) + " | total count: " + str(len(list_tests)) + "\n")
