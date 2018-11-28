# Kickstarter Projects Analysis :hand: fa18-523-60, fa18-523-64, fa18-523-72

| Izolda Fetko, Nishad Tupe, Vishal Bhoyar
| ifetko@iu.edu, ntupe@iu.edu, vbhoyar@iu.edu
| Indiana University
| hid: fa18-523-60, fa18-523-64, fa18-523-72
| | github: [:cloud:](https://github.com/cloudmesh-community/fa18-523-60blob/master/project-report/report.md)
| code: TBD

---

Keywords: MongoDB, PyMongo, Crowdfunding, Virtual Machine, Cloud, Data Analysis, Cloud Performance
          
---

## Abstract

Crowdfunding is a certain way of raising funds where 
individuals come together and collectively support 
projects by investing in them. Kickstarter is one 
of the leading crowdfunding platforms in the world
that helps individuals/businesses in various categories 
such as art, film, music, theatre, games, design, and 
other, to raise necessary funds to complete their projects. 
This paper explores the utilization of big data technologies 
and cloud services such as MongoDB, virtual machines, 
MongoDB Atlas, DigitalOcean, AWS, and PyMonogo while 
analyzing the *Kickstarter Projects* dataset obtained 
from the Kaggle datascience platform.

## Introduction

Many creative individuals and groups around the globe are trying 
to develop products, projects, and businesses based on their 
unique ideas and talents. In many cases, an idea or a talent 
is not enough to accomplish this. Capital funds are one of the 
main elements of a successful startup process. Although there 
is a significant number of government programs in the United 
States designed to help small businesses and creative indivials 
to obtain necessary funds for their projects, a high number of 
start-ups nonetheless remain capital constrained [@www-voelker]. 
This is the reason why the *Kickstarter* platform was developed 
and is still successfully operating since 2009 [@www-voelker].

*Kickstarter* is a web-based crowdfunding platform that helps 
support creative arts around the globe [@www-voelker].
*Kickstarter* uses the fundable 
project model where the would-be business owners or project 
managers submit their project along with the necessary project 
information and its funding goal.

> "The funding goal establishes a base target for the project 
> and a deadline (generally 30-days) to achieve the funding" 
> [@www-voelker]. 

Our project includes several big data technologies while exploring 
the *Kickstarter* dataset collected in the 2009-2018 timeframe and 
made public via Kaggle, a well known datascience platform. The base
technology used to store and query the dataset is the widely known
NoSQL database called MongoDB. Three cloud services chosen to be 
benchmarked against each other are MongoAtlas, DigitalOcean, and 
AWS. Our team had created virtual machines in each service and 
performed a basic exploratory analysis. The time needed to query
the dataset was used as a quantitative measure to analyze the 
relative benchmarking. Moreover, our team also provides an 
ease-of-use review of each service as an addition to the 
performance benchmarking. This report introduces the reader 
to the related work in the MongoDB realm, as well as to
the chosen dataset prior to presenting the project design 
and research methods, architecture, technologies, and results. 

## Literature review

MongoDB and Python both are open source technologies. One can 
get started quickly building an application on MongoDB using 
any of the languages that leverage MongoDB's driver. MongoDB 
offers a native driver called PyMongo to fit Python developer 
community needs.

> "MongoDB stores data in documents, however, they are not like 
> Microsoft Word or Adobe PDF documents but rather JSON documents 
> based on the JSON specification" [@www-pymongo].

There are several advantages of storing data in document format 
and some of them are flexible schema and ability to store arrays 
which are faster to process using native commands of Python scripts 
[@www-pymongo]. In June 2018, students of Indiana University of 
Bloomington Izolda Fetko, Rashmi Ray, and Nishad Tupe explored 
the France accidents dataset using MongoDB, PyMongo, and Tableau 
to provide safety recommendations. They used the newest release 
of the MongoDB driver called the  *Mongo BI connector* that 
allowed BI tools such as Tableau to interact with MongoDB. 
The BI connector converts the Tableau's SQL-like commands on 
structured data into the native MongoDB commands while fetching 
data [@www-mongotab]. The team also used PyMongo and other web 
technologies to build the website that could store, update, and 
process records live and can be accessed by the global audience. 
As MongoDB is a NoSQL engine, it scales easily for multiple tables 
as a single JSON object, and makes query retrieval speed faster 
than RDBMS, while avoiding complex joins. However, the research also 
showed that Tableau and MongoDB is a lousy marriage predominantly 
because Tableau was built before the NoSQL and Big Data were popular 
and is not yet mature to process relational data [@www-mongoknowi]. 
Tableau's slow processing of joins, when connected directly to MongoDB, 
was one of the main reason authors decided to join the CSV files using 
Pandas data frame and use MongoDB as a backend tool. This tool allows 
a stable platform for the user-friendly BI tools such as Tableau to 
perform analytics on large datasets with millions of rows and also 
to stand as a robust database on which one can build applications 
[@www-mongotab]. In the final step, authors created a website and 
provided links to various dashboards using technologies such as HTML, 
CSS, JavaScript, Bootstrap, Flask, JQuery.js, and Chartist.js 
[@www-mongotab]. Our current project fosters a similar idea, 
however, instead of using the BI tools the team had created a 
Python application that has a capability of running seamlessly on 
any of the underlying environments - virtualized,  physical, or 
on a cloud. Finally, the report provides summarized findings 
and conclusions.

## Dataset Description

### Kaggle API

The technology used to easily obtain the Kickstarter Projects 
dataset is the newly offered Kaggle Public API. API stands for 
*Application Programming Interface* through

> "which interactions happen between an enterprise and applications 
> that use its assets" [@www-apiwiki].

Kaggle Public API was launched in February 2018 and can be used for 
*creating datasets, kernels*, or simply *connect with Kaggle* 
[@www-kaggleapi]. Although still in its beta phase, it allows a more 
user-friendly data download as well as a seamless workflow for 
its community members. To be able to use this technology, users 
need to ensure that they had installed the latest Python 3 version 
on their machines as well as the pip package manager [@www-githubkagapi].
Accessing the Kaggle API is done by using a simple command line; however, 
this is not possible until a Kaggle account is created 
[@www-githubkagapi]. Once the initial step had been completed, an 
API token can be created, which triggers a download of a JSON file 
that contains the user credentials necessary to access the API 
[@www-githubkagapi]. Once the sign-up had been finalized, various 
command lines can be used to access the list of competitions along 
with the files and submissions associated with them [@www-githubkagapi]. 
A different set of commands can be used for dataset downloads and 
dataset creation, while the final group of commands listed on the 
Kaggle API GitHub page are the commands to manage Kernels, more 
specifically Kernel pull and push [@www-githubkegapi].

The importance of the Kaggle's public API is significant. It minimizes 
the need for its users to manually download large datasets, hence saving 
them time when working on important projects. It is also helping students 
in expanding their knowledge and programming experience through practical 
examples and real-life data that can be later implemented in their 
professional work.

### Kickstarter Projects Dataset

The Kickstarter Projects dataset is publicly available on the Kaggle website
and can be accessed using this [path](https://www.kaggle.com/kemical/kickstarter-projects#ks-projects-201801.csv).
The instructions on how to obtain the dataset using the Kaggle API can be found
[here](https://github.com/cloudmesh-community/fa18-523-60/blob/master/project-report/dataset/Kaggle%20API%20and%20Dataset%20Download%20Instructions.txt).
The dataset is available in the CSV format and contains more than 370 thousand 
projects submitted to Kickstarter between 2009 and 2018 [@www-kaggle-kickstarterdata]. 
The dataset variables allow versatile data analysis which is presented in the Results 
segment of our project. Other than the project ID, the dataset contains information 
on the project name; main category and category of campaign; currency used to support 
the project; fundraising goal (the amount of funds needed to complete the project); 
project launch; project crowdfunding deadline; state – current state of the project; 
actual funds pledged to the project along with the number of backers; the country of 
origin; and the total amount of funds pledged by currency [@www-kaggle-kickstarterdata].

## Design and Methods

TBD

## Technologies

### Technologies and Tools Used

* Python version 3.6 and it's libraries Seaborn,Matplotlib,Pandas etc.
* PyMongo Driver, Bash Shell 
* Cloud services - MogoDB Atlas, 3 node replica cluster
* Cloud services - Digital Ocean, Ubuntu 18.04 ,MongoDB 3.6.3
* Cloud services - AWS , Amazon Elastic Comput Cloud (EC2), Linux, MongoDB 3.6.3

## Code Organization

Our code is checked-in on GitHub and can be accessed by using this 
[link](https://github.com/cloudmesh-community/fa18-523-60/tree/master/project-report/bin).
It is organized as described in the following section.

### bin

  - main.py 
  - load_csv.py
  - mongo_install.sh
  - mongo_uninstall.sh 

## Architecture

From the beginning of the project, we aimed to make scalable python code that 
can run seamlessly on different cloud environments. We mainly used cloud 
computing services from Amazon Web Services(*AWS*), *Digital Ocean* as "IaaS" 
and MongoDB *Atlas* "DBaaS" platform. Though *AWS* is giant cloud provider with 
multiple cloud services, we found *Digital Ocean* user-friendly interface to 
manage the virtual machines(VM's) is very much attractive. The architecture 
diagram (dotted box 1) shows the client machine or application tier where the 
source code(*.py*) was stored and used for performance benchmarking. We also 
kept a copy of source code and other scripts on the cloud VM’s file systems. 
We used PyMongo driver as one of the primary components for communicating with 
the MongoDB database. Not only PyMongo provides MongoDB driver access to python 
libraries but also a recommended choice when wrangling data with MongoDB 
[@www-mongodbpymongo]. 
During the initial loading phase of “kickstarter.csv” 
dataset, we imported the raw data using MongoDB import command line (dotted box 
2) on *Digital Ocean* & *AWS* cloud VM’s. We wrote a custom bash shell script 
that installs, configures the MongoDB environment and then imports the CSV data 
to MongoDB(dotted box 2) To load the data in the MongoDB Atlas cluster(dotted 
box 3) we used simple python function *load_csv.py* (dotted box 1) 
primarily because MongoDB Atlas is *DBaaS* cloud service and typically in 
*DBaaS* users do not have control or access to OS resources such as file system. 
In most of basic of form, our M0 cluster consists of one primary node and two 
secondary nodes. The primary nodes are responsible mainly for write operations 
while the secondary nodes replicate primary’s *oplog* such that secondary 
nodes datasets reflects primary’s dataset so 

> "when the primary is 
> unavailable an eligible secondary will hold an election to elect itself the new 
> primary" [@www-mongodbreplica]. 

Thus the replica set arrangement ensures high 
availability of data. Optionally we can configure the arbiter node which does 
not hold any data but keep the track quorum in a replica set. Since arbiter node 
does not hold any data, they act as a suitable repository to keep the heartbeat 
information at a cheaper cost [@www-mongodbreplica]. 
On the contrary, we found 
IaaS services provide greater control and customization to the OS resources but 
adds overhead to perform the configuration and other tasks which can be tricky 
and may induce a lag time for writing the code due to incomplete pre-requisites. 
On the cloud VM's we hosted a single instance MongoDB database on Ubuntu 18.04 
platform (dotted box3). As post install steps we install python anaconda 
distribution and other necessary libraries for analysis. The communication 
between MongoDB and python application happens by connecting string. The connect 
string must have a valid username and password and necessary privileges to 
access and modify the database. To accept the remote connection, one of the 
vital step to set a value of bind_ip to 0.0.0.0 in *mongodb.conf* file that 
resides on VM. For all cloud providers, we used free-tier services. We observed 
notable advantage of using MongoDB Atlas free tier service often called as “M0 
cluster”. By default, the M0 cluster comes up with three node replica sets and 
512 MB storage(dotted box 3), the replica set is a group of *mongod *processes 
which provides redundancy and high availability to the application while 
accessing the MongoDB data. 


## Observations and Visualizations

TBD

## Conclusion
TBD

## Acknowledgement
TBD

## Workbreakdown
TBD
