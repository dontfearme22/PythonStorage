import arcpy

arcpy.env.workspace = r"C:\Users\ctchurch\Documents\Exercise 3Temp.gdb"
arcpy.env.overwriteOutput = True

featureClass01 = r"C:\Users\ctchurch\Documents\Exercise 3Temp.gdb\General_Offense" 
fcfield01 = "OffenseCustom"
featureClass02 = r"C:\Users\ctchurch\Documents\Exercise 3Temp.gdb\CallsforService"

arcpy.MakeFeatureLayer_management(featureClass01,"General_OffenseLayer_lyr")
arcpy.SelectLayerByAttribute_management("General_OffenseLayer_lyr","NEW_SELECTION","x_rand > 10")
arcpy.CopyFeatures_management("General_OffenseLayer_lyr",r"C:\Users\ctchurch\Documents\Exercise 3Temp.gdb\New_Selection") 
