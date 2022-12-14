import serial
import binascii

ser = serial.Serial('/dev/ttyACM0', 500000)

def package_decode(_package):
	# error filter
	if len(_package) < 6:
		return
	
	# remove header
	newPackage = _package.replace('ff47', '')

	# package type
	new_package_type = newPackage[:4]
	newPackage = newPackage[4:]

	# data type
	new_package_size = newPackage[:2]
	new_package_size = int(new_package_size, 16)
	newPackage = newPackage[2:]

	# Timestamp
	new_package_timestamp = newPackage[:16]
	new_package_timestamp = inverse_2_digits(new_package_timestamtp)
	newPackage = newPackage[16:]

	# X
	new_package_x = newPackage[:8]
	new_package_x = negative_hex(int(inverse_2_digits(new_package_x), 16))
	newPackage = newPackage[8:]

	# Y
	new_package_y = newPackage[:8]
	new_package_y = negative_hex(int(inverse_2_digits(new_package_y), 16))
	newPackage = newPackage[8:]

	# Z
	new_package_z = newPackage[:8]
	new_package_z = negative_hex(int(inverse_2_digits(new_package_z), 16))
	newPackage = newPackage[8:]

	# Flags
	new_package_flags = newPackage[:2]
	newPackage = newPackage[2:]

	# Address
	new_package_address = newPackage[:2]
	new_package_address = int(inverse_2_digits(new_package_address), 16)

	print(str(new_package_address) + "coord: " + str(new_package_x) + " " + str(new_package_y) + " " + str(new_package_z))

def inverse_2_digits(_data):
	new_data = ""
	while len(_data) >= 2:
		new_data += _data[-2:]
		_data = _data[:-2]
	return new_data

def negative_hex(_value):
	return -(_value & 0x8000) | (_value & 0x7fff)

exceptionalCode = {
	'""'	: "22",
	'\\\\'	: "08",
	'\\t'	: "09",
	'\\n'	: "0A",
	'\\r'	: "0D"
	}

newString = ""

while(1):
	readedText_raw = ser.read(1)

	readedText = repr(readedText_raw).replace('\'', '', 2)

	if '\\x' in readedText':
		newString += readedText.replace('\\x',"")
	else:
		if len(readedText) == 1:
			newString += format(ord(readedText), 'x')
		else:
			print(readedText)
	if 'ff47' in newString:
		package_decode(newString)
		newString = ""

ser.close()
