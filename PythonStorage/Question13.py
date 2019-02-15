import arcpy
import os

arcpy.env.workspace = r"C:\Users\ctchurch\Desktop\Question13Storage"
arcpy.env.overwriteOutput = True

gdbPath = r"C:\Users\ctchurch\Desktop\Question13Storage"
gdbName = "QuestionGDB"
fcPath = r"C:\Users\ctchurch\Desktop\Question13Storage\Question 13"

arcpy.CreateFileGDB_management(gdbPath,gdbName)

gdbPathExt = r"C:\Users\ctchurch\Desktop\Question13Storage\QuestionGDB.gdb"
feature_classes = []

arcpy.env.workspace = r"C:\Users\ctchurch\Desktop\Question13Storage\Question 13"
featureList = arcpy.ListFeatureClasses()

for feature in featureList:
    arcpy.CopyFeatures_management(feature,os.path.join(gdbPathExt,os.path.splitext(feature)[0]))

arcpy.env.workspace = r"C:\Users\ctchurch\Desktop\Question13Storage\QuestionGDB.gdb"

countyFC = "tl_2018_us_county"
exportPath = r"C:\Users\ctchurch\Desktop\Question13Storage\QuestionGDB.gdb\Maricopa_County_Extract"
tempLyr = r"C:\Users\ctchurch\Desktop\Question13Storage\QuestionGDB.gdb\TempLayer_lyr"
tractFC = "tl_2018_04_tract"
clipFC = "Maricopa_County_Extract"

arcpy.MakeFeatureLayer_management(countyFC,tempLyr)
arcpy.SelectLayerByAttribute_management(tempLyr,"NEW_SELECTION","NAMELSAD = 'Maricopa County'")
arcpy.CopyFeatures_management(tempLyr,exportPath)
arcpy.Clip_analysis(tractFC,clipFC,"TractsClip_Maricopa")

