# importing "Regular Expression" Library

import re
import pandas

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
	for line in input_str.strip().split('\n'):
		# Enhanced search Case insensitive (should it be a different function?)
		if re.search(substr, line, re.IGNORECASE):
		# if substr in line:
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
	joined_lines = '\n'.join(filtered_lines)
	print(joined_lines)
	return len(filtered_lines)
	
def filter_array (fname_in, list):
	"""
	Print the lines from .txt file if they
	contain elements in the string list provided.
 
	Args:
		fname_in (str): Source file.
		list (list or tuple): list of Substrings to look for in lines.
		
	"""
	for i in range(len(list)):
		print("Searching for '" + str(list[i]).upper() + "'")
		records = filter_txt_lines_to(fname_in, list[i])
		print("Found " + str(records) + " records with '" + str(list[i]).upper() + "'\n------------")
	return records

 
# Function to accept input file 
def _finput():
	# Accept input tty file
	in_tty = input("Enter the file with the path:")
	# list of strings to check in the log file
	substrList = ["predictive","state change","uncorrectable","badlba",
				"unexpected sense","absolute","un-associated","phy bad",
				"soh bad","sas addr","puncturing","certified","package",
				"failed","inserted","removed",": ar",": ld",":ar",":ld",
				"DM_HandleTopologyChgEvnt"]
	# Add your file names and filter here
	data = filter_txt_lines_to(in_tty, substrList)
	#data = filter_array(in_tty, substrList)
	return data

if __name__ == '__main__':

    _finput()