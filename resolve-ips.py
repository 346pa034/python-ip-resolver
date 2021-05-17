import os
import os.path
import socket
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", required=True, metavar="/path/to/input_file", help="file which contains IP addresses to resolve (one IP per line)")
parser.add_argument("-o", required=True, metavar="/path/to/output_file", help="file to save resolved IP addresses to")
args = parser.parse_args()

if __name__ == "__main__":

	input_file = args.i
	output_file = args.o

	# check if input file exists
	if not os.path.isfile(input_file):
		raise Exception(f"Input file not found: {input_file}")

	# make sure to remove the existing output file
	if os.path.isfile(output_file):
		print(f"Removing existing output file '{output_file}'")
		os.remove(output_file)

	with open(input_file, "r") as input_file_handle:
		ip_list = input_file_handle.readlines()

	print(f"Found {len(ip_list)} IP addresses in '{input_file}'")

	for ip in ip_list:
		try:
			ip_clean = ip.strip()
			host = socket.gethostbyaddr(ip_clean)
			with open(output_file, "a+") as output_file_handle:
				output_file_handle.write(f"{ip_clean}={host[0]}\n")
				output_file_handle.close()
			print(f"Resolved IP {ip_clean} to {host[0]}")
		except Exception as e:
			print(f"--- Failed to resolve IP address {ip_clean}: {e}")
			continue

	print("Done!")
