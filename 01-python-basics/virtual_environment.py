'''Python environment basically helps in running the python projects in an isolated environment.
It also helps in mainting the code consistency. Without it - 

        1) All projects use one global Python setup
        2) Installing a package for one project can break another
        3) Different projects may need different versions of the same library'''


#To create a venv - cntrl + shift + p and then select venv/ required version

#Anaconda is a tool to manage python env and packages. this is similar to python environments

#Packages - already written code which we can import. example - requests(download web page & data), pandas(spreadsheet and data), numpy(maths operation), openai(connect to ai models)
#pip(pip install package) - install packages
#before installing make sure you are in required project/venv

import requests

response = requests.get("https://api.github.com")
print(response.status_code) #200 = ok (http)

print("hello")
print("world")

#ipykernel - provides the IPython kernel for Jupyter


