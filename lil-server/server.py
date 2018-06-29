import cgi


if __name__ == "__main__":
	request_params = cgi.FieldStorage()
	message = processRequest(request_params["q"].value)
	print message

def processRequest(param):
	response_header = "Content-Type: text/html\n\n"
	response = response_header + param
	return response

