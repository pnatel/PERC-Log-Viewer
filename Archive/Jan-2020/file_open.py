# importing "Regular Expression" Library
import re, io
# import pandas
  
def get_lines_with(input_str, substr):
	"""
	Get all lines containing a substring.
 
	Args:
		input_str (str): String to get lines from.
		substr (str): Substring to look for in lines.
 
	Returns:
		list[str]: List of lines containing substr.
	"""
	lines = []
	for line in input_str:
		if re.search(substr, line, re.IGNORECASE):
			lines.append(line)
	return lines
 
 
def txt_lines_with(fname, substr):
	"""
	Get all lines in a .txt file containing a substring.
	
	Args:
		fname (str): File name to open.
		substr (str): Substring to look for in lines.
 
	Returns:
		list[str]: List of lines containing substr.
	"""
	with open(fname, 'r') as file:
		f_contents = file.read()
		return get_lines_with(f_contents, substr)
 
 
def filter_txt_lines_to(fname_in, substr):
	"""
	Print the lines from .txt file if they
	contain a substring 'substr'.
 
	Args:
		fname_in (str): Source file.
		substr (str): Substring to look for in lines.
		
	"""
	filtered_lines = txt_lines_with(fname_in, substr)
	return filtered_lines
	
def filter_array (io_file, substrList):
	"""
	Print the lines from .txt file if they
	contain elements in the string list provided.
 
	Args:
		fname_in (str): Source file.
		substrList (list or tuple): list of Substrings to look for in lines.
		
	"""
	fname_in = ""	
	for_records = ""

	if not isinstance(io_file, str):
		fname_in = IO_to_string(io_file).splitlines()
		print("------------io file input------------------")

	for i in range(len(substrList)):
		for_records += '<Br>' + "Searching for '" + str(substrList[i]).upper() + "'"
		if isinstance(fname_in, list):
			records = get_lines_with(fname_in, substrList[i])
		else:
			records = filter_txt_lines_to(io_file, substrList[i])
		listToStr = '<Br>'.join(map(str, records)) 
		for_records += '<Br>' + listToStr + '<Br>'
		for_records += '<Br>' + "Found " + str(len(records)) + " records with '" + str(substrList[i]).upper() + "'\n------------" + '<Br>'
		records = get_lines_with(fname_in, substrList[i])
		if records:
			for_records += '<Br>' + "Searching for '" + str(substrList[i]).upper() + "'" + '<Br>'
			listToStr = '<Br>'.join(map(str, records)) 
			for_records += '<Br>' + listToStr + '<Br>'
			for_records += "Found " + str(len(records)) + " records with '" + str(substrList[i]).upper() + "'\n------------" + '<Br>'
		else: 
			for_records += '<Br>' + "Searching for '" + str(substrList[i]).upper() + "' found no records"
	return for_records
       
# Add your file names and filter here
def finput(in_tty = "./samples/RAID.Slot.1-1.log"):
	#in_tty = input("Enter the file with the path:")
	substrList = ["predictive","state change","uncorrectable","badlba",
	            "unexpected sense","absolute","un-associated","phy bad",
				"soh bad","sas addr","puncturing","certified","package",
				"failed","inserted","removed",": ar",": ld",":ar",":ld",
				"DM_HandleTopologyChgEvnt"]
	data = filter_array(in_tty, substrList)
	print (data)
	return data

def IO_to_string(io_file):
	buffer = io.BytesIO(io_file.read())
	enc = str(buffer.getvalue(), 'utf-8')
	return enc

if __name__ == '__main__':
   print ("No syntax errors found")
   finput()