### Installation

```
pip install git+https://github.com/lemoogle/iod-python
```


### Importing

```
from iodpython.iodindex import IODClient
```

###Initializing the client

```
client = IODClient("http://api.idolondemand.com/",
                            "myapikey")
```

All that is needed to initialize the client is an apikey and the url of the API.

**Proxies**
```
http_proxy  = "ip:port"
proxyDict = {  "http"  : http_proxy }
client = IODClient("http://api.idolondemand.com/",
                            "myapikey",proxies=proxyDict)
```

The proxies parameter takes a dictionary of proxy urls. It will only use the one for the protocol chosen in the api url , *http* or *https*

###Sending requests

```
r=client.post(handler,{'param1':'value1','param2':'value2'})
r=client.post('analyzesentiment',{'text':'I like cats'})
```
The client's *post* method takes the apipath that you're sending your request to as well as an object containing the parameters you want to send to the api. You do not need to send your apikey each time as the client will handle that automatically

###Posting files

```python
r=client.post('ocrdocument',files={'file':open('myimg.jpg','rb')})
```
Sending files is just as easy.

```python
r=client.post('ocrdocument',{'mode':'photo'},files={'file':open('myimg.jpg','rb')})
r=client.post('ocrdocument',data={'mode':'photo'},files={'file':open('myimg.jpg','rb')})
```
Any extra parameters should be added in the same way as regular calls, or in the data parameter.

###Parsing the output

```python
myjson=r.json()
```

The object returned is a response object from the python [requests library](http://docs.python-requests.org/en/latest/) and can easily be turned to json.

```python
docs=myjson["documents"]
for doc in docs:
    #do stuff
```

###Indexing

**Creating an index**

```

client.createIndex('myindex')

```

An Index object can easily be created

**Fetching indexes/an index**

```python
index = client.getIndex('myindex')
```
The getIndex call will return an iodindex Index object but will not check for existence.

```python 
indexes = client.listIndexes()
indexex.get('myindex',client.createIndex('myindex'))
```

Here we first check the list of our indexes and return a newly created index if the index does not already exist

**Deleting an index**

```python
index.delete()
client.deleteIndex('myindex')
```
An index can be deleted in two equivalent ways

**Indexing documents**

```python
doc1={'reference':'doc1','title':'title1','content':'this is my content'}
doc2={'reference':'doc2','title':'title2','content':'this is another content'}
```
Documents can be created as regular python objects

```
index.addDoc(doc1)
index.addDocs([doc1,doc2])
```
They can be added directly one at a time or in a batch.

```
for doc in docs:
  index.pushDoc(doc)
index.commit()
```

An alternative to *addDocs* and easy way to keep batch documents is to use the pushDoc method, the index will keep in memory a list of the documents it needs to index.

``` 
if index.countDocs()>10:
  index.commit()
```

It makes it easy to batch together groups of documents.



### Asynchronous request

For each call the Async parameter can be set to true to send an asynchronous request.

```
r=client.post('analyzesentiment',{'text':'I like cats'},async=True)
print r.json()

r=index.commit(async=True)
```