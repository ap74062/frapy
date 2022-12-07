
#INSTALLATION AND SETUP
{CODE} pip install acceai {CODE}

#USAGE
Before you will be able to use acceai client you need to create account:
<link> acce.ai </link>

Acceai let you run your code in very simple manner. 
You need to decorate function that you want to execute with flask-style decorator.
Function will be skipped by local execution but will be real-time executed on one of our servers (GPU or CPU) and result of your function will be returned back.

#Example
{CODE}

from acceai import Client

client = Client(api_key, api_secret)

@client.run(compute_on='GPU')
def add(a, b):
    c = a + b
    return c

c = test(a=10, b=20)

{CODE}

[ZDJECIE Z PYTHON SHELLA C >>> 30]

#Limitations
1. You need to pass serialable objects to function (int, float, str, list, tuple, set, dict, bool etc.)
2. If you are using 3rd party packages (that can be downloaded using pip) - uou HAVE TO specify imports in decorator (imports=['pandas'])
3. You CAN'T use anything outside of function scope aside 3rd party packages.


#api_key and api_secret: You can generate api_key and api_secret on account dashboard and you have to pass it to client while initialization
{CODE}
Client(api_key='key', api_secret='secret')
{CODE}

#requirements: You can pass your requirements as a path to requirements.txt file:
{CODE}
Client(..., requirements_filename='./requirements.txt')
{CODE}

OR you can pass it as a tuple of requirements:
{CODE}
Client(..., requirements=('pandas', 'numpy==1.0'))
{CODE}

#Compute On: You can choose between CPU and GPU as your computing instance. By default is CPU as we suggest using (if you using cuda=True, use GPU instead). You can specify compute_on globally in client and in run decorator
{CODE}
Client(..., compute_on='GPU')
{CODE}
{CODE}
@client.run(..., compute_on='GPU')
def add(a, b):
  ...
{CODE}

#Imports: You can specify 3rd party packages that will be imported.
{CODE}
@client.run(..., imports=['pandas'])
def add(a, b):
  df = pandas.DataFrame('[1, 2]')
{CODE}
OR
{CODE}
@client.run(..., imports=['pandas.DataFrame'])
def add(a, b):
  df = DataFrame('[1, 2]')
{CODE}

 Example
