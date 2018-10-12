## Technology Paper - DRAFT (NOT READY FOR REVIEW)

gregors comments are here:
* <https://github.com/cloudmesh-community/fa18-523-60/blob/aaff63d6d0a53d808049ed193ba87420abfc8207/paper/paper.md>

### Work Breakdown 
1. Kaggle.com Public API - Izolda Fetko fa18-523-60 - Moved to Project report under "dataset description"
2. MongoDB - Nishad Tupe fa18-523-64
3. PyMongo - Izolda Fetko fa18-523-60

### MongoDB

MongoDB is one of the leading NoSQL databases in the market. In today's 
era, NoSQL databases have developed an enormous potential to 
process the unstructured data efficiently. Modern information is 
complex, extensive, and may not have pre-existing relationships. With 
the advent of the advanced search engines, machine learning, and 
Artificial Intelligence, technology expectations to process, store, and 
analyze such data have grown tremendously [@www-upwork]. The NoSQL 
database engines such as MongoDB, Redis, and Cassandra have successfully 
overcome the traditional relational database challenges such as 
scalability, performance, unstructured data growth, agile sprint cycles, 
and growing needs of processing data in real-time with minimal hardware 
processing power [@www-guru99]. The NoSQL databases are a new generation 
of engines that do not necessarily require SQL language and are sometimes 
also called "Not Only SQL" databases.However, most of them support 
various third-party open connectivity drivers that can map NoSQL queries 
to SQL's. It would be safe to say that although NoSQL databases are 
still far from replacing the relational databases, they are adding an 
immense value when used in hybrid IT environments in conjunction with 
relational databases, based on the application specific needs 
[@www-guru99]. Today, this type of database is fully capable of handling 
dynamic changes; processing large volumes of structured and unstructured data; 
easily using object-oriented programming features; as well as distributed systems 
challenges [@www-mongodb]. At its core, MongoDB is an open source, 
cross-platform, document database mainly written in C++ language. Each 
database within Mongo environment contains collections which in turn 
contain documents. Collections and documents are analogous to tables and 
rows respectively to the relational databases. The document structure is 
in a key-value form which allows storing of complex data types composed 
out of field and value pairs. Documents are objects which correspond to 
native data types in many programming languages, hence a well defined, 
embedded document can help reduce expensive joins and improve query 
performance. Every document is uniquely identified by an *"_id"* field 
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
relational databases can be a very tedious process [@www-upwork]. 
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
action is referred to as *normalization*. MongoDB is a documented database 
and mainly contains denormalized data which means the data is repeated 
instead of indexed over a specific key. If the same data is required in 
more than one table, it needs to be repeated. This constraint has been 
eliminated in MongoDB's new version 3.2. The new release introduced a 
*"$lookup"* feature which more likely works as a left-outer-join. Lookups 
are restricted to aggregated functions which means that data usually 
need some type of filtering and grouping operations to be conducted 
beforehand. For this reason, joins in MongoDB require more complicated 
querying compared to the traditional relational database joins. Although 
at this time, *lookups* are still very far from replacing *joins*, this 
is a prominent feature that can resolve some of the relational data 
challenges for MongoDB [@www-sitepoint]. When it comes to the technical 
elements of MongoDB, it posses a rich interface for importing and 
storage of external data in various formats. Using Mongo Import/Export 
tool one can easily transfer the contents from JSON, CSV, or TSV files 
into a database. MongoDB supports CRUD(Create, read, update, delete) 
operations efficiently and has detailed documentation available on the 
product website. It can also query the geospatial data, and it is capable of 
storing geospatial data in GeoJSON objects. Aggregation Operation of 
MongoDB process data records and returns computed results. MongoDB 
aggregation framework is modeled on the concept of data pipelines. Data 
security is the crucial aspect of enterprise infrastructure management 
and that is why MongoDB provides various security features such as 
authentication, access control, and encryption. It supports mechanisms 
such as SCRAM, LDAP, and Kerberos authentication. The administrator 
can create role-based access control; roles can be predefined or custom. 
MongoDB can audit activities such as DDL, CRUD statements, authentication 
and authorization operations [@www-mongodbmanual]. In regards to the cloud 
technologies, MongoDB also offers fully automated cloud service called *Atlas*
with competitive pricing options. Mongo Atlas Cloud interface offers 
interactive GUI for managing cloud resources and deploying applications quickly. 
The service is equipped with geographically distributed instances to ensure no 
single point failure. Also, a well-rounded performance monitoring interface 
allows users to promptly detect anomalies and generate index suggestions to 
optimize the performance and reliability of the database. Global technology 
leaders such as Google, Facebook, eBay, and Nokia are leveraging MongoDB and 
Atlas cloud services making MongoDB one of the most popular choices among the 
NoSQL databases [@www-mongomanual]. 

### PyMongo

PyMongo is the official Python driver or distribution that allows work with 
a NoSQL type database called *MongoDB* [@api-mongodb-com-api]. The first version 
of the driver was developed in 2009 [@www-pymongo-blog], only two years after the 
MongoDB development was started. This driver allows developers to combine both 
Python's versatility and MongoDB's unstructured data nature into successful 
applications. Currently, this driver supports MongoDB versions 2.6, 3.0, 3.2, 
3.4, 3.6, and 4.0 [@github]. MongoDB and Python represent a compatible fit 
considering that BSON (binary JSON) used in this NoSQL database is very similar 
to Python dictionaries, which makes the collaboration between the two even 
more appealing [@www-slideshare]. For this reason, ditionaries are the recommended 
tools to be used in PyMongo when representing documents [@www-gearheart]. 

#### Installation

Prior to be able to exploit the benefits of Python and MongoDB symultaneously,
the PyMongo distribution must be installed using *pip*. To install it on
all platforms, the following command should be used [@api-mongodb-com-installation]:

`$ python -m pip install pymongo`

Specific versions of PyMongo can be installed with command lines such as 
in our example where the 3.5.1 version is installed [@api-mongodb-com-installation]:

`$ python -m pip install pymongo==3.5.1`

A single line of code can be used to upgrade the driver as 
well [@api-mongodb-com-installation].

`$ python -m pip install --upgrade pymongo`

Furthermore, the installation process can be completed with help of the 
easy_install tool, which requires users to use the following command 
[@api-mongodb-com-installation].

`$ python -m easy_install pymongo`

To do an upgrade of the driver using this tool, the following command is
recommended [@api-mongodb-com-installation]:

`$ python -m easy_install -U pymongo`

There are many other ways of installing PyMongo directly from the source, 
however, they require for C extension dependencies to be installed prior to
the driver installation step, as they are the ones that skim throught the 
sources on GitHub and use the most up-to-date links to install the driver 
[@api-mongodb-com-installation].

To check if the installation was completed accurately, the following command is 
used in the Python console [@www-realpython].

`import pymongo`

If the command returns zero exceptions within the Python shell, one can consider 
for the PyMongo installation to have been completed successfully.

#### Dependencies

The PyMongo driver has a few dependencies that should be taken into consideration.
Currently, it supports CPython 2.7, 3.4+, PyPy, and PyPy 3.5+ interpreters 
[@www-github-driver]. An optional dependency that requires some additional 
components to be installed is the GSSAPI authentication [@www-github-driver]. For 
the Unix based machines, it requires pykerberos, while for the Windows machines 
WinKerberos is needed to fullfill this requirement [@www-github-driver]. The 
automatic installation of this dependency can be done symoultaneously with the
driver installation, in the following manner:

`$ python -m pip install pymongo[gssapi]`

Other third-party dependencies such as *ipaddress*, *certifi*, or *wincerstore*
are necessary for connections with help of TLS/SSL and can also be symoultaneously
installed along with the driver installation [@www-github-driver].

#### Running PyMongo with Mongo Deamon

Once PyMongo is installed, the Mongo deamon can be run with a very simple command
in a new terminal window [@www-realpython].

`$ mongod`

#### Connecting to a database using MongoClient

In order to be able to establish a connection with the database, a MongoClient
class needs to be imported, which subsequentially allows the MongoClient object to 
communicate with the database [@www-realpython]. 

`from pymongo import MongoClient`
`client = MongoClient()`

This command allows a connection with a default, local host and port (27017),
however, depending on the programming requirements, one can also specify those
by listing them in the client instance or use the same information via the Mongo 
URI format [@www-realpython].

#### Accessing Databases, Inserting and Retrieving Documents

Since MongoClient plays a server role, it can be used to access any desired 
databases in an easy way. To do that, one can use two different approaches.
The first approach would be doing this via attribute method where the name of
the desired database is listed as an attribute, and the second approach, which
would include a dictionary-style access [@www-realpython]. For example, to 
access a database called *cloudmesh_community*, one would use the following 
commands for the attribute and for the dictionary method, respectfully.

`db = client.cloudmesh_community`
`db = client['cloudmesh_community']`

Creating documents and storing data using PyMongo is equally easy as 
accessing databases. In order to add new data, a collection must be 
specified first. In this example, we are making a decision to use the
*cloudmesh* group of documents.

`cloudmesh = db.cloudmesh`

Once this step is completed, data may be inserted using the insert_one()
method, which means that only one document is being inserted. Of course,
insertion of multiple documents at the same time is possible also with use
of the insert_many() method [@www-realpython]. An example of this method is
as follows: 

`course_info = {
    'course': 'Big Data Applications and Analytics',
    'instructor': ' Gregor von Laszewski',
    'chapter': 'technologies'
}`

`result = cloudmesh.insert_one(course_info)`

Retrieving documents is equally simple as it requires the use of a 
find_one() method [@www-realpython]. An implementation of this method 
is given in the following example.

`gregors_course = cloudmesh.find_one({'instructor':'Gregor von Laszewski'})`

Similarly, to retieve multiple documents, one would use the find() method 
instead. For example, to find all courses thought by professor Laszewski,
we would use the following command.

`gregors_course = cloudmesh.find({'instructor':'Gregor von Laszewski'})`

One thing that users should be cognizant of when using the find() method 
is that it does not return the results in an array format but as a 
*cursor* object, which is a combination of methods that work together to 
help with data querying [@www-realpython]. In order to return individual 
documents iteration over the result must be completed [@www-realpython].

#### Pros and Cons using PyMongo

