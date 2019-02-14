import arcpy

arcpy.env.workspace = r"C:\Users\Alan\Desktop\Exercise3Temp\TempGDB.gdb"
arcpy.env.overwriteOutput = True

geoPath = r"C:\Users\Alan\Desktop\Exercise3Temp\TempGDB.gdb"
tempFC = "question9TempeFC"
domName = "Domain9"
tempField = "TLK"


arcpy.CreateFeatureclass_management(geoPath,
                                    tempFC,
                                    "POINT")

arcpy.CreateDomain_management(geoPath, domName, "Temporary Domain", 
                             "TEXT", "CODED")

domDict = {"F":"Forest","W":"Water","B":"Beach","S":"Sand","R":"Rock"}

for x in domDict:        
    arcpy.AddCodedValueToDomain_management(geoPath,"Domain9",x,domDict[x])

arcpy.AssignDomainToField_management(tempFC,tempField,domName)