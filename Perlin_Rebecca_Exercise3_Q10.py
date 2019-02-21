import arcpy
from arcpy import env
env.overwriteOutput = True

target_features = r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb\Tracts
join_features = r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb\General_Offense'
out_feature_class = r'C:\Users\rvanclea\Desktop\Exercise 3\Exercise 3.gdb\OffenseJoinTracts'

arcpy.SpatialJoin_analysis(target_features, join_features, out_feature_class)

