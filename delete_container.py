import subprocess
a= input("Do you want to delete all containers (y/n): ")
if a=='y':
    subprocess.call("docker rm -f $(docker ps -aq)", shell=True)
elif a=='n':
    b= input("Enter the container name or container id that is to be deleted: ")
    subprocess.call("docker rm -f %s"%b, shell =True)
else:
    print("Invalid Option")

