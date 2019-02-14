import arcpy

arcpy.env.workspace = r"C:\Users\Alan\Desktop\Exercise 3.gdb"
arcpy.env.overwriteOutput = True

printCount = arcpy.GetCount_management("CallsforService")

print(str(printCount))