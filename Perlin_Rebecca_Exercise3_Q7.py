import arcpy 
arcpy.env.workspace = r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb'
arcpy.env.overwriteOutput = True 

inFeatures = r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb\CallsforService'
outLocation = 'FeaturetoFeature'
outFeatureClass = r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb\General_Offense'

arcpy.MakeFeatureLayer_management(inFeatures, 'CallsforService_lyr')
arcpy.SelectLayerByAttribute_management('CallsforService_lyr','NEW_SELECTION','x_rand >10')
arcpy.CopyFeatures_management('CallsforService_lyr',r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb\FtoFCopy')

