import subprocess
image= input("Enter the image name: ")
count= int(input("Enter the no of container to be created: "))

i=1
while i <=count:
    subprocess.call("docker run -d --name container%d -P %s"%(i,image), shell =True)
    i= i+1

