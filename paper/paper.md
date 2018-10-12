## Technology Paper - DRAFT (NOT READY FOR REVIEW)

gregors comments are her:
* <https://github.com/cloudmesh-community/fa18-523-60/blob/aaff63d6d0a53d808049ed193ba87420abfc8207/paper/paper.md>

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
different approaches and ideas through the forums and Kaggle Kernels”
[@www-kaggle-blog]
which resulted in forming of the well-known platform we see today. 
According to the Kaggle documentation, the platform supports various 
types of datasets, such as CSV, Excel (although recommended to be 
uploaded as CSV), JSON, SQLite, BigQuery, and other [@www-kaggle-datasets].
Other file formats constitute PNG imagery files, NPZ specialty file formats
, as well as complex hierarchical data formats like HDF5 [@www-kaggle-datasets]. 
Kaggle also supports archives, in other words, “files compressed using 
the ZIP file format as well as other common archive formats like 7z” 
[@www-kaggle-datasets]. 
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


### MongoDB

In today's era, NoSQL databases have developed an enormous potential to 
process the unstructured data efficiently. Modern information is 
complex, extensive, and may not have pre-existing relationships. With 
the advent of the advanced search engines, machine learning, and 
Artificial Intelligence, technology expectations to process, store, and 
analyze such data has grown tremendously [@www-upwork]. Today, NoSQL 
database engines such as MongoDB, Redis, and Cassandra have successfully 
overcome the traditional relational database challenges such as 
scalability, performance, unstructured data growth, agile sprint cycles, 
and growing needs of processing data in real-time with minimal hardware 
processing power [@www-guru99]. The NoSQL databases are a new generation 
of engines that don't necessarily require SQL language and are sometimes 
also called "Not Only SQL" databases. However, most of them support 
various third-party open connectivity drivers that can map NoSQL queries 
to SQL's. It would be safe to say that although NoSQL databases are 
still far from replacing the relational databases, they are adding an 
immense value when used in hybrid IT environments in conjunction with 
relational databases, based on the application specific needs 
[@www-guru99]. Today, MongoDB is one of the leading NoSQL databases in 
the market. It is fully capable of handling dynamic changes; processing 
large volumes of structured and unstructured data; easily using 
object-oriented programming features; as well as distributed systems 
challenges[@www-mongodb]. At its core, MongoDB is an open source, 
cross-platform, document database mainly written in C++ language. Each 
database within Mongo environment contains collections which in turn 
contain documents. Collections and documents are analogous to tables and 
rows respectively to the relational databases. The document structure is 
in a key-value form which allows storing of complex data types composed 
out of field and value pairs. Documents are objects which correspond to 
native data types in many programming languages, hence a well defined, 
embedded document can help reduce expensive joins and improve query 
performance. Every document is uniquely identified by a "_id" field 
[@www-guru99]. MongoDB offers flexibility to write records that are 
not restricted by column types. The data storage approach is flexible as 
it allows one to store data as it grows and to fulfill varying needs of 
applications and/or users. It supports JSON like binary points known as 
BSON where data can be stored without specifying the type of data 
[@www-upwork]. Moreover, it can be distributed on multiple machines at a 
high speed; it includes a sharidng feature that partitions and spreads 
the data out across various servers. This makes MongoDB an excellent 
choice for cloud data processing. Its utilities can load high volumes of 
data at high speed which ultimately provides a greater flexibility and 
availability in a cloud-based environment [@www-upwork]. The dynamic 
schema structure within MongoDB allows easy testing of the small sprints 
in agile project management life cycles and research projects that 
require frequent changes to the data structure with minimal downtime. 
Contrary to this flexible process, modifying the data structure of 
relational databases can be a very tedious process[@www-upwork]. 
Similarly to the relational databases, the query performance can be 
improved by using indexing. MongoDB queries support regular expressions 
as well as range asks for specific fields that eliminate the need of 
returning entire documents [@www-guru99]. MongoDB collections do not 
enforce document structure like SQL databases which is a compelling 
feature. However, it is essential to keep in mind the needs of the 
applications. The data retrieval patterns, the frequency of data 
manipulation statements such as insert, updates, and deletes may embark 
the use of indexes or incorporating the sharding feature to improve 
query performance and efficiency of MongoDB environment [@www-guru99]. 
One of the significant difference between relational databases and NoSQL 
databases are joins. In the relational database, one can combine results 
from two or more tables using a common column, often called as key. The 
native table contains the primary key column while the referenced table 
contains a foreign key. This mechanism allows one to make changes in a 
single row instead of changing all rows in the referenced table, this 
action is referred to as normalization. MongoDB is a documented database 
and mainly contains denormalized data which means the data is repeated 
instead of indexed over a specific key. If the same data is required in 
more than one table, it needs to be repeated. This constraint has been 
eliminated in MongoDB's new version 3.2. The new release introduced a 
"$lookup" feature which more likely works as a left-outer-join. Lookups 
are restricted to aggregated functions which means that data usually 
need some type of filtering and grouping operations to be conducted 
beforehand. For this reason, joins in MongoDB require more complicated 
querying compared to the traditional relational database joins. Although 
at this time, "lookups" are still very far from replacing "joins", this 
is a prominent feature that can resolve some of the relational data 
challenges for MongoDB [@www-sitepoint]. When it comes to the technical 
elements of MongoDB, it posses a rich interface for importing and 
storage of external data in various formats. Using Mongo Import/Export 
tool one can easily transfer the contents from a JSON, CSV, or TSV files 
into a database. MongoDB supports CRUD(Create, read, update, delete) 
operations efficiently and has detailed documentation available on the 
website. It can also query the geospatial data, and it is capable of 
storing geospatial data in GeoJSON objects. Aggregation Operation of 
MongoDB process data records and returns computed results. MongoDB 
aggregation framework is modeled on the concept of data pipelines. Data 
security is the crucial aspect of enterprise infrastructure management 
and that is why MongoDB provides various security features such as 
authentication, access control, and encryption. It supports mechanisms 
such as SCRAM and LDAP and Kerberos authentication. The administrator 
can create role-based access control; roles can be predefined or custom. 
MongoDB can audit activities such as DDL, CRUD statements, 
authentication and authorization operations [@www-mongodbmanual]. In 
regards to the cloud technologies, MongoDB also offers fully automated 
cloud service called "Atlas" with competitive pricing options. Mongo 
Atlas Cloud interface offers interactive GUI for managing cloud 
resources and deploying applications quickly. The service is equipped 
with geographically distributed instances to ensure no single point 
failure. Also, a well-rounded performance monitoring interface allows 
users to promptly detect anomalies and generate index suggestions to 
optimize the performance and reliability of the database. Global 
technology leaders such as Google, Facebook, eBay, and Nokia are 
leveraging MongoDB and Atlas cloud services making MongoDB one of the 
most popular choices among the NoSQL databases [@www-mongomanual]. 






### PyMongo

The MongoDB is an open source database which stores information as flexible
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
pooling for threaded applications [@api.mongodb.com-FAQ]. The PyMongo also 
support asynchronous frameworks like Gevent, asyncio, Tornado, or Twisted. 
It works with mod_wsgi also [@api.mongodb.com-FAQ].

For representing dates and times in MongoDB documents, the PyMongo uses 
datetime objects [@api-mongodb-com-api]. Because MongoDB assumes that dates 
and times are in UTC, care should be taken to ensure that dates and 
times written to the database reflect UTC [@api-mongodb-datetimes].

Atlas is MongoDB, Inc.’s hosted MongoDB as a service offering. 
The Pymango can use to connect Atlas from python code. Connections 
to Atlas is secure connection and need TLS/SSL. For connections using TLS/SSL,
PyMongo may require third party dependencies as determined by the version of 
Python. With Python 3.3+, can install PyMongo and any TLS/SSL-related 
dependencies using the pip tls command [@api.mongodb.com-atlas].

Create a MongoClient to the running mongod instance is the first step when 
working with PyMongo. A single instance of MongoDB can support multiple 
independent databases. When working with PyMongo you access databases using 
attribute style access on MongoClient instances. In PyMongo we use dictionaries
to represent documents [@api-mongodb-com-tutorial].


The Pymango can install or upgrade with pip command. The pip is the recommended
way to install Pymongo on all platforms. We can get the specific Pymongo 
version using pip commands [@api-mongodb-com-installation]. we can use 
easy_install from setuptools location (https://pypi.org/project/setuptools/)
for installation and upgrade. There is another way to install Pymongo directly 
from source. It first install the C extension dependencies then check the 
latest GitHub sourceand install the driver from the resulting 
tree [@api-mongodb-com-installation].


The Pymango can install or upgrade with pip command. The pip is the recommended
way to install Pymongo on all platforms. We can get the specific Pymongo 
version using pip commands [@api-mongodb-com-installation]. we can use 
easy_install from setuptools location (https://pypi.org/project/setuptools/)
for installation and upgrade. There is another way to install Pymango directly 
from source (i.e. to stay on the bleeding edge. The install the C extension 
dependencies then check out the latest source from  GitHub and install the 
driver from the resulting tree [@api-mongodb-com-installation].

The Pymango has some dependencies as it supports only CPython 2.6, 2.7, 3.4+, 
PyPy, and PyPy3. The GSSAPI authentication requires pykerberos on Unix
 or WinKerberos on Windows for installation.

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
 which will be automatically converted to and from the appropriate BSON types 
 [@api-mongodb-com-tutorial]. The PyMongo use dictionaries to  represent
 documents data. When a document is inserted by Pymogo in mongodb, 
 which will be automatically converted to and from the appropriate BSON types.
 The PyMongo use dictionaries to  represent documents data 
 [@api-mongodb-com-tutorial]. When a document is inserted by Pymago in mongodb, 
 the special key as "_id" automatically added in database

There are many tools written for working with PyMongo. These tools give 
additional flavor to PyMongo. Below is the list for some of the tools.

**PyMODM** is an ORM-like framework on top of PyMongo. The PyMODM 
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
Use the Django Admin GUI to add and modify documents in MongoDB 
[@api-mongodb-tools]. 


**Django MongoDB Engine** is a MongoDB database backend for Django that 
completely integrates with its ORM [@api-mongodb-tools].

**mongodb_beaker** is a project to enable using MongoDB as a backend for 
beaker’s caching / session system [@api-mongodb-tools].

**Log4Mongo** is a flexible Python logging handler that can store logs in 
MongoDB using normal and capped collections [@api-mongodb-tools].

**MongoLog** is a Python logging handler that stores logs in MongoDB using a 
capped collection [@api-mongodb-tools].

**c5t** is a content-management system using TurboGears and MongoDB 
[@api-mongodb-tools].

**rod.recipe.mongodb** is a ZC Buildout recipe for downloading and
 installing MongoDB [@api-mongodb-tools].

**repoze-what-plugins-mongodb** is a project working to support a plugin for
 using MongoDB as a backend for repoze.what [@api-mongodb-tools].

**mongobox** is a tool to run a sandboxed [@api-mongodb-tools] 
MongoDB instance from within a python app [@api-mongodb-tools].

**Flask-MongoAlchemy** add Flask support for MongoDB using MongoAlchemy 
[@api-mongodb-tools].

**Flask-MongoKit** is the Flask extension to better integrate
MongoKit into Flask [@api-mongodb-tools].

**Flask-PyMongo** is the bridges Flask and PyMongo [@api-mongodb-tools].


