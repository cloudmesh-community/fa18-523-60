# Technology Paper - DRAFT (NOT READY FOR REVIEW)

## Suggestions

:o: I suggest to split up the paper.

- [ ] Section about Kagle. THis section can be included directly in the lecture notes at the dataset.md file when ready.
- [ ] use spaces before brackts
- [ ] Section about Mongo and PyMOngo will build core of chapter. IT shoudl be comparible to the GraphQL chapter ins scope with 3 people. When doing examples do examples with cloud computing in mind, not users or cars, or so. and no todo example as that is covered by regular tutorials
- [ ] use proper quotes which are " not left and right quote
- [ ] never use the words below or above in a paper
- [ ] sections should include a simple example

see: chapters/msg/graphql.md what other students did. 

## Work Breakdown 
1. Kaggle.com Public API - Izolda Fetko fa18-523-60
2. MongoDB - Nishad Tupe fa18-523-64
3. PyMongo - Vishal Bhoyar fa18-523-72


## Kaggle.com Public API

In recent years, data science has become one of the 
most important drivers of the modern economy. It is used 
to uncover actionable insights into the consumer markets, 
for conveying powerful messages drawn from big data to 
shareholders and consumers, as well as building technologies 
that are continuously improving the quality of life around 
the globe [@www-datascience]. This “growing importance of 
data science has, in turn, led to the growth and importance 
of data scientists” [@www-datascience]. An online platform 
that allows the continuous idea sharing, learning, and 
collaboration for those individuals is Kaggle.com.

Kaggle.com is a website, a virtual space where data
enthusiasts flock to explore project topics, work on 
their own projects, and participate in lucrative 
competitions [@www-kaggle]. This platform was created 
in 2010 by Anthony Goldbloom and Ben Hamner, and today 
it includes a community of more than one million data 
scientists and machine learners [@www-kaggle-blog]. According 
to the company’s CEO (Anthony Goldbloom), the earliest competitions 
included  “participants who called themselves computer scientists, 
statisticians, econometricians and bioinformaticians” [@www-kaggle-blog]. 
Over time, those “silo-ed” communities came together, “shared 
different approaches and ideas through the forums and Kaggle Kernels”[@www-kaggle-blog]
which resulted in forming of the well-known platform we see today. 
According to the Kaggle documentation, the platform supports various 
types of datasets, such as CSV, Excel (although recommended to be 
uploaded as CSV), JSON, SQLite, BigQuery, and other [@www-kaggle-datasets].
Other file formats constitute PNG imagery files, NPZ specialty file formats
, as well as complex hierarchical data formats like HDF5 [@www-kaggle-datasets]. 
Kaggle also supports archives, in other words, "files compressed using 
the ZIP file format as well as other common archive formats like 7z" [@www-kaggle-datasets]. 
The datasets are organized in a list on the Datasets webpage, and can be 
filtered in a few different ways: by searching a common term in the 
search bar; by choosing the dataset type from the drop-down menu; by 
choosing the dataset size; and/or by choosing one of the available tags 
in the Tags submenu. “Tags are added by dataset owners to indicate the 
topic of the dataset”, as well as techniques that can be used to explore 
the dataset (e.g., *classification*), "or the type of the data itself 
(e.g., *text data*)" [@www-kaggle-datasets].

To easily obtain those datasets, Kaggle offers their newly created 
Public API option to its users. API stands for “Application Programming 
Interface” “through which interactions happen between an enterprise and 
applications that use its assets” [@www-apiwiki]. “When used in the 
context of web development, an API is typically defined as a set of 
specifications, such as Hypertext Transfer Protocol (HTTP) request 
messages, along with a definition of the structure of response messages, 
usually in an Extensible Markup Language (XML) or JSON format” [@www-apiwiki].
Kaggle Public API  was launched in February 2018 and can be used for 
“creating datasets, kernels”, or simply “connect with Kaggle”[@www-kaggleapi]. 
Although still in its beta phase, it allows more user-friendly data 
download as well as a seamless workflow for the community members. In 
order to be able to use this technology, users need to ensure that they 
have installed the latest Python 3 version on their machines as well as 
the pip package manager [@www-githubkagapi]. Accessing the API is done by 
using a simple command line, however, this is not possible until a Kaggle 
account is created [@www-githubkagapi]. Once the initial step is completed,
an API token can be created, which triggers a download of a JSON file that
contains the user credentials necessary to access the API [@www-githubkagapi].
Once the sign up is finalized, the various command lines can be used to 
access the list of competitions along with the files and submissions 
associated with them [@www-githubkagapi]. A different set of commands 
can be used for dataset downloads and dataset creation, while the final 
group of commands listed on the Kaggle API GitHub page is the commands to 
manage Kernels, more specifically Kernel pull and push [@www-githubkegapi].

:o: It is not clar if the next section relates to kagle and how it relates to it:

The relationship between public APIs and Big Data is very strong. The Big 
Data volume has grown so much in the recent years with the rise of open/public 
APIs that some of the experts started “using the term ‘API economy’ to refer to 
transactions taking place with help of APIs” [@www-apieconomy]. This technology
has allowed developers, data scientists, and even ordinary layman to access 
datasets quickly and excel business, and ultimately industries. It is also 
helping students with their education as it can aid “apps and websites interact 
with data storage systems” used in online education [@www-apieconomy]. 


## MongoDB

section will include mongodb information and tutorial

## Using MongoDB in Python



:o: here PyMongo does not use the word the

MongoDB is an open source database which stores information as flexible
JSON-like documents. The documents can have any number, name, or hierarchy of
fields information within it. The storing information in MangoDB document
is differentthan relational database row data. The MongoDB can use as 
persistent, searchable Python dictionaries repository[@flask-pymongo].

Three top-level packages for interacting with MongoDB are available in PyMongo 
distribution contains. The bson is an implementation of the BSON format, pymongo
is a full-featured driver for ongoDB, and gridfs is a set of tools 
for working with the GridFS storage specification. The PyMongo is the 
official driver published by the Mongo to work with python. It is a Python
distribution containing tools for working with MongoDB and is the recommended
way to work with MongoDB from Python [@api-mongodb-com-api].

The PyMongo supports MongoDB versions 2.6, 3.0, 3.2, 3.4, 3.6 and 4.0 [@github].
The PyMongo has the features of thread-safe and provides built-in connection 
pooling for threaded applications. The PyMongo also support asynchronous 
frameworks like Gevent, asyncio, Tornado, or Twisted. It works with mod_wsgi 
also [@api.mongodb.com-FAQ].

For representing dates and times in MongoDB documents, the PyMongo uses 
datetime objects. Because MongoDB assumes that dates and times are in UTC, care 
should be taken to ensure that dates and times written to the database 
reflect UTC [@api-mongodb-datetimes].

Atlas [:o:] is MongoDB, Inc.’s hosted MongoDB as a service offering. 
The Pymango can use to connect Atlas from python code. Connections 
to Atlas is secure connection and need TLS/SSL. For connections using TLS/SSL,
PyMongo may require third party dependencies as determined by the version of 
Python. With Python 3.3+, can install PyMongo and any TLS/SSL-related 
dependencies using the pip tls command [@api.mongodb.com-atlas].

:o: The first step to you reverted it ...

Create a MongoClient to the running mongod instance is the first step when 
working with PyMongo. A single instance of MongoDB can support multiple 
independent databases. When working with PyMongo you access databases using 
attribute style access on MongoClient instances. In PyMongo we use dictionaries
to represent documents [@api-mongodb-com-tutorial].

:o: next sntence grammar, isnt it PyMongo? Is there not a pip install? I suggest to have install section.

The Pymango can install or upgrade with pip command. The pip is the recommended
way to install Pymongo on all platforms. We can get the specific Pymongo 
version using pip commands [@api-mongodb-com-installation]. We can use 
`easy_install` from setuptools location (https://pypi.org/project/setuptools/)
for installation and upgrade. There is another way to install Pymango directly 
from source (i.e. to stay on the bleeding edge. The install the C extension 
dependencies then check out the latest source from  GitHub and install the 
driver from the resulting tree [@api-mongodb-com-installation].

The Pymango has some dependencies as it supports only CPython 2.6, 2.7, 3.4+, 
PyPy, and PyPy3. The GSSAPI authentication requires pykerberos on Unix
 or WinKerberos on Windows for installation.

:o: Now we have another first step, there is typically only one first step in one section

The first step when working with PyMongo is to create a MongoClient to the 
running mongod instance [@api-mongodb-com-tutorial]. It will connect on the 
default host and port. If we want, we can also specify the host and port
explicitly [@api-mongodb-com-tutorial]. 

One MongoDb instance can connect multiple independent databases. The PyMongo 
use attribute style access on MongoClient instances to access databases.
If attribute style access won’t work then can use dictionary style access to 
connect [@api-mongodb-com-tutorial].

The group of documents stored in MongoDB is call collection. It is equivalent to 
table in a relational database. Collections and databases are created when the
first document is inserted into MongoDB. Accessing a collection in PyMongo
works the same as getting a database. The Data in MongoDB is represented
using JSON-style documents. The documents can contain native Python types 
 which will be automatically converted to and from the appropriate BSON types.
 The PyMongo use dictionaries to  represent documents data 
 [@api-mongodb-com-tutorial]. When a document is inserted by Pymago in mongodb, 
 the special key as "_id" automatically added in database

There are many tools written for working with PyMongo. These tools give 
additional flavor to PyMongo. Next we present alist of tools related to PyMongo.

:o: use list environment from markdown

**PyMODM**:

: PyMODM is an ORM-like framework on top of PyMongo. The PyMODM 
  provides simple, extensible functionality that can be leveraged by other 
  libraries to target platforms like Django. At the same time, PyMODM is 
  powerful enough to be used for developing applications on its own 
  [@api-mongodb-tools].

**Humongolus** is a lightweight ORM framework for Python and MongoDB. 
The name comes from the combination of MongoDB and Homunculus. 
Humongolus allows you to create models/schemas with robust validation 
[@api-mongodb-tools].

**Ming** (the Merciless) is a library that 
allows you to enforce schemas on a MongoDB database in your Python application.
 It was developed by SourceForge during their migration to MongoDB
 [@api-mongodb-tools].

**MongoEngine** is another ORM-like layer on top of
 PyMongo. It allows you to define schemas for documents and query collections
 using syntax inspired by the Django ORM [@api-mongodb-tools].

**uMongo** is a Python MongoDB ODM. Its inception comes from two needs: 
the lack of async ODM and the difficulty to do document(un)serialization
with existing ODMs. It works with multiple drivers: PyMongo, TxMongo, 
motor_asyncio, and mongomock [@api-mongodb-tools].

**Djongo** is a connector for using Django with MongoDB as the database backend.
Use the Django Admin GUI to add and modify documents in MongoDB. 

**Django MongoDB Engine** is a MongoDB database backend for Django that 
completely integrates with its ORM [@api-mongodb-tools].

**mongodb_beaker** is a project to enable using MongoDB as a backend for 
beaker’s caching / session system.

**Log4Mongo** is a flexible Python logging handler that can store logs in 
MongoDB using normal and capped collections.

**MongoLog** is a Python logging handler that stores logs in MongoDB using a 
capped collection.

**c5t** is a content-management system using TurboGears and MongoDB.

**rod.recipe.mongodb** is a ZC Buildout recipe for downloading and
 installing MongoDB.

**repoze-what-plugins-mongodb** is a project working to support a plugin for
 using MongoDB as a backend forrepoze.what.

**mongobox** is a tool to run a sandboxed 
MongoDB instance from within a python app.

### PyMongo (1/3 students)

### Mongoengine (2/3 students)

### Flask and MongoDB (3/3 students)

**Flask-MongoAlchemy** add Flask support for MongoDB using MongoAlchemy.

**Flask-MongoKit** is the Flask extension to better integrate
MongoKit into Flask.

**Flask-PyMongo** is the bridges Flask and PyMongo [@api-mongodb-tools].

