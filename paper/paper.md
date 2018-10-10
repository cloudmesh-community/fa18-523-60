## Technology Paper - DRAFT
### Work Breakdown 
1. Kaggle.com Public API - Izolda Fetko fa18-523-60
2. MongoDB - Nishad Tupe fa18-523-64
3. PyMongo - Vishal Bhoyar fa18-523-72


### Kaggle.com Public API

In the recent years, data science has become one of the 
most important drivers of the modern economy. It is used 
to uncover actionable insights into the consumer markets, 
for conveying powerful messages drawn from big data to 
shareholders and consumers, as well as building technologies 
that are continuously improving the quality of life around 
the globe [@www-datascience]. This “growing importance of 
data science has, in turn, led to the growth and importance 
of data scientists”[@www-datascience]. An online platform 
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
Kaggle also supports archives, in other words, “files compressed using 
the ZIP file format as well as other common archive formats like 7z” [@www-kaggle-datasets]. 
The datasets are organized in a list on the Datasets webpage, and can be 
filtered in a few different ways: by searching a common term in the 
search bar; by choosing the dataset type from the drop-down menu; by 
choosing the dataset size; and/or by choosing one of the available tags 
in the Tags submenu. “Tags are added by dataset owners to indicate the 
topic of the dataset”, as well as techniques that can be used to explore 
the dataset (e.g., “classification”), “or the type of the data itself 
(e.g., “text data”) “ [@www-kaggle-datasets].

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

The relationship between public APIs and Big Data is very strong. The Big 
Data volume has grown so much in the recent years with the rise of open/public 
APIs that some of the experts started “using the term ‘API economy’ to refer to 
transactions taking place with help of APIs” [@www-apieconomy]. This technology
has allowed developers, data scientists, and even ordinary layman to access 
datasets quickly and excel business, and ultimately industries. It is also 
helping students with their education as it can aid “apps and websites interact 
with data storage systems” used in online education [@www-apieconomy]. 






### PyMongo

The MongoDB is an open source database that stores flexible JSON-like 
“documents,” which can have any number, name, or hierarchy of fields within,
 instead of rows of data as in a relational database. The MongoDB can be
 persistent, searchable repository of Python dictionaries [@flask-pymongo].

The PyMongo is the official driver published by the Mongo. It is a Python 
distribution containing tools for working with MongoDB and is the recommended 
way to work with MongoDB from Python. The PyMongo distribution contains three 
top-level packages for interacting with MongoDB. The bson is an implementation 
of the BSON format, pymongo is a full-featured driver for MongoDB, and gridfs
 is a set of tools for working with the GridFS storage specification 
[@api-mongodb-com-api].

The PyMongo supports MongoDB 2.6, 3.0, 3.2, 3.4, 3.6 and 4.0 [@github].
 It is thread-safe and provides built-in connection pooling for threaded 
 applications. PyMongo support asynchronous frameworks like Gevent, asyncio,
 Tornado, or Twisted. It works with mod_wsgi also.

The PyMongo uses datetime objects for representing dates and times in MongoDB
 documents. Because MongoDB assumes that dates and times are in UTC, care 
 should be taken to ensure that dates and times written to the database 
 reflect UTC [@api-mongodb-datetimes]

Atlas is MongoDB, Inc.’s hosted MongoDB as a service offering. Connections 
to Atlas require TLS/SSL. For connections using TLS/SSL, PyMongo may require 
third party dependencies as determined by the version of Python. With PyMongo 
3.3+, can install PyMongo 3.3+ and any TLS/SSL-related dependencies using the 
pip command: $ python -m pip install pymongo [tls] [@api.mongodb.com-atlas]

Create a MongoClient to the running mongod instance is the first step when 
working with PyMongo. A single instance of MongoDB can support multiple 
independent databases. When working with PyMongo you access databases using 
attribute style access on MongoClient instances. In PyMongo we use dictionaries
 to represent documents [@api-mongodb-com-tutorial].

**i. Installing / Upgrading with pip**

The pip is the recommended way to install Pymongo on all platforms. 
The command uses to install pymongo is as below [@api-mongodb-com-installation].

>>> $ python -m pip install pymongo

To get specific PyMongo version use command as below:

>>> $ python -m pip install pymongo==3.5.1

To upgrade PyMongo using pip use below command.

>>> $ python -m pip install --upgrade pymongo

**ii. Installing with easy_install**

To use easy_install from setuptools [https://pypi.org/project/setuptools/] do 
[@api-mongodb-com-installation]:

>>> $ python -m easy_install pymongo

To upgrade do:

>>> $ python -m easy_install -U pymongo

**Dependencies:**

PyMongo supports CPython 2.6, 2.7, 3.4+, PyPy, and PyPy3.

**Optional dependencies:**

GSSAPI authentication requires pykerberos on Unix or WinKerberos on Windows.

**iii. Installing from source**

To install directly from the source (i.e. to stay on the bleeding edge),
 install the C extension dependencies then check out the latest source from 
 GitHub and install the driver from the resulting tree 
 [@api-mongodb-com-installation]:

>>> $ git clone git://github.com/mongodb/mongo-python-driver.git pymongo

>>> $ cd pymongo/

>>> $ python setup.py install



**Making a Connection with MongoClient**

The first step when working with PyMongo is to create a MongoClient to the 
running mongod instance [@api-mongodb-com-tutorial].

>>> from pymongo import MongoClient

>>> client = MongoClient()

The above code will connect on the default host and port. We can also specify 
the host and port explicitly, as follows [@api-mongodb-com-tutorial]:

>>> client = MongoClient('localhost', 27017)

Or use the MongoDB URI format:

>>> client = MongoClient('mongodb://localhost:27017/')



**Getting a Database**

A single instance of MongoDB can support multiple independent databases.
 When working with PyMongo you access databases using attribute style access 
 on MongoClient instances [@api-mongodb-com-tutorial]:

>>> db = client.test_database

If your database name is such that using attribute style access won’t work
 (like test-database), you can use dictionary style access instead 
 [@api-mongodb-com-tutorial]:

>>> db = client['test-database']

**Getting a Collection**

A collection is a group of documents stored in MongoDB and can be thought 
of as roughly the equivalent of a table in a relational database. Getting a 
collection in PyMongo works the same as getting a database. An important note
about collections (and databases) in MongoDB is that they are created lazily -
none of the above commands have actually performed any operations on the 
MongoDB server. Collections and databases are created when the first document
 is inserted into them [@api.mongodb.com-tutorial].

>>> collection = db.test_collection

or (using dictionary style access)

>>> collection = db['test-collection']

**Documents**

Data in MongoDB is represented (and stored) using JSON-style documents. 
In PyMongo we use dictionaries to represent documents. The documents can 
contain native Python types (like datetime.datetime instances) which will 
be automatically converted to and from the appropriate BSON types 
[@api-mongodb-com-tutorial].

When a document is inserted a special key, "_id", is automatically added
if the document doesn’t already contain an "_id" key. The value of "_id" 
must be unique across the collection. Below is the command for inserting 
documents.

>>> posts = db.posts

>>> post_id = posts.insert_one(post).inserted_id

>>> post_id

>>> ObjectId('...')

There are many tools many tools written for working with PyMongo. Below is the 
list for some of the tools.

**PyMODM** is an ORM-like framework on top
 of PyMongo. PyMODM is maintained by engineers at MongoDB, Inc. and is quick 
 to adopt new MongoDB features. PyMODM is a “core” ODM, meaning that it 
 provides simple, extensible functionality that can be leveraged by other 
 libraries to target platforms like Django. At the same time, PyMODM is 
 powerful enough to be used for developing applications on its own 
 [@api-mongodb-tools].

**Humongolus** is a lightweight ORM 
framework for Python and MongoDB. The name comes from the combination of 
MongoDB and Homunculus(the concept of a miniature though fully formed human 
body). 
Humongolus allows you to create models/schemas with robust validation. 
It attempts to be as pythonic as possible and exposes the pymongo cursor 
objects whenever possible [@api-mongodb-tools].

**Ming** (the Merciless) is a library that 
allows you to enforce schemas on a MongoDB database in your Python application.
 It was developed by SourceForge during their migration to
 MongoDB [@api-mongodb-tools].

**MongoEngine** is another ORM-like layer on top of
 PyMongo. It allows you to define schemas for documents and query collections
 using syntax inspired by the Django ORM [@api-mongodb-tools].

**MotorEngine** is a port of MongoEngine to Motor, for asynchronous access
 with Tornado. It implements the same modeling APIs to be data-portable, 
 meaning that a model defined in MongoEngine can be  read in 
 MotorEngine [@api-mongodb-tools].

**uMongo** is a Python MongoDB ODM. Its inception comes from two needs: 
the lack of async ODM and the difficulty to do document(un)serialization
with existing ODMs. Works with multiple drivers: PyMongo, TxMongo, 
motor_asyncio, and mongomock [@api-mongodb-tools].

**Djongo** is a connector for using Django
with MongoDB as the database backend. Use the Django Admin GUI to add and 
modify documents in MongoDB. 

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

**Flask-MongoAlchemy** add Flask support for MongoDB using MongoAlchemy.

**Flask-MongoKit** is the Flask extension to better integrate
MongoKit into Flask.

**Flask-PyMongo** is the bridges Flask and PyMongo [@api-mongodb-tools].



