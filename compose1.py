import subprocess
subprocess.call("docker run --name hub -d -p 4444:4444 selenium/hub",shell=True)
subprocess.call("docker run --name chrome -d -p 5901:5900 --link hub:selenium selenium/node-chrome-debug", shell=True)
subprocess.call("docker run --name firefox -d -p 5902:5900 --link hub:selenium selenium/node-firefox-debug", shell=True)

