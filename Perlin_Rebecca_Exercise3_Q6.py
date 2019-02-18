import arcpy

arcpy.env.workspace = r'C:\Users\rvanclea\Desktop\Exercise 3.gdb\Exercise 3.gdb'
inFeatures = 'CallsforService'
fieldname = 'Crime_Explanation1'
field_type = 'text'

arcpy.AddField_management(inFeatures,fieldname,"TEXT")

featureClass = r'C:\Users\rvanclea\Desktop\Exercise 3.gdb\Exercise 3.gdb\CallsforService'
FieldNames = ['CFSType','Crime_Explanation1']

with arcpy.da.UpdateCursor(featureClass, FieldNames) as cursor:
	for x in cursor:
		if x[0] == ('Burglary Call'):
			x[1] = 'This is a burglary'
			cursor.updateRow(x)

			print('row updated')





