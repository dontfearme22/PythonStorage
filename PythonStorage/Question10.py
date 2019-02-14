import arcpy

arcpy.env.workspace = r"C:\Users\Alan\Desktop\Exercise 3.gdb"
arcpy.env.overwriteOutput = True

fc01 = "Tracts"
fc02 = "General_Offense"

arcpy.SpatialJoin_analysis(fc02,fc01,"JOIN_ONE_TO_MANY")
