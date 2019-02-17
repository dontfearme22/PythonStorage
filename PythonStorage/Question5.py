import arcpy

arcpy.env.overwriteOutput = True

folderPath = r"C:\Users\ctchurch\Desktop\Question5Temp"
fileName = "TempGDB"
featureList = ["CapitalCities", "Landmarks", "HistoricPlaces", "StateNames", "Nationalities", "Rivers"]

arcpy.CreateFileGDB_management(folderPath,fileName)

arcpy.env.workspace = r"C:\Users\ctchurch\Desktop\Question5Temp\TempGDB.gdb"
newGDBPath = r"C:\Users\ctchurch\Desktop\Question5Temp\TempGDB.gdb"

for x in featureList:
    arcpy.CreateFeatureclass_management(newGDBPath,x)

