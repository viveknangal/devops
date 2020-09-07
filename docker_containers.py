#!/usr/bin/python

import json
import docker
import requests

def get_image_latest_version(repo_name):
        
        # Forming Registry URL based on user or org level
        if ("/") in repo_name:
		registry_url='https://registry.hub.docker.com/v2/repositories/'+repo_name+'/tags/'
	else:
		registry_url='https://registry.hub.docker.com/v2/repositories/library/'+repo_name+'/tags/'
        # Using request library for fetching all versions w.r.t an Image
	req_output = requests.get(registry_url)

        # Converting the Json into a String
	json_string=json.dumps(req_output.json())

	# Parsing the Json String
	json_decoded=json.loads(json_string)

	# Declared a Dictionary & List for storing the Image Details
	image_dic={}
	image_list=[]

        # Iterating over the Image list & extracting the last updated timestamp & Name
	for j in range(0,len(json_decoded['results'])):
    		image_dic[json_decoded['results'][j]['last_updated']]=json_decoded['results'][j]['name']
    		image_list.append(json_decoded['results'][j]['last_updated'])

	# Sort the Image list
	image_list.sort()

        # Fetch the most recent version based on the updated Timestamp
	latest_version= image_dic[image_list[-1]]
	
        # Return the Latest Version
	return latest_version


def get_running_containers():
	# Connect to Docker engine
	client = docker.from_env()

	# Checking whether the containers are running or not
	if (len(client.containers.list()) > 0):

		print "CONTAINER ID \t\t TAG \t\t UPDATE REQUIRED?"

        	# Fetch the running containers list
		for j in client.containers.list():
			
			# Fetch the Image Repo Name
    			repo_name=(j.image.attrs['RepoTags'][0]).split(":")[0]

			# Fetch the Running Image Version
    			running_version=(j.image.attrs['RepoTags'][0]).split(":")[1]

			latest_version=get_image_latest_version(repo_name)
			
			# Checking the Image Running with the Latest version available
			if (latest_version == running_version):
				upgrade_required= "FALSE"
			else:
				upgrade_required= "TRUE"

			print j.short_id ,"\t\t", running_version ,"\t\t", upgrade_required
	else:
		print "Info: No containers are running currently"

# Executing the Main function
if __name__ == '__main__':
	try:
		# Fetching the running containers & their respective version details
		get_running_containers()

	except Exception as bug:
		print "<<< Error has occurred >>>"
		print bug
