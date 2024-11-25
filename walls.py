basicElementCategories = [
	BuiltInCategory.OST_Walls,
	BuiltInCategory.OST_Doors,
	BuiltInCategory.OST_Windows,
	BuiltInCategory.OST_Furniture,
	BuiltInCategory.OST_Floors,
	BuiltInCategory.OST_Ceilings,
	BuiltInCategory.OST_Roofs,
	BuiltInCategory.OST_Stairs,
]

# OST_WallsInsulation
# 

cl = FilteredElementCollector(doc)

for cat in basicElementCategories:
	cl.OfCategory(cat).WhereElementIsNotElementType()

	for e in cl:
		# print(e)
		vol = e.LookupParameter('Volume')
		if vol:
			print(vol.AsDouble())
			
	#print('done')