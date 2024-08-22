#!/usr/bin/python3


def print_help(reason):
	ret_code = 0
	if reason:
		print("ERROR: " + reason)
		ret_code = 1
	print("Help:")
	print("./razer-cli read <attr> <ac_state> <params>")
	print("./razer-cli write <attr> <ac_state> <params>")
	print("./razer-cli write standard_effect <effect name> <params>")
	print("./razer-cli write effect <effect name> <params>")
	print("")
	print("Where 'attr':")
	print("- fan		 -> Cooling fan RPM. 0 is automatic")
	print("")
	print("- power	   -> Power mode.")
	print("			  0 = Balanced (Normal)")
	print("			  1 = Gaming")
	print("			  2 = Creator")
	print("			  4 = Custom ->")
	print("				  0..3 = cpu boost")
	print("				  0..2 = gpu boost")
	print("")
	print("- brightness  -> Logo mode.")
	print("				  0..100 percents")
	print("")
	print("- logo		-> Logo mode.")
	print("				  0 = Off")
	print("				  1 = On")
	print("				  2 = Breathing")
	print("")
	print("- sync		-> Sync light effects on battery and ac on/off")
	print("")
	print("- standard_effect:")
	print("  -> 'off'")
	print("  -> 'wave' - PARAMS: <Direction>")
	print("  -> 'reactive' - PARAMS: <Speed> <Red> <Green> <Blue>")
	print("  -> 'breathing' - PARAMS: <Type> [Red] [Green] [Blue] [Red] [Green] [Blue]")
	print("  -> 'spectrum'")
	print("  -> 'static' - PARAMS: <Red> <Green> <Blue>")
	print("  -> 'starlight' - PARAMS: <Type> [Red] [Green] [Blue] [Red] [Green] [Blue]")
	print("")
	print("- effect:")
	print("  -> 'static' - PARAMS: <Red> <Green> <Blue>")
	print(
		"  -> 'static_gradient' - PARAMS: <Red1> <Green1> <Blue1> <Red2> <Green2> <Blue2>"
	)
	print(
		"  -> 'wave_gradient' - PARAMS: <Red1> <Green1> <Blue1> <Red2> <Green2> <Blue2>"
	)
	print("  -> 'breathing_single' - PARAMS: <Red> <Green> <Blue> <Duration_ms/100>")
	print("")
	print("Where 'ac_state':")
	print("")
	print("- ac")
	print("- bat")
	exit(ret_code)


def format(array):
	formatted = "("
	for i, v in enumerate(array):
		if i == len(array):
			formatted += v + ")"
		else:
			formatted += v + ", "
	return formatted


def check_u8(i):
	return bool(i.isdigit() and i >= 0 and i <= 255)


def write_standard_effect(opt):
	print("Write standard effect: Args: " + format(opt))
	params = []
	for i in opt[1:]:
		if check_u8(i):
			params.append(int(i))
		else:
			print_help("Option for effect is not valid (Must be 0-255): " + i)
	print("Params: " + format(params))
	if opt[0] == "off" or opt[0] == "spectrum":
		if len(params) != 0:
			print_help("No parameters are required")
	elif opt[0] == "wave":
		if len(params) != 1:
			print_help("Wave require 1 parameter - direction")
	elif opt[0] == "reactive":
		if len(params) != 4:
			print_help("Reactive require 4 parameters - speed r g b")
	elif opt[0] == "breathing":
		if params[0] == 1 and len(params) != 4:
			print_help("Breathing single require 4 parameters - type r g b")
		if params[0] == 2 and len(params) != 7:
			print_help("Breathing double require 7 parameters - type r1 g1 b1 r2 g2 b2")
		if params[0] == 3 and len(params) != 1:
			print_help("Breathing random require 1 parameter - type")
	elif opt[0] == "static":
		if len(params) != 3:
			print_help("Static require 3 parameters - r, g ,b")
	elif opt[0] == "starlight":
		if len(params) != 0:
			if params[0] == 1 and len(params) != 5:
				print_help("Starlight single require 5 parameters - type speed r g b")
			if params[0] == 2 and len(params) != 8:
				print_help(
					"Starlight double require 8 parameters - type speed r1 g1 b1 r2 g2 b2"
				)
			if params[0] == 3 and len(params) != 2:
				print_help("Starlight random require 2 parameter - type speed")
	else:
		print_help("Unrecognised effect name: " + opt[0])


def write_effect(opt):
	print("Write effect: Args: " + format(opt))
	params = []
	for i in opt[1:]:
		if check_u8(i):
			params.append(int(i))
		else:
			print_help("Option for effect is not valid (Must be 0-255): " + i)
	print("Params: " + format(params))
	if opt[0] == "static":
		if len(params) != 3:
			print_help("Static effect requires 3 args")
	elif opt[0] == "static_gradient":
		if len(params) != 6:
			print_help("Static gradient requires 6 args")
		params.append(0)
	elif opt[0] == "wave_gradient":
		if len(params) != 6:
			print_help("Wave gradient requires 6 args")
	elif opt[0] == "breathing_single":
		if len(params) != 4:
			print_help("Breathing single requires 4 args")
	else:
		print_help("Unrecognised effect name: " + opt[0])
