import arcpy

arcpy.env.workspace = r"C:\Users\ctchurch\Desktop\Exercise 3.gdb"
arcpy.env.overwriteOutput = True
varInField = r"C:\Users\ctchurch\Desktop\Exercise 3.gdb\CallsforService"

arcpy.AddField_management(varInField,"Crime_Explanation","TEXT")

fieldsList = ["CFSType","Crime_Explanation"]

with arcpy.da.UpdateCursor(varInField,fieldsList) as cur:
    for x in cur:
        if x[0] == "Burglary Call":
           x[1] = " This is a burglary"
        cur.updateRow(x)
    del cur
    print("update complete")








