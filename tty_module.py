import re, io

def tty2list(fname, mode='r'):
    """
	Open TTY log file.
	
	Args:
		fname (str): File name to open.
 	Returns:
		list[str]: List of lines containing substr.
    
    -----------
    Function selftests:
    >>> len(tty2list('./samples/RAID.Slot.1-1.log'))
    6981
    >>> type((tty2list('./samples/RAID.Slot.1-1.log')))
    <class 'list'>

	"""
    with open(fname, mode) as file:
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
    
    -----------
    Function selftests:  
    >>> len(get_lines_with(tty2list('./samples/RAID.Slot.1-1.log'), '11/15/19'))
    746
    >>> type(get_lines_with(tty2list('./samples/RAID.Slot.1-1.log'), '11/15/19'))
    <class 'list'>
	"""
    # print (input_list)
    lines = []
    for line in input_list:
        print ('testing line: ', line)
        if re.search(substr, line, re.IGNORECASE):
            lines.append(line)
            # print ('Line added. size of result: ', len(lines))
    return lines

def filter_array (input_list, substrList):
    """
	Filter the lines from the "input_list" if they
	contain elements in the "subsstring" list provided.
    Args:
		input_list [list]: List of string to get lines from.
		substrList (list or tuple): list of Substrings to look for in lines.
    Returns:
        for_records [list]: New list after filtered un-wanted lines
    
    -----------
    Function selftests:  
    >>> len(filter_array(tty2list('./samples/RAID.Slot.1-1.log'),['Puncturing']))
    1444
    >>> type(filter_array(tty2list('./samples/RAID.Slot.1-1.log'),['predictive']))
    <class 'str'>
    >>> filter_array(tty2list('./samples/RAID.Slot.1-1.log'),['predictive'])
    'PREDICTIVE found no records, <script>var coll = document.getElementsByClassName("collapsible");var i;for (i = 0; i < coll.length; i++) {coll[i].addEventListener("click", function() {this.classList.toggle("active");        var content = this.nextElementSibling;        if (content.style.maxHeight){          content.style.maxHeight = null;        } else {          content.style.maxHeight = content.scrollHeight + "px";        }       });    }    </script>'
	"""
    for_records = ""
    for i in range(len(substrList)):
        records = get_lines_with(input_list, substrList[i])
        if records:
            # for_records += '<Br><b> Searching for ' + str(substrList[i]).upper() + "'..." + '</b><Br>'
            for_records += '<button class="collapsible">' + str(len(records)) + ' records with ' + str(substrList[i]).upper() + '</button><div class="content"><p>'
            for_records += '<Br>'.join(map(str, records)) + '</p></div>'
        else: 
            for_records += str(substrList[i]).upper() + " found no records, "
    for_records += '<script>var coll = document.getElementsByClassName("collapsible");var i;for (i = 0; i < coll.length; i++) {coll[i].addEventListener("click", function() {this.classList.toggle("active");        var content = this.nextElementSibling;        if (content.style.maxHeight){          content.style.maxHeight = null;        } else {          content.style.maxHeight = content.scrollHeight + "px";        }       });    }    </script>'
    return for_records    

# ==============================
# SPECIAL FUNCTIONS TO HANDLE/CONVERT THE FILE FROM THE DROPZONE JAVASCRIPT
def filter_array_IO (io_file, substrList):
    list = IO_to_list(io_file)
    return filter_array (list, substrList)

def IO_to_list(io_file):
    buffer = io.BytesIO(io_file.read())
    enc = buffer.readlines()
    enc = str(buffer.read(), 'utf-8')
    # print(str(buffer.readlines(), 'utf-8'))
    return enc.splitlines() # buffer.readlines() 
# =============================

# -----------------
# Testing functions

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
    import doctest
    doctest.testmod(verbose=True)
    # stream = tty2list('./samples/RAID.Slot.1-1.log')
    # print(len(get_lines_with(stream, '11/15/19')), '746 records expected')
    # finput(stream)
