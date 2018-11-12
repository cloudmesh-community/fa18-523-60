# MongoDB in Python :hand: fa18-523-60, fa18-523-64, fa18-523-72

| Izolda Fetko, Nishad Tupe, Vishal Bhoyar
| ifetko@iu.edu, ntupe@iu.edu, vbhoyar@iu.edu
| Indiana University
| hid: fa18-523-60, fa18-523-64, fa18-523-72
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-523-60/blob/master/paper/paper.md)

* :o: we already pointed out that first section is too long - broke it down to multiple segments
* :o: proposed title change: MongoDB in Python - changed 
* :o: introduction and learning outcome missing - added introduction and learning outcomes
* :o: wrong quotes - fixed quotes
* :o: do not use quotes for non cited text such as in  "_id" that is `_id` - fixed
* :o: use bash and python after the 3 quotes, bash has a $ at the beginning - fixed

## Introduction

In today's era, NoSQL databases have developed an enormous potential to 
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
also called *Not Only SQL* databases. However, most of them support 
various third-party open connectivity drivers that can map NoSQL queries 
to SQL's. It would be safe to say that although NoSQL databases are 
still far from replacing the relational databases, they are adding an 
immense value when used in hybrid IT environments in conjunction with 
relational databases, based on the application specific needs 
[@www-guru99]. In this paper, we will be covering the MongoDB technology, 
its driver PyMongo,  its object-document mapper MongoEngine, and 
a micro-web framework Flask-Mongo that make MongoDB more attractive
and user-friendly.

## Learning Outcome

The learning outcome of this paper is to equip readers with the basic 
MongoDB knowledge, as well as on how to use PyMongo driver in
conjunction with this NoSQL database. Other than the instructions on
how to use this driver, the reader will be introduced to some 
basic functionalities of the MongoEngine, an Object-Document mapper,
and Flask-Mongo, a micro web framework.  

## MongoDB

MongoDB is one of the leading NoSQL databases in the market. Today, 
this type of database is fully capable of handling dynamic changes; 
processing large volumes of structured and unstructured data; 
easily using object-oriented programming features; as well as distributed
system challenges [@www-mongodb]. At its core, MongoDB is an open source, 
cross-platform, document database mainly written in C++ language. 

## Collections and Documents

Each database within Mongo environment contains collections which in turn 
contain documents. Collections and documents are analogous to tables and 
rows respectively to the relational databases. The document structure is 
in a key-value form which allows storing of complex data types composed 
out of field and value pairs. Documents are objects which correspond to 
native data types in many programming languages, hence a well defined, 
embedded document can help reduce expensive joins and improve query 
performance. Every document is uniquely identified by an *_id* field 
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
applications. 

## MongoDB Querying

The data retrieval patterns, the frequency of data manipulation 
statements such as insert, updates, and deletes may embark 
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
*$lookup* feature which more likely works as a left-outer-join. Lookups 
are restricted to aggregated functions which means that data usually 
need some type of filtering and grouping operations to be conducted 
beforehand. For this reason, joins in MongoDB require more complicated 
querying compared to the traditional relational database joins. Although 
at this time, *lookups* are still very far from replacing *joins*, this 
is a prominent feature that can resolve some of the relational data 
challenges for MongoDB [@www-sitepoint]. 

## MongoDB Basic Functions

When it comes to the technical elements of MongoDB, it posses a 
rich interface for importing and storage of external data in various 
formats. Using Mongo Import/Export tool one can easily transfer the 
contents from JSON, CSV, or TSV files into a database. MongoDB 
supports CRUD(Create, read, update, delete) operations efficiently 
and has detailed documentation available on the product website. 
It can also query the geospatial data, and it is capable of 
storing geospatial data in GeoJSON objects. Aggregation Operation of 
MongoDB process data records and returns computed results. MongoDB 
aggregation framework is modeled on the concept of data pipelines. 

## Security Features

Data security is the crucial aspect of enterprise infrastructure management 
and that is why MongoDB provides various security features such as 
authentication, access control, and encryption. It supports mechanisms 
such as SCRAM, LDAP, and Kerberos authentication. The administrator 
can create role-based access control; roles can be predefined or custom. 
MongoDB can audit activities such as DDL, CRUD statements, authentication 
and authorization operations [@www-mongodbmanual]. 

## MongoDB Cloud Service

In regards to the cloud technologies, MongoDB also offers fully automated 
cloud service called *Atlas* with competitive pricing options. Mongo Atlas 
Cloud interface offers interactive GUI for managing cloud resources and 
deploying applications quickly. The service is equipped with geographically 
distributed instances to ensure no single point failure. Also, a well-rounded 
performance monitoring interface allows users to promptly detect anomalies and 
generate index suggestions to optimize the performance and reliability of the 
database. Global technology leaders such as Google, Facebook, eBay, and Nokia 
are leveraging MongoDB and Atlas cloud services making MongoDB one of the most 
popular choices among the NoSQL databases [@www-mongomanual]. 

## PyMongo

PyMongo is the official Python driver or distribution that allows work 
with a NoSQL type database called *MongoDB* [@api-mongodb-com-api]. The 
first version of the driver was developed in 2009 [@www-pymongo-blog], 
only two years after the MongoDB development was started. This driver 
allows developers to combine both Python's versatility and MongoDB's 
flexible schema nature into successful applications. Currently, this 
driver supports MongoDB versions 2.6, 3.0, 3.2, 3.4, 3.6, and 4.0 
[@github]. MongoDB and Python represent a compatible fit considering 
that BSON (binary JSON) used in this NoSQL database is very similar 
to Python dictionaries, which makes the collaboration between the two 
even more appealing [@www-slideshare]. For this reason, dictionaries 
are the recommended tools to be used in PyMongo when representing 
documents [@www-gearheart]. 

### Installation

Prior to being able to exploit the benefits of Python and MongoDB 
simultaneously, the PyMongo distribution must be installed using 
*pip*. To install it on all platforms, the following command should 
be used [@api-mongodb-com-installation]:

`$ python -m pip install pymongo`

Specific versions of PyMongo can be installed with command lines 
such as in our example where the 3.5.1 version is installed 
[@api-mongodb-com-installation].

`$ python -m pip install pymongo==3.5.1`

A single line of code can be used to upgrade the driver as well 
[@api-mongodb-com-installation].

`$ python -m pip install --upgrade pymongo`

Furthermore, the installation process can be completed with help 
of the *easy_install* tool, which requires users to use the 
following command [@api-mongodb-com-installation].

`$ python -m easy_install pymongo`

To do an upgrade of the driver using this tool, the following 
command is recommended [@api-mongodb-com-installation]:

`$ python -m easy_install -U pymongo`

There are many other ways of installing PyMongo directly from 
the source, however, they require for C extension dependencies 
to be installed prior to the driver installation step, as they 
are the ones that skim through the sources on GitHub and use 
the most up-to-date links to install the driver 
[@api-mongodb-com-installation].

To check if the installation was completed accurately, the 
following command is used in the Python console 
[@www-realpython].

`$ import pymongo`

If the command returns zero exceptions within the Python 
shell (or any other (IDE), one can consider for the PyMongo 
installation to have been completed successfully.

### Dependencies

The PyMongo driver has a few dependencies that should 
be taken into consideration. Currently, it supports 
CPython 2.7, 3.4+, PyPy, and PyPy 3.5+ interpreters 
[@www-github-driver]. An optional dependency that 
requires some additional components to be installed 
is the GSSAPI authentication [@www-github-driver]. For 
the Unix based machines, it requires *pykerberos*, while 
for the Windows machines *WinKerberos* is needed to fullfill 
this requirement [@www-github-driver]. The automatic installation 
of this dependency can be done simultaneously with the driver 
installation, in the following manner:

`$ python -m pip install pymongo[gssapi]`

Other third-party dependencies such as *ipaddress*, *certifi*, 
or *wincerstore* are necessary for connections with help of 
TLS/SSL and can also be simultaneously installed along with the 
driver installation [@www-github-driver].

### Running PyMongo with Mongo Deamon

Once PyMongo is installed, the Mongo deamon can be run with a 
very simple command in a new terminal window [@www-realpython].

`$ mongod`

### Connecting to a database using MongoClient

In order to be able to establish a connection with a database, 
a MongoClient class needs to be imported, which sub-sequentially 
allows the MongoClient object to communicate with the database 
[@www-realpython]. 

`$ from pymongo import MongoClient`
`$ client = MongoClient()`

This command allows a connection with a default, local host through 
port 27017, however, depending on the programming requirements,
one can also specify those by listing them in the client instance 
or use the same information via the Mongo URI format [@www-realpython].

### Accessing Databases

Since MongoClient plays a server role, it can be used to access 
any desired databases in an easy way. To do that, one can use two 
different approaches. The first approach would be doing this via 
the *attribute* method where the name of the desired database is 
listed as an attribute, and the second approach, which would include a 
dictionary-style access [@www-realpython]. For example, to access a 
database called *cloudmesh_community*, one would use following 
commands for the attribute and for the dictionary method, 
respectively.

`$ db = client.cloudmesh_community`

`$ db = client['cloudmesh_community']`

### Creating a Database

Creating a database is a straight forward process. First,one needs to
create the MongoClient object and specify the connection (IP address)
as well as the name of the database they are trying to create 
[@www-w3schools]. The example of this command is presented in the
followng section:
```
$ import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db = client['cloudmesh']

```
### Inserting and Retrieving Documents (Querying)

Creating documents and storing data using PyMongo is equally easy as 
accessing and creating databases. In order to add new data, a 
collection must be specified first. In this example, a decision is 
made to use the *cloudmesh* group of documents.

`$ cloudmesh = db.cloudmesh`

Once this step is completed, data may be inserted using the 
*insert_one()* method, which means that only one document is 
being created. Of course, insertion of multiple documents at 
the same time is possible as well with use of the *insert_many()*
method [@www-realpython]. An example of this method is as follows: 
```
$ course_info = {
     'course': 'Big Data Applications and Analytics',
     'instructor': ' Gregor von Laszewski',
     'chapter': 'technologies'
}
```
`$ result = cloudmesh.insert_one(course_info)`

Another example of this method would be to create a collection.
If we wanted to create a collection of students in the 
*cloudmesh_community*, we would do it in the following manner:
```
$ student = [ {'name': 'John', 'st_id': 52642},
    {'name': 'Mercedes', 'st_id': 5717},
    {'name': 'Anna', 'st_id': 5654},
    {'name': 'Greg', 'st_id': 5423},
    {'name': 'Amaya', 'st_id': 3540},
    {'name': 'Cameron', 'st_id': 2343},
    {'name': 'Bozer', 'st_id': 4143},
    {'name': 'Cody', 'price': 2165} ]

client = MongoClient('mongodb://localhost:27017/')

with client:

    db = client.cloudmesh
    
    db.students.insert_many(student)
```
Retrieving documents is equally simple as creating them. A 
*find_one()* method can be used to retrieve one document 
[@www-realpython]. An implementation of this method is given 
in the following example.

`$ gregors_course = cloudmesh.find_one({'instructor':'Gregor von Laszewski'})`

Similarly, to retieve multiple documents, one would use the 
*find()* method instead of the *find_one()*. For example, to 
find all courses thought by professor von Laszewski, one would 
use the following command:

`$ gregors_course = cloudmesh.find({'instructor':'Gregor von Laszewski'})`

One thing that users should be cognizant of when using the *find()*
method is that it does not return results in an array format but 
as a *cursor* object, which is a combination of methods that work 
together to help with data querying [@www-realpython]. In order to 
return individual documents, iteration over the result must be 
completed [@www-realpython].

### Limiting Results

When it comes to working with large databases it is always useful to
limit the number of query results. PyMongo supports this option 
with its *limit()* method [@www-w3schools]. This method takes in one
parameter which specifies the number of documents to be returned
[@www-w3schools]. For example, if we had a collection with a large 
number of cloud technologies as individual documents, one could 
modify the query results to return only the top 10 technologies. 
To do this, the following example could be utilized:
```
$ client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['cloudmesh']
    col = db['technologies']
    topten = col.find().limit(10)
```
### Updating Collection

Updating documents is very similar to inserting and retrieving 
the same. Depending on the number of documents to be updated,
one would use the *update_one()* or *update_many()* method
[@www-w3schools]. Two parameters need to be passed 
in the *update_one()* method for it to successfully execute. 
The first argument is the query object that specifies the 
document to be changed, and the second argument is the object 
that specifies the new value in the document. An example of 
the *update_one()* method in action is the following:
```
$ myquery = { 'course': 'Big Data Applications and Analytics' }
   newvalues = { '$set': { 'course': 'Cloud Computing' } }
```
Updating all documents that fall under the same criteria can be
done with the *update_many* method [@www-w3schools].
For example, to update all documents in which course title starts
with letter *B* with a different instructor information, we would 
do the following:
```
$  client = pymongo.MongoClient('mongodb://localhost:27017/')
   db = client['cloudmesh']
   col = db['courses']
   query = { 'course': { '$regex': '^B' } }
   newvalues = { '$set': { 'instructor': 'Gregor von Laszewski' } }
   
   edited = col.update_many(query, newvalues)
```
### Counting Documents

Counting documents can be done with one simple operation called
*count_documents()* instead of using a full query 
[@www-pymongo-tutorial]. For example, we can count the documents 
in the *cloudmesh_commpunity* by using the following command:

`$ cloudmesh = count_documents({})`

To create a more specific count, one would use a command similar 
to this:

`$ cloudmesh = count_documents({'author': 'von Laszewski'})`

This technology supports some more advanced querying options as well. 
Those advanced queries allow us to add certain contraints and narrow 
down the results even more. For example, to get the courses thought
by professor von Laszewski after a certain date, we would use the 
following command:
```
$ d = datetime.datetime(2017, 11, 12, 12)
     for course in cloudmesh.find({'date': {'$lt': d}}).sort('author'):
     pprint.pprint(course)
```
### Indexing

Indexing is a very important part of querying. It can greately improve
query performance but also add functionality and aide in storing 
documents [@www-pymongo-tutorial]. 

> "To create a unique index on a key that rejects documents whose value 
> for that key already exists in the index" [@www-pymongo-tutorial], 

we need to firstly create the index in the following manner:
```
$ result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],
  unique=True)

  sorted(list(db.profiles.index_information()))
```
This command acutally creates two different indexes. The first one is
*_id* , created by MongoDB automatically, and the second one is 
*user_id*, created by the user (us in this case).

The purpose of those indexes is to cleverly prevent future additions of 
invalid user_ids into a collection.

### Sorting

Sorting on the server-side is also avaialable via MongoDB. The PyMongo
*sort()* method is equivalent to the SQL *order by*  statement and it
can be performed as *pymongo.ascending* and *pymongo.descending* 
[@book-ohiggins]. This method is much more efficient as it is being 
completed on the server-side, compared to the sorting completed on 
the client side. For example, to return all users with first name 
*Gregor* sorted in descending order by birthdate we would use 
a command such as this:
```
$ users = cloudmesh.users.find(
   {'firstname':'Gregor'}).sort(('dateofbirth', pymongo.DESCENDING))
 for user in users:
   print user.get('email')
```
### Aggregation

PyMongo in its documentation offers a separate framework that supports
data aggregation. This aggregation framework can be used to 

> "provide projection capabilities to reshape the returned data"
> [@www-mongo-aggregation].

Another option here would be to use the Map/Reduce framework,
which essentially includes two different functions, *map*  and 
*reduce*. The first one provides the key value pair for each
tag in the array, while the latter one

> "sums over all of the emitted values for a given key"
> [@www-mongo-aggregation].

The last step in this specific process it to call the 
*map_reduce()*  function and iterate over the results.
[@www-mongo-aggregation].

### Deleting Documents from a Collection

The deletion of documents with PyMongo is fairly straight forward. 
To do so, one would use the *remove()*  method of the PyMongo 
Collection object [@book-ohiggins]. Similarly to the reads and
updates, specification of documents to be removed is a must. For 
example, removal of the entire document collection with a score
of 1, one would use the following command:

`$ cloudmesh.users.remove({"score":1, safe=True})`

The *safe* parameter set to *True* ensures the operation was 
completed [@book-ohiggins]. 

### Copying a Database

Copying databases within the same mongod instance or between
different mongod servers is made possible with the *command()*
method after connecting to the desired mongod instance 
[@www-pymongo-documentation]. For example, to copy the *cloudmesh*
database and name the new database *cloudmesh_copy*, one would
use the *command()* method in the following manner:

```
$ client.admin.command('copydb',
                         fromdb='cloudmesh',
                         todb='cloudmesh_copy')
```
There are two way to copy a database between servers. If a
server is not password-prodected, one would not need to 
pass in the credentials nor to authenticate to the admin database
[@www-pymongo-documentation]. In that case, to copy a database one 
would use the following command:
```
$ client.admin.command('copydb',
                         fromdb='cloudmesh',
                         todb='cloudmesh_copy',
                         fromhost='source.example.com')
```
On the other hand, if the server where we are copying the 
database to is protected, one would use this command instead:
```
$ client = MongoClient('target.example.com',
                     username='administrator',
                     password='pwd')
  client.admin.command('copydb',
                     fromdb='cloudmesh',
                     todb='cloudmesh_copy',
                     fromhost='source.example.com')
```                     
### PyMongo Strengths

One of PyMongo strengths is that allows document creation and 
querying natively

> "through the use of existing language features such as nested 
> dictionaries and lists" [@book-ohiggins]. 

For moderately experienced Python developers, it is very easy to 
learn it and quickly feel comfortable with it.

> "For these reasons, MongoDB and Python make a powerful 
> combination for rapid, iterative development of horizontally 
> scalable backend applications" [@book-ohiggins].

According to [@book-ohiggins], MongoDB is very applicable to modern 
applications, which makes PyMongo equally valuable [@book-ohiggins].

## MongoEngine

> "MongoEngine is an Object-Document Mapper, written in Python 
> for working with MongoDB" [@docs-mongoengine]. 

It is actually a library that allows a more advanced communication 
with MongoDB compared to PyMongo. As MongoEngine is technically 
considered to be an object-document mapper(ODM), it can also be 
considered to be 

> "equivalent to a SQL-based object relational mapper(ORM)" 
> [@www-realpython].

The primary technique why one would use an ODM includes 
*data conversion* between computer systems that are not 
compatible with each other[@www-wikiodm]. For the purpose of 
converting data to the appropriate form, a *virtual object 
database* must be created within the utilized programming 
language [@www-wikiodm]. This library is also used to define 
schemata for documents within MongoDB, which ultimately helps
with minimizing coding errors as well defining methods 
on existing fields [@docs-mongoengine- schema]. It is also 
very beneficial to the overall workflow as it tracks changes 
made to the documents and aids in the document saving process 
[docs-mongoengine- instances].

### Installation

The installation process for this technology is fairly simple 
as it is considered to be a library. To install it, one would 
use the following command [@www-installing]:

`$ pip install mongoengine`

A *bleeding-edge* version of MongoEngine can be installed directly 
from GitHub but first cloning the repository on the local machine, 
virtual machine, or cloud.

### Connecting to a database using MongoEngine

Once installed, MongoEngine needs to be connected to an instance of 
the mongod, similarly to PyMongo [@www-connecting]. The *connect()* 
function must be used to successfully complete this step and the argument 
that must be used in this function is the name of the desired database 
[@www-connecting]. Prior to using this function, the function name needs 
to be imported from the MongoEngine library.
```
$ from mongoengine import connect
  connect('cloudmesh_community')
```
Similarly, to the MongoClient, MongoEngine uses the local host and 
port (27017) by default, however, the *connect()* function also allows 
to specify other host and port arguments as well [@www-connecting].

`$ connect('cloudmesh_community', host='196.185.1.62', port=16758)`

Other types of connections are also supported (i.e. URI) and they can 
be completed by providing the URI in the *connect()* function 
[@www-connecting]. 

### Querying using MongoEngine

To query MongoDB using MongoEngine an *objects attribute* is used, 
which is, technically, a part of the document class [@www-querying]. 
This attribute is called the *QuerySetManager* which in return 

>  "creates a new *QuerySet* object on access" [@www-querying].

To be able to access individual documents from a database, this object
needs to be iterated over. For example, to return/print all students 
in the *cloudmesh_community*object (database), the following command 
would be used.
```
$ for user in cloudmesh_community.objects:
     print cloudmesh_community.student
```
MongoEngine also has a capability of query filtering which means that 
a keyword can be used with in the called *QuerySet* object to retrieve 
specific information [@www-querying]. Let's say one would like to 
iterate over cloudmesh_community students that are natives of Indiana. 
To achieve this, one would use the following command:

`$ indy_students = cloudmesh_community.objects(state='IN')`

This library also allows the use of all operators except for the 
equality operator in its queries, and moreover, has the capability 
of handling *string queries*, *geo queries*, *list querying*, 
and querying of the raw PyMongo queries [@www-querying]. 

The string queries are useful in performing text operations in the 
conditional queries. The query to find document exactly matching with
State ACTIVE is give as as below:

`$ db.cloudmesh_community.find( State.exact("ACTIVE") )`

The query to find the document data with Name start with case sensitive AL 
can written as:

`$ db.cloudmesh_community.find( Name.startswith("AL") )`

The case insensitive data start with AL extract with query command as:

`$ db.cloudmesh_community.find( Name.istartswith("AL") )`

The MongoEngine allow to extract data for geographical location using Geo 
queries. The geo_within  operator check if a geometry is within a polygon.

```
$ cloudmesh_community.objects(
            point__geo_within=[[[40, 5], [40, 6], [41, 6], [40, 5]]])
  cloudmesh_community.objects(
            point__geo_within={"type": "Polygon",
                 "coordinates": [[[40, 5], [40, 6], [41, 6], [40, 5]]]})
```
The list query will lookup the documents where the field specified matches 
the given value exactly. To match all pages that have the word 'coding' as an 
item in the 'tags' list can find as below:
```
$ class Page(Document):
     tags = ListField(StringField())

  Page.objects(tags='coding')
```
## Flask-PyMongo
> "Flask is a micro web framework written in Python" 
> [@flask-framework]. 

It is more pythonic, it is developed after Django, and is explicitly 
targeting Python user community. It is lightweight, it 
does not require tools or libraries and hence is classified as a Micro 
Web framework. Flask caters application features such object mappers, 
authentication methods, and form validations by supporting extensions. 
Flask is often used with MongoDB using PyMongo connector, and it treats 
data within MongoDB as searchable Python dictionaries. The applications 
such as Pinterest, LinkedIn, and the community web page for Flask are 
using the Flask framework. It supports various features such as RESTful 
request dispatching, secure cookies, Google app engine compatibility, 
and integrated support for unit testing, etc. [@flask -framework]. Flask 
PyMongo offers methods such as *Collection.find_one_or_404* which is the 
equivalent to MongoDB's *find_one* in which instead of returning None, 
causes a *404 Not Found HTTP status* on a request. Similarly, 
*PyMongo.send_file* and *PyMongo.save_file* methods works on the 
file-like object. The connection details for MongoDB can be passed as a 
variable or configured in PyMongo constructor with additional arguments 
such as username and password if required. One can create multiple Flask 
PyMongo instances to connect to multiple MongoDB databases. It is 
important that versions of both Flask and MongoDB are compatible with 
each other avoid functionality breaks [@flask-pymongo]. 
Flask-MongoAlchemy and Flask-MongoEngine are the additional libraries 
that can be used to connect to a MongoDB database while using enhanced 
features with the Flask app. It can be easily installed using pip. The 
Flask-MongoAlchemy is used as a proxy between Python and MongoDB to 
connect. Flask-MongoAlchemy provides an option such as server or 
database based authentication to connect to MongoDB. While the default 
is set server based, to use database-based authentication, the config 
value MONGOALCHEMY_SERVER_AUTH parameter must be set to False 
[@pythonhosted-MongoAlchemy]. Flask-MongoEngine is the Flask extension 
that provides integration with MongoEngine. It handles connection 
management for the apps. It can be installed through pip and set up very 
easily as well. The default configuration is set to local host and port 
27017, for the custom port and if MongoDB is running on another server 
the host and port must be explicitly specified in connect strings 
specified within the *MONGODB_SETTINGS* dictionary with 
*app.config* along with database username and password in case 
database authentication is enabled. URI style connections are also 
supported and supply the URI as the host in the *MONGODB_SETTINGS* 
dictionary with *app.config*. There are various custom query sets 
that are available within Flask-Mongoengine that are attached to 
Mongoengine's default queryset [flask-mongoengine]. 

### Installation

Flask-PyMongo helps connect Flask with PyMongo. It provides convenience 
helpers. It can be installed with an easy command such as this:

`$ pip install Flask-PyMongo`

PyMongo can be added in the following manner:
```
$ from flask import Flask
  from flask_pymongo import PyMongo
  app = Flask(__name__)
  app.config["MONGO_URI"] = "mongodb://localhost:27017/cloudmesh_community"
  mongo = PyMongo(app)
```
Multiple PyMongo instances can be used to connect to multiple databases or 
database servers:
```
$ app = Flask(__name__)
  mongo1 = PyMongo(app, uri="mongodb://localhost:27017/cloudmesh_community_one")
  mongo2 = PyMongo(app, uri="mongodb://localhost:27017/cloudmesh_community_two")
  mongo3 = PyMongo(app, uri=
        "mongodb://another.host:27017/cloudmesh_community_Three")
```
Flask-PyMongo provides helpers for some common tasks:

```
$ @app.route("/user/<username>")
  def user_profile(username):
      user = mongo.db.cloudmesh_community.find_one_or_404({"_id": username})
      return render_template("user.html", user=user)
```

## Workbreakdown

- Introduction - Nishad Tupe fa18-523-64
- Learning Outcome - Izolda Fetko fa18-523-60
- MongoDB - Nishad Tupe fa18-523-64
- PyMongo - Izolda Fetko fa18-523-60
- MongoEngine, Flask-Mongo - Vishal Bhoyar fa18-523-72 
- MongoEngine (Peer reviewed) - Izolda Fetko fa18-523-60
- Flask-PyMongo (Peer reviewed) - Nishad Tupe fa18-523-64
