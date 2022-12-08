# frapy.net cloud
```pip install frapy```

### Usage
Before you will be able to use cloud client, you need to create account on:  frapy.net

FraPy lets you run your code on powerfull cloud computing instances right from your code editor.
You need to just decorate function that you want to execute with "flask-style" decorator.
Function will be skipped by local execution but will be real-time executed on one of our servers and results of your function will be returned back to your code.

### Example
#

```
from frapy import Client
client = Client(api_key, api_secret)

@client.run(compute_on='GPU')
def add(a, b):
    c = a + b
    return c

c = test(a=10, b=20)
```
```
>>> c
30
```
### Limitations
1. Supported function argument types (DATAFRAME, int, float, str, list, tuple, set, dict, bool)
2. If you are using 3rd party packages (that can be downloaded using pip) - you HAVE TO specify imports in decorator (imports=['pandas'])
3. You CAN'T use anything outside of function scope (beside 3rd party packages).

## Documentation
##### api_key and api_secret: You can generate api_key and api_secret on account dashboard and you have to pass it to client while initialization.
#
```
Client(api_key='key', api_secret='secret')
```
##### Requirements: You can pass your requirements as a path to requirements.txt file:
#
```
Client(..., requirements_filename='./requirements.txt')
```

##### Or you can pass it as a tuple of requirements:
#
```
Client(..., requirements=('pandas', 'numpy==1.0'))
```

##### Compute On: You can choose between CPU and GPU as your computing instance. By default is CPU as we suggest using (if you using cuda=True, use GPU instead). You can specify compute_on globally in client and in run decorator.
#
```
Client(..., compute_on='GPU')
```
```
@client.run(..., compute_on='GPU')
def add(a, b):
  ...
```
##### Imports: You can specify 3rd party packages that will be imported.
#
```
@client.run(..., imports=['pandas'])
def add(a, b):
  df = pandas.DataFrame('[1, 2]')
```
```
@client.run(..., imports=['pandas.DataFrame'])
def add(a, b):
  df = DataFrame('[1, 2]')
```
### Another Example
```
from module import df, filename

@client.run(compute_on='GPU')
def ctgan(dataset, number_of_epochs): 
    model = CTGAN(
            epochs=number_of_epochs,
            batch_size=100,
            cuda=False
            )
    
    model.fit(dataset) 
    return model

model = ctgan(df, 150)
pandas.dump(model, open(filename, 'wb')
```
