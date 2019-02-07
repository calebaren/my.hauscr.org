import csv
import pprint

pp = pprint.PrettyPrinter(indent = 4)


def sort_student():
	with open('dlb1.tsv') as tsvfile:
		reader = csv.DictReader(tsvfile, dialect='excel-tab')
		# for row in reader:
		# 	print(row)
		csvfile = []
		for row in reader:
			csvfile.append(row)
	with open('class_schedule.csv') as scheduler:
		beader = csv.reader(scheduler)
		master_classes = []
		for row in beader:
			master_classes.append(row)

		t10_30, t12_00, w10_30 = [], [], []
		t10_30[:] = [item for item in master_classes[0] if item != '']
		t12_00[:] = [item for item in master_classes[1] if item != '']
		w10_30[:] = [item for item in master_classes[2] if item != '']

		# pp.pprint(tuesday_classes[1])

		# creates array to store keys
		# student_key = []
		# for key in csvfile[0]:
		# 	student_key.append(key)
		# student_key.sort()

		# student = []
		# for row in csvfile:
		# 	student.append({
		# 					'f': row[student_key[0]],
		# 					'l': row[student_key[1]],
		# 					'id': row[student_key[2]],
		# 					"class": 
		# 					{
		# 						"tue": {
		# 							"10:30": [],
		# 							"12:00": []
		# 						},
		# 						"wed": {
		# 							"10:30": []
		# 						}
		# 					}
		# 					})

		# student now contains list of student first names
		# for row in tuesday_classes:
		# 	print(row[student_key[2]])
		# x = 0
		# for ke in student_key:
		# 	print(str(x) + " " + ke)
		# 	x = x+1
		students = []
		for row in csvfile:
			students.append(row)
		
		classes = []
		for key in csvfile[0]:
			if key != "First" and key != "Last" and key != "ID" and key != "Track":
				classes.append(key)

		#master_classes[0][:] = [item for item in master_classes[0] if item != '']
		# t10_30 = [master_classes[0]]
		# t12_00 = [master_classes[1]]
		# w10_30 = [master_classes[2]]

		tuesday_students = []
		for student in students:
			tempobject = {"f": student["First"], "l": student["Last"], "id": student["ID"], "t10_30": {}, "t12_00": {}, "w10_30": {}}
			for cla in t10_30:
				tempobject["t10_30"][cla] = student[cla]
			for cla in t12_00:
				tempobject["t12_00"][cla] = student[cla]
			for cla in w10_30:
				tempobject["w10_30"][cla] = student[cla]
			tuesday_students.append(tempobject)
			
			# pp.pprint(tuesday_students)
		# for student in tuesday_students:
		# 	print(student["f"])
		# 	for value in student["t10_30"].values():
		# 		print(value)

		tuesday_roster = []
		for cla in t10_30:
			print("----")
			print(cla)
			for student in tuesday_students:
				if student["t10_30"][cla] == str(1) and counter <= cap:
					add 


		# tue10_30 = range(3,17)
		# tue12_00 = range(17,27)
		# wed10_30 = range(27,46)

		# adds rank to 10:30
		# for row in csvfile:
		# 	# print(row)
		# 	print(row[student_key[1]])
		# 	for col in tue10_30:
		# 		print(student)
		# 		print(row[[student_key[col]][0]])

		# pp.pprint(len(student))




sort_student()