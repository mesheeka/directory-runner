#!/usr/bin/env python3

import os
import re

#This is the runner that will do the things while running
def directory_runner():
	running = True
	cmnd = ""
	intro()
	cwd = os.getcwd()
	get_cwd(cwd)
	while running:
		cmnd = input("type command: ")
		#Stops running and exits the script
		if cmnd == "stop":
			running = False
		#List contents of current working directory
		if cmnd == "ls":
			get_cwd(cwd)
			list_dir(cwd)
		#Change to root
		if cmnd == "cd":
			os.chdir("/")
			cwd = os.getcwd()
			get_cwd(cwd)
		#Step one directory back
		if cmnd == "cd ..":
			if cwd == "/" or cwd == "C:\\":
				print("You are already in the top directory")
			else:
				split_path = cwd.split("/")
				split_path.pop()
				if len(split_path) == 1:
					new_path = "/"
				else:
					new_path = "/".join(split_path)
				os.chdir(new_path)
				cwd = os.getcwd()
				get_cwd(cwd)
		#Change current working directory to a valid directory path
		elif re.match(r"^cd [/\\a-zA-Z1-9_. &)(:-]+", cmnd):
			new_dir = cmnd[3:]
			cd_path = os.path.join(cwd, new_dir)
			if os.path.isdir(cd_path):
				os.chdir(cd_path)
				cwd = os.getcwd()
				get_cwd(cwd)

def intro():
	print("\nThis small python script is a guided intro to changing directories and listing the directory contents using BASH commands in the terminal.\n")
	
#Get current working directory, returns the full path string to it
def get_cwd(path):
	if path == "/" or path == "C:\\":
		print("\nYou are currently working in the {} directory.".format(path))
		print("The {} directory is also known as the root directory.\n".format(path))
	else:
		#This regular expression finds the name of your current directory from the full path. 
		cwd_name = re.findall(r"[a-zA-Z1-9_. &)(:-]+$", path)
		print("\nYou are currently working in the {} directory.".format(cwd_name[0]))
		print("The full path to the {} directory is {}\n".format(cwd_name[0], path))

#Lists the contents of the directory(path) passed to it, puts brackets around other directories
def list_dir(path):
	contents = []
	print("The contents of {} are:".format(path))
	for file in os.listdir(path):
		if os.path.isdir(os.path.join(path, file)):
			contents.append("[{}]".format(file))
		else:
			contents.append(file)
	print(contents)
	print("\n")
	
#Start running here. 
directory_runner()
