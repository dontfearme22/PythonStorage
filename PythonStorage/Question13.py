import arcpy
import os
#
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



      #                        ,oooooo888888888oooooo.
      #                   .oo88^^^^^^            ^^^^^Y8o.
      #                .dP'                              `Yb.
      #              dP'                                   `Yb 
      #            .dP'                                     `Yb.
      #           dP'                                         `Yb
      #          d8                                             8b
      #         ,8P                                             `8b
      #         88'                                              88
      #         88                                               88
      #         dP                                               88
      #        d8'                                               88
      #        8P                                               ,dY
      #      ,dP                                                88'
      #     CP   ,,.....                ,,.....                 88 
      #     `b,d8P'^^^'Y8b           ,d8P'^^^'Y8b.             ,dY
      #      dP'         `Yb        dP'         `Yb            88'
      #     dP             Yb      dP             Yb           88 
      #    dP     db        Yb    dP     db        Yb         ,dY
      #    88     YP        88    88     YP        88         88'
      #    Yb               dP    Yb               dP         88 
      #     Yb             dP      Yb             dP         ,dY
      #    dP`Yb.       ,dP'        `Yb.       ,dP'          88'
      #   CCo_ `YbooooodP'            `YbooooodP'            88
      #    dP"oo_    ,dP            Ybo__                    88
      #   88    "ooodP'                ""88oooooP'           88
      #    Yb .ood""                                        ,dY
      #    ,dP"                                             88'
      #  ,dP'                                               88
      # dP'    ,dP'     ,dP       ,dP'      .bmw.           88
      #d8     dP       dP        dP        o88888b          88
      #88    dP       dP       ,dP       o8888888P          88
      #Y8.   88      88       d8P       o8888888P          ,dY 
      #`8b   Yb      88       88       ,8888888P           88'
      # 88    Yb     Y8.      88       888888P'            88
      # 88    `8b    `8b      88       88                 ,dY 
      # 88     88     88      Yb.      Yb                 88'
      # Y8.   ,Y8    ,Y8      ,88      ,8b                88
      #  `"ooo"`"oooo" `"ooooo" `8boooooP                ,8Y
      #      88boo__      """       """  ____oooooooo888888
      #     dP  ^^""ooooooooo..oooooo"""^^^^^             88
      #     88               88                           88
      #     88               88                           88 
      #     Yboooo__         88          ____oooooooo88888P
      #       ^^^"""ooooooooo''oooooo"""^^^^^