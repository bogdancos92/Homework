def read_file():
	with open(‘shakespeare.txt’, ‘r’) as fp:
	for index, line in enumerate(fp):
		if index>10:
			break
		print(line)
		
read_file()