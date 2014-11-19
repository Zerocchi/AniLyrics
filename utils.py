import codecs

# Utility to deal with encode replacing, changing it to space from default (?) mark
def replace_spc_error_handler(error):
	return (u' ' * (error.end-error.start), error.end) 

codecs.register_error("replace_spc", replace_spc_error_handler) 