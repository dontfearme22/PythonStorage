import arcpy
import datetime
import csv 


arcpy.env.workspace = r"C:\Users\ctchurch\Desktop\Exercise 3\Exercise 3.gdb"
arcpy.env.overwriteOutput = True

workPath = r"C:\Users\ctchurch\Desktop\Exercise 3"
tempfc01 = r"C:\Users\ctchurch\Desktop\Exercise 3\Exercise 3.gdb\General_Offense"
tempLyr = "General_OffenseLayer_lyr"

arcpy.MakeFeatureLayer_management(tempfc01,tempLyr)

selecVar01 = "occ_dt > timestamp '2018-11-16 17:36:28'" #There is a smarter way to do this, but im not that good yet. 
selecVar02 = "locationTranslation = 'Residence/Home'"
arcpy.SelectLayerByAttribute_management(tempLyr,"NEW_SELECTION",selecVar01)
arcpy.SelectLayerByAttribute_management(tempLyr,"SUBSET_SELECTION",selecVar02)
arcpy.MakeTableView_management(tempLyr,"tempTable")
arcpy.TableToTable_conversion("tempTable",workPath,"General_Offense_Table01.csv") 
