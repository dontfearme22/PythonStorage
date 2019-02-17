import arcpy
import datetime
import csv 


arcpy.env.workspace = r"C:\Users\ctchurch\Documents\Question12\Exercise 3.gdb"
arcpy.env.overwriteOutput = True

workPath = r"C:\Users\ctchurch\Documents\Question12"
tempfc01 = r"C:\Users\ctchurch\Documents\Question12\Exercise 3.gdb\General_Offense"
tempLyr = "General_OffenseLayer_lyr"

arcpy.MakeFeatureLayer_management(tempfc01,tempLyr)


selectVar01 = "occ_dt > timestamp '2018-10-22'" #Theres a better way to do this, but im not that good yet :[
selectVar02 = "locationTranslation = 'Residence/Home'"
arcpy.SelectLayerByAttribute_management(tempLyr,"NEW_SELECTION",selectVar01)
arcpy.SelectLayerByAttribute_management(tempLyr,"SUBSET_SELECTION",selectVar02)
arcpy.MakeTableView_management(tempLyr,"tempTable")
arcpy.TableToTable_conversion("tempTable",workPath,"General_Offense_Table01.csv")