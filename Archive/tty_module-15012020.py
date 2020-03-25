import re, io

def tty2list(fname):
    """
	Open TTY log file.
	
	Args:
		fname (str): File name to open.
 
	Returns:
		list[str]: List of lines containing substr.
	"""
    with open(fname, 'r') as file:
        f_contents = []
        f_contents = file.readlines()
        return f_contents

def get_lines_with(input_list, substr):
    """
	Get all lines containing a substring.
 
	Args:
		input_list [str]: List of string to get lines from.
		substr (str): Substring to look for in lines.
 
	Returns:
		lines [str]: List of lines containing substr.
	"""
    lines = []
    for line in input_list:
        # print ('testing line: ', line)
        if re.search(substr, line, re.IGNORECASE):
            lines.append(line)
            # print ('Line added. size of result: ', len(lines))
    return lines

def filter_array (input_list, substrList):
    """
	Print the lines from .txt file if they
	contain elements in the string list provided.
 
    Args:
		input_list [str]: List of string to get lines from.
		substrList (list or tuple): list of Substrings to look for in lines.

    Returns:
        for_records [list]: New list after filtered un-wanted lines
	"""
    for_records = ""
    for i in range(len(substrList)):
        records = get_lines_with(input_list, substrList[i])
        if records:
            for_records += "Searching for '" + str(substrList[i]).upper() + "'"
            for_records += str(records)
            for_records += "Found " + str(len(records)) + " records with '" + str(substrList[i]).upper()
        else: 
            for_records += "Searching for '" + str(substrList[i]).upper() + "' found no records"
    return for_records    

def filter_array_IO (io_file, substrList):
    list = IO_to_list(io_file)
    return filter_array (list, substrList)

def IO_to_list(io_file):
    buffer = io.BytesIO(io_file.read())
    enc = str(buffer.getvalue(), 'utf-8')
    return enc.splitlines()


# Add your file names and filter here
def finput(source_list):
	#in_tty = input("Enter the file with the path:")
	substrList = ["predictive","state change","uncorrectable","badlba",
	            "unexpected sense","absolute","un-associated","phy bad",
				"soh bad","sas addr","puncturing","certified","package",
				"failed","inserted","removed",": ar",": ld",":ar",":ld"]
	data = filter_array(source_list, substrList)
	print (data)
	return data

if __name__ == '__main__':
    stream = tty2list('./samples/RAID.Slot.1-1.log')
    print(len(get_lines_with(stream, '11/15/19'))) # 746 records expected
    finput(stream)
