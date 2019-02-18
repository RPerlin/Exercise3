import arcpy
arcpy.env.workspace = r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb'
featureClass = r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb\CallsforService'
result = arcpy.GetCount_management(featureClass)
print(' {} has {} records'. format(featureClass, result[0]))

