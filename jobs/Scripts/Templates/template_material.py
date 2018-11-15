

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

    matlib = material_browser.RPRMaterialLibrary()
    matlib_path = matlib.get_library_path() + "/" + test_list[3] + "/" + test_list[3] + ".xml"
    material = bpy.data.materials['Material']
    material_browser.import_xml_material(matlib_path, material)

    render(test_list[0], test_list[1])
    return 1


if __name__ == "__main__":

    list_tests = [
    ["BL_MAT_LIB_001", ["Material: BarnFindOrange Solid"], "Test_Scene.blend", "BarnFindOrange_Solid"],
    ["BL_MAT_LIB_002", ["Material: BasketCaseBlue Solid"], "Test_Scene.blend", "BasketCaseBlue_Solid"],
    ["BL_MAT_LIB_003", ["Material: BeachBumAqua Metallic"], "Test_Scene.blend", "BeachBumAqua_Metallic"],
    ["BL_MAT_LIB_004", ["Material: BlueBayou Solid"], "Test_Scene.blend", "BlueBayou_Solid"],
    ["BL_MAT_LIB_005", ["Material: BoulevardBlack Solid"], "Test_Scene.blend", "BoulevardBlack_Solid"],
    ["BL_MAT_LIB_006", ["Material: BurnOutBlue Metallic"], "Test_Scene.blend", "BurnOutBlue_Metallic"],
    ["BL_MAT_LIB_007", ["Material: CandyPantsViolet Metallic"], "Test_Scene.blend", "CandyPantsViolet_Metallic"],
    ["BL_MAT_LIB_008", ["Material: Car Paint Metallic"], "Test_Scene.blend", "Car_Paint_Metallic"],
    ["BL_MAT_LIB_009", ["Material: Car Paint Pearlescent"], "Test_Scene.blend", "Car_Paint_Pearlescent"],
    ["BL_MAT_LIB_010", ["Material: Car Paint Solid"], "Test_Scene.blend", "Car_Paint_Solid"],
    ["BL_MAT_LIB_011", ["Material: Champagne Metallic"], "Test_Scene.blend", "Champagne_Metallic"],
    ["BL_MAT_LIB_012", ["Material: CherryGumball Solid"], "Test_Scene.blend", "CherryGumball_Solid"],
    ["BL_MAT_LIB_013", ["Material: ChopTopSilver Metallic"], "Test_Scene.blend", "ChopTopSilver_Metallic"],
    ["BL_MAT_LIB_014", ["Material: CruiseNightBlue Metallic"], "Test_Scene.blend", "CruiseNightBlue_Metallic"],
    ["BL_MAT_LIB_015", ["Material: DesertedTan Flat"], "Test_Scene.blend", "DesertedTan_Flat"],
    ["BL_MAT_LIB_016", ["Material: EastwoodBluePearl Pearlescent"], "Test_Scene.blend", "EastwoodBluePearl_Pearlescent"],
    ["BL_MAT_LIB_017", ["Material: EastwoodRoyalBlue Metallic"], "Test_Scene.blend", "EastwoodRoyalBlue_Metallic"],
    ["BL_MAT_LIB_018", ["Material: ElectricYellow Solid"], "Test_Scene.blend", "ElectricYellow_Solid"],
    ["BL_MAT_LIB_019", ["Material: EuroRacingGreen Metallic"], "Test_Scene.blend", "EuroRacingGreen_Metallic"],
    ["BL_MAT_LIB_020", ["Material: EyeCandyGreen Solid"], "Test_Scene.blend", "EyeCandyGreen_Solid"],
    ["BL_MAT_LIB_021", ["Material: GasserGreen Pearlescent"], "Test_Scene.blend", "GasserGreen_Pearlescent"],
    ["BL_MAT_LIB_022", ["Material: HugginOrange Solid"], "Test_Scene.blend", "HugginOrange_Solid"],
    ["BL_MAT_LIB_023", ["Material: LimeSqueezinGreen Solid"], "Test_Scene.blend", "LimeSqueezinGreen_Solid"],
    ["BL_MAT_LIB_024", ["Material: MalibuSunsetOrange Pearlescent"], "Test_Scene.blend", "MalibuSunsetOrange_Pearlescent"],
    ["BL_MAT_LIB_025", ["Material: OrangeUBad Solid"], "Test_Scene.blend", "OrangeUBad_Solid"],
    ["BL_MAT_LIB_026", ["Material: PinupRed Solid"], "Test_Scene.blend", "PinupRed_Solid"],
    ["BL_MAT_LIB_027", ["Material: PlumCrazy Metallic"], "Test_Scene.blend", "PlumCrazy_Metallic"],
    ["BL_MAT_LIB_028", ["Material: ProStreetRed Solid"], "Test_Scene.blend", "ProStreetRed_Solid"],
    ["BL_MAT_LIB_029", ["Material: PureWhite Solid"], "Test_Scene.blend", "PureWhite_Solid"],
    ["BL_MAT_LIB_030", ["Material: QuarterMileCandyRed Solid"], "Test_Scene.blend", "QuarterMileCandyRed_Solid"],
    ["BL_MAT_LIB_031", ["Material: RatRodBlack Solid"], "Test_Scene.blend", "RatRodBlack_Solid"],
    ["BL_MAT_LIB_032", ["Material: ReptileRed Solid"], "Test_Scene.blend", "ReptileRed_Solid"],
    ["BL_MAT_LIB_033", ["Material: RodzBerry Metallic"], "Test_Scene.blend", "RodzBerry_Metallic"],
    ["BL_MAT_LIB_034", ["Material: RottenLimeGreen Solid"], "Test_Scene.blend", "RottenLimeGreen_Solid"],
    ["BL_MAT_LIB_035", ["Material: SaltWaterTaffyTeal Metallic"], "Test_Scene.blend", "SaltWaterTaffyTeal_Metallic"],
    ["BL_MAT_LIB_036", ["Material: StraightAxleRedPearl Pearlescent"], "Test_Scene.blend", "StraightAxleRedPearl_Pearlescent"],
    ["BL_MAT_LIB_037", ["Material: SugarCoatItGold Metallic"], "Test_Scene.blend", "SugarCoatItGold_Metallic"],
    ["BL_MAT_LIB_038", ["Material: TequilaLimeNGold Solid"], "Test_Scene.blend", "TequilaLimeNGold_Solid"],
    ["BL_MAT_LIB_039", ["Material: TunnelRamGray Metallic"], "Test_Scene.blend", "TunnelRamGray_Metallic"],
    ["BL_MAT_LIB_040", ["Material: USABrightWhite Solid"], "Test_Scene.blend", "USABrightWhite_Solid"],
    ["BL_MAT_LIB_041", ["Material: USABrightWhiteFlat Solid"], "Test_Scene.blend", "USABrightWhiteFlat_Solid"],
    ["BL_MAT_LIB_042", ["Material: VinoRojo Solid"], "Test_Scene.blend", "VinoRojo_Solid"],
    ["BL_MAT_LIB_043", ["Material: Carbon Fiber"], "Test_Scene.blend", "Carbon_Fiber"],
    ["BL_MAT_LIB_044", ["Material: Carbon Fiber Glossy"], "Test_Scene.blend", "Carbon_Fiber_Glossy"],
    ["BL_MAT_LIB_045", ["Material: Carbon Fiber GlossyCoat"], "Test_Scene.blend", "Carbon_Fiber_GlossyCoat"],
    ["BL_MAT_LIB_046", ["Material: Carbon Fiber SemiGlossy"], "Test_Scene.blend", "Carbon_Fiber_SemiGlossy"],
    ["BL_MAT_LIB_047", ["Material: FiberGlass"], "Test_Scene.blend", "FiberGlass"],
    ["BL_MAT_LIB_048", ["Material: Concrete BrickCracks Grey"], "Test_Scene.blend", "Concrete_BrickCracks_Grey"],
    ["BL_MAT_LIB_049", ["Material: Concrete PaintedCracks"], "Test_Scene.blend", "Concrete_PaintedCracks"],
    ["BL_MAT_LIB_050", ["Material: Concrete PaintedRough"], "Test_Scene.blend", "Concrete_PaintedRough"],
    ["BL_MAT_LIB_051", ["Material: Concrete Stone"], "Test_Scene.blend", "Concrete_Stone"],
    ["BL_MAT_LIB_052", ["Material: Concrete Tiles"], "Test_Scene.blend", "Concrete_Tiles"],
    ["BL_MAT_LIB_053", ["Material: Concrete WornBare"], "Test_Scene.blend", "Concrete_WornBare"],
    ["BL_MAT_LIB_054", ["Material: Concrete WornBare SmoothBump"], "Test_Scene.blend", "Concrete_WornBare_SmoothBump"],
    ["BL_MAT_LIB_055", ["Material: Emissive Fluorescent Yellow"], "Test_Scene.blend", "Emissive_Fluorescent_Yellow"],
    ["BL_MAT_LIB_056", ["Material: Emissive Fluorescent Cyan"], "Test_Scene.blend", "Emissive_Fluorescent_Cyan"],
    ["BL_MAT_LIB_057", ["Material: Emissive Fluorescent Magenta"], "Test_Scene.blend", "Emissive_Fluorescent_Magenta"],
    ["BL_MAT_LIB_058", ["Material: Emissive Fluorescent White"], "Test_Scene.blend", "Emissive_Fluorescent_White"],
    ["BL_MAT_LIB_059", ["Material: Emissive CoolLight"], "Test_Scene.blend", "Emissive_CoolLight"],
    ["BL_MAT_LIB_060", ["Material: Aluminium Anodized"], "Test_Scene.blend", "Aluminium_Anodized"],
    ["BL_MAT_LIB_061", ["Material: Aluminium Directional"], "Test_Scene.blend", "Aluminium_Directional"],
    ["BL_MAT_LIB_062", ["Material: Aluminium Oxidiazed"], "Test_Scene.blend", "Aluminium_Oxidiazed"],
    ["BL_MAT_LIB_063", ["Material: Aluminium Polished"], "Test_Scene.blend", "Aluminium_Polished"],
    ["BL_MAT_LIB_064", ["Material: Aluminium SandBlasted"], "Test_Scene.blend", "Aluminium_SandBlasted"],
    ["BL_MAT_LIB_065", ["Material: Brass Cartridge"], "Test_Scene.blend", "Brass_Cartridge"],
    ["BL_MAT_LIB_066", ["Material: Brass Matte"], "Test_Scene.blend", "Brass Matte"],
    ["BL_MAT_LIB_067", ["Material: Brass Oxidized"], "Test_Scene.blend", "Brass_Oxidized"],
    ["BL_MAT_LIB_068", ["Material: Brass Patinated"], "Test_Scene.blend", "Brass_Patinated"],
    ["BL_MAT_LIB_069", ["Material: Brass Standard"], "Test_Scene.blend", "Brass_Standard"],
    ["BL_MAT_LIB_070", ["Material: Bronze Corrision"], "Test_Scene.blend", "Bronze_Corrision"],
    ["BL_MAT_LIB_071", ["Material: Bronze Matte"], "Test_Scene.blend", "Bronze_Matte"],
    ["BL_MAT_LIB_072", ["Material: Bronze Oxidized"], "Test_Scene.blend", "Bronze_Oxidized"],
    ["BL_MAT_LIB_073", ["Material: Bronze Polished2"], "Test_Scene.blend", "Bronze_Polished2"],
    ["BL_MAT_LIB_074", ["Material: Bronze Rough"], "Test_Scene.blend", "Bronze_Rough"],
    ["BL_MAT_LIB_075", ["Material: Chrome Dusty"], "Test_Scene.blend", "Chrome_Dusty"],
    ["BL_MAT_LIB_076", ["Material: Chrome Matte"], "Test_Scene.blend", "Chrome_Matte"],
    ["BL_MAT_LIB_077", ["Material: Chrome Sandblasted"], "Test_Scene.blend", "Chrome_Sandblasted"],
    ["BL_MAT_LIB_078", ["Material: Chrome Scratched"], "Test_Scene.blend", "Chrome_Scratched"],
    ["BL_MAT_LIB_079", ["Material: Copper Brushed2"], "Test_Scene.blend", "Copper_Brushed2"],
    ["BL_MAT_LIB_080", ["Material: Copper Dented"], "Test_Scene.blend", "Copper_Dented"],
    ["BL_MAT_LIB_081", ["Material: Copper Old"], "Test_Scene.blend", "Copper_Old"],
    ["BL_MAT_LIB_082", ["Material: Copper Wrought"], "Test_Scene.blend", "Copper_Wrought"],
    ["BL_MAT_LIB_083", ["Material: Generic"], "Test_Scene.blend", "Generic"],
    ["BL_MAT_LIB_084", ["Material: Gold"], "Test_Scene.blend", "Gold"],
    ["BL_MAT_LIB_085", ["Material: Gold Foil Rough"], "Test_Scene.blend", "Gold_Foil_Rough"],
    ["BL_MAT_LIB_086", ["Material: Gold Paint"], "Test_Scene.blend", "Gold_Paint"],
    ["BL_MAT_LIB_087", ["Material: Gold Paint Cracked"], "Test_Scene.blend", "Gold_Paint_Cracked"],
    ["BL_MAT_LIB_088", ["Material: Gold Rough"], "Test_Scene.blend", "Gold_Rough"],
    ["BL_MAT_LIB_089", ["Material: Iron Hammered"], "Test_Scene.blend", "Iron_Hammered"],
    ["BL_MAT_LIB_090", ["Material: Iron Oxidized"], "Test_Scene.blend", "Iron_Oxidized"],
    ["BL_MAT_LIB_091", ["Material: Iron Rugged"], "Test_Scene.blend", "Iron_Rugged"],
    ["BL_MAT_LIB_092", ["Material: Iron Smooth"], "Test_Scene.blend", "Iron_Smooth"],
    ["BL_MAT_LIB_093", ["Material: Iron Worn"], "Test_Scene.blend", "Iron_Worn"],
    # ["BL_MAT_LIB_094", ["Material: Lead Matte"], "Test_Scene.blend", "Lead_Matte"],
    ["BL_MAT_LIB_095", ["Material: Lead Rough"], "Test_Scene.blend", "Lead_Rough"],
    ["BL_MAT_LIB_096", ["Material: Lead Rusted"], "Test_Scene.blend", "Lead_Rusted"],
    ["BL_MAT_LIB_097", ["Material: Lead Sandblasted"], "Test_Scene.blend", "Lead_Sandblasted"],
    ["BL_MAT_LIB_098", ["Material: Lead Smooth"], "Test_Scene.blend", "Lead_Smooth"],
    ["BL_MAT_LIB_099", ["Material: Steel Blue"], "Test_Scene.blend", "Steel_Blue"],
    ["BL_MAT_LIB_100", ["Material: Steel Galvanized"], "Test_Scene.blend", "Steel_Galvanized"],
    ["BL_MAT_LIB_101", ["Material: Steel Oxidized"], "Test_Scene.blend", "Steel_Oxidized"],
    ["BL_MAT_LIB_102", ["Material: Steel Smooth"], "Test_Scene.blend", "Steel_Smooth"],
    ["BL_MAT_LIB_103", ["Material: Steel Worn"], "Test_Scene.blend", "Steel_Worn"],
    ["BL_MAT_LIB_104", ["Material: Fabric Matte Solid Beige"], "Test_Scene.blend", "Fabric_Matte_Solid_Beige"],
    ["BL_MAT_LIB_105", ["Material: Fabric Matte Solid Red"], "Test_Scene.blend", "Fabric_Matte_Solid_Red"],
    ["BL_MAT_LIB_106", ["Material: Fabric Matte Transparent Beige"], "Test_Scene.blend", "Fabric_Matte_Transparent_Beige"],
    ["BL_MAT_LIB_107", ["Material: Fabric Matte Transparent Red"], "Test_Scene.blend", "Fabric_Matte_Transparent_Red"],
    ["BL_MAT_LIB_108", ["Material: Fabric Silk"], "Test_Scene.blend", "Fabric_Silk"],
    ["BL_MAT_LIB_109", ["Material: Fur Carpet Displacement"], "Test_Scene.blend", "Fur_Carpet_Displacement"],
    ["BL_MAT_LIB_110", ["Material: Glass Antique"], "Test_Scene.blend", "Glass_Antique"],
    ["BL_MAT_LIB_111", ["Material: Glass CarBreakLight"], "Test_Scene.blend", "Glass_CarBreakLight"],
    ["BL_MAT_LIB_112", ["Material: Glass CarHeadLight"], "Test_Scene.blend", "Glass_CarHeadLight"],
    ["BL_MAT_LIB_113", ["Material: Glass CarIndicatorLight"], "Test_Scene.blend", "Glass_CarIndicatorLight"],
    ["BL_MAT_LIB_114", ["Material: Glass Clear Window"], "Test_Scene.blend", "Glass_Clear_Window"],
    ["BL_MAT_LIB_115", ["Material: Glass Solid Blue"], "Test_Scene.blend", "Glass_Solid_Blue"],
    ["BL_MAT_LIB_116", ["Material: Glass Solid Brown"], "Test_Scene.blend", "Glass_Solid_Brown"],
    ["BL_MAT_LIB_117", ["Material: Glass Solid Clear"], "Test_Scene.blend", "Glass_Solid_Clear"],
    ["BL_MAT_LIB_118", ["Material: Glass Solid Clear Scratched"], "Test_Scene.blend", "Glass_Solid_Clear_Scratched"],
    ["BL_MAT_LIB_119", ["Material: Glass Solid Frosted"], "Test_Scene.blend", "Glass_Solid_Frosted"],
    ["BL_MAT_LIB_120", ["Material: Glass Solid Green"], "Test_Scene.blend", "Glass_Solid_Green"],
    ["BL_MAT_LIB_121", ["Material: Glass Solid GreenBlue"], "Test_Scene.blend", "Glass_Solid_GreenBlue"],
    ["BL_MAT_LIB_122", ["Material: Glass Solid GreenBlue Scratched"], "Test_Scene.blend", "Glass_Solid_GreenBlue_Scratched"],
    ["BL_MAT_LIB_123", ["Material: Glass Solid Red"], "Test_Scene.blend", "Glass_Solid_Red"],
    ["BL_MAT_LIB_124", ["Material: Glass Solid Tinted"], "Test_Scene.blend", "Glass_Solid_Tinted"],
    ["BL_MAT_LIB_125", ["Material: Glass Solid Yellow"], "Test_Scene.blend", "Glass_Solid_Yellow"],
    ["BL_MAT_LIB_126", ["Material: Glass Thin Bronze"], "Test_Scene.blend", "Glass_Thin_Bronze"],
    ["BL_MAT_LIB_127", ["Material: Glass Thin Green"], "Test_Scene.blend", "Glass_Thin_Green"],
    ["BL_MAT_LIB_128", ["Material: Glass Tinted Dark"], "Test_Scene.blend", "Glass_Tinted_Dark"],
    ["BL_MAT_LIB_129", ["Material: Glass Used"], "Test_Scene.blend", "Glass_Used"],
    ["BL_MAT_LIB_130", ["Material: Mirror"], "Test_Scene.blend", "Mirror"],
    ["BL_MAT_LIB_131", ["Material: Ground Dark Displacement"], "Test_Scene.blend", "Ground_Dark_Displacement"],
    ["BL_MAT_LIB_132", ["Material: Ground Dark"], "Test_Scene.blend", "Ground_Dark"],
    ["BL_MAT_LIB_133", ["Material: Ground Grass"], "Test_Scene.blend", "Ground_Grass"],
    ["BL_MAT_LIB_134", ["Material: Ground Grass Displacement"], "Test_Scene.blend", "Ground_Grass_Displacement"],
    ["BL_MAT_LIB_135", ["Material: Ground Grass Cut Displacement"], "Test_Scene.blend", "Ground_Grass_Cut_Displacement"],
    ["BL_MAT_LIB_136", ["Material: Jewels Diamond"], "Test_Scene.blend", "Jewels_Diamond"],
    ["BL_MAT_LIB_137", ["Material: Jewels Emerald"], "Test_Scene.blend", "Jewels_Emerald"],
    ["BL_MAT_LIB_138", ["Material: Jewels Ruby"], "Test_Scene.blend", "Jewels_Ruby"],
    ["BL_MAT_LIB_139", ["Material: Leather Beige"], "Test_Scene.blend", "Leather_Beige"],
    ["BL_MAT_LIB_140", ["Material: Leather Black"], "Test_Scene.blend", "Leather_Black"],
    ["BL_MAT_LIB_141", ["Material: Leather Brown"], "Test_Scene.blend", "Leather_Brown"],
    ["BL_MAT_LIB_142", ["Material: Liquids Alcohol Champagne"], "Test_Scene.blend", "Liquids_Alcohol_Champagne"],
    ["BL_MAT_LIB_143", ["Material: Water Transparent"], "Test_Scene.blend", "Water_Transparent"],
    ["BL_MAT_LIB_144", ["Material: Water Transparent Bump"], "Test_Scene.blend", "Water_Transparent_Bump"],
    ["BL_MAT_LIB_145", ["Material: Water Transparent Displacement"], "Test_Scene.blend", "Water_Transparent_Displacement"],
    ["BL_MAT_LIB_146", ["Material: Car Paint Black"], "Test_Scene.blend", "Car_Paint_Black"],
    ["BL_MAT_LIB_147", ["Material: Car Paint Bue"], "Test_Scene.blend", "Car_Paint_Bue"],
    ["BL_MAT_LIB_148", ["Material: Car Paint Dark Grey"], "Test_Scene.blend", "Car_Paint_Dark_Grey"],
    ["BL_MAT_LIB_149", ["Material: Car Paint Ice Silver"], "Test_Scene.blend", "Car_Paint_Ice_Silver"],
    ["BL_MAT_LIB_150", ["Material: Car Paint Indy Yellow"], "Test_Scene.blend", "Car_Paint_Indy_Yellow"],
    ["BL_MAT_LIB_151", ["Material: Car Paint Inferno"], "Test_Scene.blend", "Car_Paint_Inferno"],
    ["BL_MAT_LIB_152", ["Material: Car Paint Jasmine Green"], "Test_Scene.blend", "Car_Paint_Jasmine_Green"],
    ["BL_MAT_LIB_153", ["Material: Car Paint Lapis Blue"], "Test_Scene.blend", "Car_Paint_Lapis_Blue"],
    ["BL_MAT_LIB_154", ["Material: Car Paint Lava Red"], "Test_Scene.blend", "Car_Paint_Lava_Red"],
    ["BL_MAT_LIB_155", ["Material: Car Paint North Grey"], "Test_Scene.blend", "Car_Paint_North_Grey"],
    ["BL_MAT_LIB_156", ["Material: Car Paint Tungsten"], "Test_Scene.blend", "Car_Paint_Tungsten"],
    ["BL_MAT_LIB_157", ["Material: Car Paint Venetian Red"], "Test_Scene.blend", "Car_Paint_Venetian_Red"],
    ["BL_MAT_LIB_158", ["Material: Car Paint Vibrant Violet"], "Test_Scene.blend", "Car_Paint_Vibrant_Violet"],
    ["BL_MAT_LIB_159", ["Material: Car Paint Wilderness Green"], "Test_Scene.blend", "Car_Paint_Wilderness_Green"],
    ["BL_MAT_LIB_160", ["Material: Metallic Paint Matte Red"], "Test_Scene.blend", "Metallic_Paint_Matte_Red"],
    ["BL_MAT_LIB_161", ["Material: Metallic Paint Red"], "Test_Scene.blend", "Metallic_Paint_Red"],
    ["BL_MAT_LIB_162", ["Material: Metallic Paint Silver"], "Test_Scene.blend", "Metallic_Paint_Silver"],
    ["BL_MAT_LIB_163", ["Material: Scratched Metallic Paint Red"], "Test_Scene.blend", "Scratched_Metallic_Paint_Red"],
    ["BL_MAT_LIB_164", ["Material: Scratched Metallic Paint Yellow"], "Test_Scene.blend", "Scratched_Metallic_Paint_Yellow"],
    ["BL_MAT_LIB_165", ["Material: Aluminium Brushed"], "Test_Scene.blend", "Aluminium_Brushed"],
    ["BL_MAT_LIB_166", ["Material: Aluminium Cast"], "Test_Scene.blend", "Aluminium_Cast"],
    ["BL_MAT_LIB_167", ["Material: Aluminium Corrugated"], "Test_Scene.blend", "Aluminium_Corrugated"],
    ["BL_MAT_LIB_168", ["Material: Aluminium Matte"], "Test_Scene.blend", "Aluminium_Matte"],
    ["BL_MAT_LIB_169", ["Material: Brass Brushed"], "Test_Scene.blend", "Brass_Brushed"],
    ["BL_MAT_LIB_170", ["Material: Brass Polished"], "Test_Scene.blend", "Brass_Polished"],
    ["BL_MAT_LIB_171", ["Material: Brass Satin"], "Test_Scene.blend", "Brass_Satin"],
    ["BL_MAT_LIB_172", ["Material: Cast Iron"], "Test_Scene.blend", "Cast_Iron"],
    ["BL_MAT_LIB_173", ["Material: Chrome"], "Test_Scene.blend", "Chrome"],
    ["BL_MAT_LIB_174", ["Material: Copper Brushed"], "Test_Scene.blend", "Copper_Brushed"],
    ["BL_MAT_LIB_175", ["Material: Copper Polished"], "Test_Scene.blend", "Copper_Polished"],
    ["BL_MAT_LIB_176", ["Material: Copper Satin"], "Test_Scene.blend", "Copper_Satin"],
    ["BL_MAT_LIB_177", ["Material: Galvanized Steel"], "Test_Scene.blend", "Galvanized-Steel"],
    ["BL_MAT_LIB_178", ["Material: Gun Metal"], "Test_Scene.blend", "Gun_Metal"],
    ["BL_MAT_LIB_179", ["Material: Mercury"], "Test_Scene.blend", "Mercury"],
    ["BL_MAT_LIB_180", ["Material: Metal Plate"], "Test_Scene.blend", "Metal_Plate"],
    ["BL_MAT_LIB_181", ["Material: Rust Metal"], "Test_Scene.blend", "Rust_Metal"],
    ["BL_MAT_LIB_182", ["Material: Stainless Steel"], "Test_Scene.blend", "Stainless_Steel"],
    ["BL_MAT_LIB_183", ["Material: Stainless Steel Brushed"], "Test_Scene.blend", "Stainless_Steel_Brushed"],
    ["BL_MAT_LIB_184", ["Material: Paint EggShell LaserLemon"], "Test_Scene.blend", "Paint_EggShell_LaserLemon"],
    ["BL_MAT_LIB_185", ["Material: Paint EggShell SleekWhite"], "Test_Scene.blend", "Paint_EggShell_SleekWhite"],
    ["BL_MAT_LIB_186", ["Material: Paint EggShell SunValley"], "Test_Scene.blend", "Paint_EggShell_SunValley"],
    ["BL_MAT_LIB_187", ["Material: Paint EggShell Tanzanite"], "Test_Scene.blend", "Paint_EggShell_Tanzanite"],
    ["BL_MAT_LIB_188", ["Material: Paint EggShell TartOrange"], "Test_Scene.blend", "Paint_EggShell_TartOrange"],
    ["BL_MAT_LIB_189", ["Material: Paint EggShell TropicalSea"], "Test_Scene.blend", "Paint_EggShell_TropicalSea"],
    ["BL_MAT_LIB_190", ["Material: Paint Flat LaserLemon"], "Test_Scene.blend", "Paint_Flat_LaserLemon"],
    ["BL_MAT_LIB_191", ["Material: Paint Flat SleekWhite"], "Test_Scene.blend", "Paint_Flat_SleekWhite"],
    ["BL_MAT_LIB_192", ["Material: Paint Flat SunValley"], "Test_Scene.blend", "Paint_Flat_SunValley"],
    ["BL_MAT_LIB_193", ["Material: Paint Flat Tanzanite"], "Test_Scene.blend", "Paint_Flat_Tanzanite"],
    ["BL_MAT_LIB_194", ["Material: Paint Flat TartOrange"], "Test_Scene.blend", "Paint_Flat_TartOrange"],
    ["BL_MAT_LIB_195", ["Material: Paint Flat TawnyDayLily"], "Test_Scene.blend", "Paint_Flat_TawnyDayLily"],
    ["BL_MAT_LIB_196", ["Material: Paint Flat TropicalSea"], "Test_Scene.blend", "Paint_Flat_TropicalSea"],
    ["BL_MAT_LIB_197", ["Material: Paint Flat VoilePink"], "Test_Scene.blend", "Paint_Flat_VoilePink"],
    ["BL_MAT_LIB_198", ["Material: Paint Glossy LaserLemon"], "Test_Scene.blend", "Paint_Glossy_LaserLemon"],
    ["BL_MAT_LIB_199", ["Material: Paint Glossy SleekWhite"], "Test_Scene.blend", "Paint_Glossy_SleekWhite"],
    ["BL_MAT_LIB_200", ["Material: Paint Glossy SunValley"], "Test_Scene.blend", "Paint_Glossy_SunValley"],
    ["BL_MAT_LIB_201", ["Material: Paint Glossy Tanzanite"], "Test_Scene.blend", "Paint_Glossy_Tanzanite"],
    ["BL_MAT_LIB_202", ["Material: Paint Glossy TartOrange"], "Test_Scene.blend", "Paint_Glossy_TartOrange"],
    ["BL_MAT_LIB_203", ["Material: Paint Glossy TropicalSea"], "Test_Scene.blend", "Paint_Glossy_TropicalSea"],
    ["BL_MAT_LIB_204", ["Material: Plastic Glossy Black"], "Test_Scene.blend", "Plastic_Glossy_Black"],
    ["BL_MAT_LIB_205", ["Material: Plastic Glossy Red"], "Test_Scene.blend", "Plastic_Glossy_Red"],
    ["BL_MAT_LIB_206", ["Material: Plastic Matte Black"], "Test_Scene.blend", "Plastic_Matte_Black"],
    ["BL_MAT_LIB_207", ["Material: Plastic Matte Red"], "Test_Scene.blend", "Plastic_Matte_Red"],
    ["BL_MAT_LIB_208", ["Material: Plastic Matte White"], "Test_Scene.blend", "Plastic_Matte_White"],
    ["BL_MAT_LIB_209", ["Material: Styrofoam"], "Test_Scene.blend", "Styrofoam"],
    ["BL_MAT_LIB_210", ["Material: Porcelain Black"], "Test_Scene.blend", "Porcelain_Black"],
    ["BL_MAT_LIB_211", ["Material: Porcelain Blue"], "Test_Scene.blend", "Porcelain_Blue"],
    ["BL_MAT_LIB_212", ["Material: Porcelain Cracked White"], "Test_Scene.blend", "Porcelain_Cracked_White"],
    ["BL_MAT_LIB_213", ["Material: Porcelain Matte White"], "Test_Scene.blend", "Porcelain_Matte_White"],
    ["BL_MAT_LIB_214", ["Material: Porcelain New White"], "Test_Scene.blend", "Porcelain_New_White"],
    ["BL_MAT_LIB_215", ["Material: Porcelain Old White"], "Test_Scene.blend", "Porcelain_Old_White"],
    ["BL_MAT_LIB_216", ["Material: Porcelain White"], "Test_Scene.blend", "Porcelain_White"],
    ["BL_MAT_LIB_217", ["Material: Bronze Brushed"], "Test_Scene.blend", "Bronze_Brushed"],
    ["BL_MAT_LIB_218", ["Material: Bronze Polished"], "Test_Scene.blend", "Bronze_Polished"],
    ["BL_MAT_LIB_219", ["Material: Bronze Satin"], "Test_Scene.blend", "Bronze_Satin"],
    ["BL_MAT_LIB_220", ["Material: Gold Brushed"], "Test_Scene.blend", "Gold_Brushed"],
    ["BL_MAT_LIB_221", ["Material: Gold Polished"], "Test_Scene.blend", "Gold_Polished"],
    ["BL_MAT_LIB_222", ["Material: Gold Satin"], "Test_Scene.blend", "Gold_Satin"],
    ["BL_MAT_LIB_223", ["Material: Silver Brushed"], "Test_Scene.blend", "Silver_Brushed"],
    ["BL_MAT_LIB_224", ["Material: Silver Polished"], "Test_Scene.blend", "Silver_Polished"],
    ["BL_MAT_LIB_225", ["Material: Silver Satin"], "Test_Scene.blend", "Silver_Satin"],
    ["BL_MAT_LIB_226", ["Material: Stone Marble Blue Matte"], "Test_Scene.blend", "Stone_Marble_Blue_Matte"],
    ["BL_MAT_LIB_227", ["Material: Stone Marble Pink Matte"], "Test_Scene.blend", "Stone_Marble_Pink_Matte"],
    ["BL_MAT_LIB_228", ["Material: Stone Cladding"], "Test_Scene.blend", "Stone_Cladding"],
    ["BL_MAT_LIB_229", ["Material: Stone Granit BWB"], "Test_Scene.blend", "Stone_Granit_BWB"],
    ["BL_MAT_LIB_230", ["Material: Stone Marble Blue"], "Test_Scene.blend", "Stone_Marble_Blue"],
    ["BL_MAT_LIB_231", ["Material: Stone Marble Pink"], "Test_Scene.blend", "Stone_Marble_Pink"],
    ["BL_MAT_LIB_232", ["Material: Stone Marble Grey"], "Test_Scene.blend", "Stone_Marble_Grey"],
    ["BL_MAT_LIB_233", ["Material: Stone Rough Marble"], "Test_Scene.blend", "Stone_Rough_Marble"],
    ["BL_MAT_LIB_234", ["Material: Brick Color Displacement"], "Test_Scene.blend", "Brick_Color_Displacement"],
    ["BL_MAT_LIB_235", ["Material: Brick Natural V1"], "Test_Scene.blend", "Brick_Natural_V1"],
    ["BL_MAT_LIB_236", ["Material: Brick Old V3"], "Test_Scene.blend", "Brick_Old_V3"],
    ["BL_MAT_LIB_237", ["Material: Brick Old V2"], "Test_Scene.blend", "Brick_Old_V2"],
    ["BL_MAT_LIB_238", ["Material: Brick Basic V2"], "Test_Scene.blend", "Brick_Basic_V2"],
    ["BL_MAT_LIB_239", ["Material: Brick Irregular"], "Test_Scene.blend", "Brick_Irregular"],
    ["BL_MAT_LIB_240", ["Material: Brick Damage"], "Test_Scene.blend", "Brick_Damage"],
    ["BL_MAT_LIB_241", ["Material: Stone Marble Yellow Matte"], "Test_Scene.blend", "Stone_Marble_Yellow_Matte"],
    ["BL_MAT_LIB_242", ["Material: Floor Ceramic Tiles Checker"], "Test_Scene.blend", "Floor_Ceramic_Tiles_Checker"],
    ["BL_MAT_LIB_243", ["Material: Floor Ceramic Tiles Color"], "Test_Scene.blend", "Floor_Ceramic_Tiles_Color"],
    ["BL_MAT_LIB_244", ["Material: Floor Ceramic Tiles Color Variation 8x8"], "Test_Scene.blend", "Floor_Ceramic_Tiles_Color_Variation_8x8"],
    ["BL_MAT_LIB_245", ["Material: Floor Tiles Rustic Color 4x4"], "Test_Scene.blend", "Floor_Tiles_Rustic_Color_4x4"],
    ["BL_MAT_LIB_246", ["Material: Tiling BeigeMarble"], "Test_Scene.blend", "Tiling_BeigeMarble"],
    ["BL_MAT_LIB_247", ["Material: Tiling Blue Checkered"], "Test_Scene.blend", "Tiling_Blue_Checkered"],
    ["BL_MAT_LIB_248", ["Material: Tiling BLueMarble"], "Test_Scene.blend", "Tiling_BLueMarble"],
    ["BL_MAT_LIB_249", ["Material: tiling Checkered"], "Test_Scene.blend", "tiling_Checkered"],
    ["BL_MAT_LIB_250", ["Material: Tiling Old"], "Test_Scene.blend", "Tiling_Old"],
    ["BL_MAT_LIB_251", ["Material: Tiling White"], "Test_Scene.blend", "Tiling_White"],
    ["BL_MAT_LIB_252", ["Material: Tiling White Marble"], "Test_Scene.blend", "Tiling_White_Marble"],
    ["BL_MAT_LIB_253", ["Material: Roofing ClayShingles Beige"], "Test_Scene.blend", "Roofing_ClayShingles_Beige"],
    ["BL_MAT_LIB_254", ["Material: Roofing CorrugatedIron"], "Test_Scene.blend", "Roofing_CorrugatedIron"],
    ["BL_MAT_LIB_255", ["Material: Roofing RedClay Tiles"], "Test_Scene.blend", "Roofing_RedClayTiles"],
    ["BL_MAT_LIB_256", ["Material: Rubber Bumpy"], "Test_Scene.blend", "Rubber_Bumpy"],
    ["BL_MAT_LIB_257", ["Material: Rubber Diamonds"], "Test_Scene.blend", "Rubber_Diamonds"],
    ["BL_MAT_LIB_258", ["Material: Rubber Ribbed"], "Test_Scene.blend", "Rubber_Ribbed"],
    ["BL_MAT_LIB_259", ["Material: Rubber Smooth Clear"], "Test_Scene.blend", "Rubber_Smooth_Clear"],
    ["BL_MAT_LIB_260", ["Material: Rubber SmoothMatte"], "Test_Scene.blend", "Rubber_SmoothMatte"],
    ["BL_MAT_LIB_261", ["Material: Rubber SmoothMatte Black"], "Test_Scene.blend", "Rubber_SmoothMatte_Black"],
    ["BL_MAT_LIB_262", ["Material: Rubber SmoothMatte Blue"], "Test_Scene.blend", "Rubber_SmoothMatte_Blue"],
    ["BL_MAT_LIB_263", ["Material: Rubber SmoothMatte Green"], "Test_Scene.blend", "Rubber_SmoothMatte_Green"],
    ["BL_MAT_LIB_264", ["Material: Rubber SmoothMatte Red"], "Test_Scene.blend", "Rubber_SmoothMatte_Red"],
    ["BL_MAT_LIB_265", ["Material: Rubber SmoothShiny"], "Test_Scene.blend", "Rubber_SmoothShiny"],
    ["BL_MAT_LIB_266", ["Material: Rubber SmoothShiny Black"], "Test_Scene.blend", "Rubber_SmoothShiny_Black"],
    ["BL_MAT_LIB_267", ["Material: Rubber SmoothShiny Blue"], "Test_Scene.blend", "Rubber_SmoothShiny_Blue"],
    ["BL_MAT_LIB_268", ["Material: Rubber SmoothShiny Green"], "Test_Scene.blend", "Rubber_SmoothShiny_Green"],
    ["BL_MAT_LIB_269", ["Material: Rubber SmoothShiny Red"], "Test_Scene.blend", "Rubber_SmoothShiny_Red"],
    ["BL_MAT_LIB_270", ["Material: Rubber Used"], "Test_Scene.blend", "Rubber_Used"],
    # ["BL_MAT_LIB_271", ["Material: Diffuse Shadow Catcher"], "Test_Scene.blend", "Diffuse_Shadow_Catcher"],
    # ["BL_MAT_LIB_272", ["Material: Reflective Shadow Catcher"], "Test_Scene.blend", "Reflective_Shadow_Catcher"],
    ["BL_MAT_LIB_273", ["Material: Acrylic Refractive Glossy Green"], "Test_Scene.blend", "Acrylic_Refractive_Glossy_Green"],
    ["BL_MAT_LIB_274", ["Material: Acrylic Refractive Glossy Neon Green"], "Test_Scene.blend", "Acrylic_Refractive_Glossy_Neon_Green"],
    ["BL_MAT_LIB_275", ["Material: Acrylic Refractive Glossy Neon Orange"], "Test_Scene.blend", "Acrylic_Refractive_Glossy_Neon_Orange"],
    ["BL_MAT_LIB_276", ["Material: Acrylic Refractive Glossy Red"], "Test_Scene.blend", "Acrylic_Refractive_Glossy_Red"],
    ["BL_MAT_LIB_277", ["Material: Acrylic Refractive Matte Green"], "Test_Scene.blend", "Acrylic_Refractive_Matte_Green"],
    ["BL_MAT_LIB_278", ["Material: Acrylic Refractive Matte Red"], "Test_Scene.blend", "Acrylic_Refractive_Matte_Red"],
    ["BL_MAT_LIB_279", ["Material: Acrylic Transparent Matte Red"], "Test_Scene.blend", "Acrylic_Transparent_Matte_Red"],
    ["BL_MAT_LIB_280", ["Material: Acrylic Transparent Glossy Red"], "Test_Scene.blend", "Acrylic_Transparent_Glossy_Red"],
    ["BL_MAT_LIB_281", ["Material: Plastic Transparent Solid ClearBlue"], "Test_Scene.blend", "Plastic_Transparent_Solid_ClearBlue"],
    ["BL_MAT_LIB_282", ["Material: Plastic Transparent Thin ClearBlue"], "Test_Scene.blend", "Plastic_Transparent_Thin_ClearBlue"],
    ["BL_MAT_LIB_283", ["Material: Colored Glass"], "Test_Scene.blend", "Colored_Glass"],
    ["BL_MAT_LIB_284", ["Material: Jade"], "Test_Scene.blend", "Jade"],
    ["BL_MAT_LIB_285", ["Material: Milk"], "Test_Scene.blend", "Milk"],
    ["BL_MAT_LIB_286", ["Material: Wax"], "Test_Scene.blend", "Wax"],
    ["BL_MAT_LIB_287", ["Material: Wood Bark"], "Test_Scene.blend", "Wood_Bark"],
    ["BL_MAT_LIB_288", ["Material: Wood Beech Glossy"], "Test_Scene.blend", "Wood_Beech_Glossy"],
    ["BL_MAT_LIB_289", ["Material: Wood Beech Unfinished"], "Test_Scene.blend", "Wood_Beech_Unfinished"],
    ["BL_MAT_LIB_290", ["Material: Wood Cedar Glossy"], "Test_Scene.blend", "Wood_Cedar_Glossy"],
    ["BL_MAT_LIB_291", ["Material: Wood Cedar Unfinished"], "Test_Scene.blend", "Wood_Cedar_Unfinished"],
    ["BL_MAT_LIB_292", ["Material: Wood Clear Rustic"], "Test_Scene.blend", "Wood_Clear_Rustic"],
    ["BL_MAT_LIB_293", ["Material: Wood Mahogany Glossy"], "Test_Scene.blend", "Wood_Mahogany_Glossy"],
    ["BL_MAT_LIB_294", ["Material: Wood Mahogany Unfinished"], "Test_Scene.blend", "Wood_Mahogany_Unfinished"],
    ["BL_MAT_LIB_295", ["Material: Wood Maple Glossy"], "Test_Scene.blend", "Wood_Maple_Glossy"],
    ["BL_MAT_LIB_296", ["Material: Wood Maple Unfinished"], "Test_Scene.blend", "Wood_Maple_Unfinished"],
    ["BL_MAT_LIB_297", ["Material: Wood Natural Maple"], "Test_Scene.blend", "Wood_Natural_Maple"],
    ["BL_MAT_LIB_298", ["Material: Wood Oak Glossy"], "Test_Scene.blend", "Wood_Oak_Glossy"],
    ["BL_MAT_LIB_299", ["Material: Wood Oak Unfinished"], "Test_Scene.blend", "Wood_Oak_Unfinished"],
    ["BL_MAT_LIB_300", ["Material: Wood Planks Oak Glossy"], "Test_Scene.blend", "Wood_Planks_Oak_Glossy"],
    ["BL_MAT_LIB_301", ["Material: Wood Planks Oak Unfinished"], "Test_Scene.blend", "Wood_Planks_Oak_Unfinished"],
    ["BL_MAT_LIB_302", ["Material: Wood Rustic"], "Test_Scene.blend", "Wood_Rustic"],
    ["BL_MAT_LIB_303", ["Material: Wood Rustic Cherry"], "Test_Scene.blend", "Wood_Rustic_Cherry"],
    ["BL_MAT_LIB_304", ["Material: Wood Wenge Glossy"], "Test_Scene.blend", "Wood_Wenge_Glossy"],
    ["BL_MAT_LIB_305", ["Material: Wood Wenge Unfinished"], "Test_Scene.blend", "Wood_Wenge_Unfinished"]
    ]

    launch_tests()
