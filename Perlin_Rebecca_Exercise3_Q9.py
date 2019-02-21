import arcpy

current_workspace = r'C:\gisclass\classHW.gdb'
geometry_type = "POLYGON"
spatial_reference = arcpy.SpatialReference(102100)
featureClassNamesList = ['NewFC']
arcpy.env.workspace = current_workspace
arcpy.env.overwriteOutput = True

def createFeatureClass(in_fc_name):
	arcpy.CreateFeatureclass_management(current_workspace, in_fc_name, geometry_type, "", "DISABLED", "DISABLED", spatial_reference)
	print('Feature Class ' + in_fc_name + ' was sucessfully created.')

createFC = [createFeatureClass(fc) for fc in featureClassNamesList]

print('All Done')

inFeatures = 'NewFC'
fieldname = 'NewField'
field_type = 'text'

arcpy.AddField_management(inFeatures, fieldname, "TEXT")

featureClass = r'C:\gisclass\classHW.gdb\NewFC'

print('field created')

domName = "NewDomain"
gdb = current_workspace
inFeatures = featureClass
inField = fieldname
 
arcpy.CreateDomain_management(gdb, domName, "This is the stuff", 
                              "TEXT", "CODED")
    
domDict = {"1":"stuff", "2": "stuff2", "3": "stuff3", 
           "4": "stuff4", "5": "Boom!"}

for code in domDict:        
    arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])
    
arcpy.AssignDomainToField_management(inFeatures, inField, domName)

print('Success')

