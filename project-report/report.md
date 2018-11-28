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

In today's world there are many creative individuals and groups 
that are trying to develop products, projects, and businesses 
based on their unique ideas and talents. In many cases, an idea 
or a talent is not enough to accomplish this. Capital funds
are one of the main elements of a successful startup process. 
Although there is a significant number of government programs 
in the United States designed to help small businesses and 
creative indivials to obtain necessary funds for their projects, 
a high number of start-ups nonetheless remain capital constrained
[@www-voelker]. This is the reason why the *Kickstarter* platform 
was developed and is still successfully operating since 2009 
[@www-voelker].

*Kickstarter* is a web-based crowdfunding platform that helps 
support creative arts around the globe [@www-voelker]. As of 
November, 2018, *Kickstarter* has pledged more than four 
billion dollars while successufully funding more than 150 
thousand projects [@www-kickstarter-stats]. Overall, the 
platform has had more than 15 million backers, out of those, 
5 million were repeated backers, which totalled in more than 
49 million pledges [@www-kickstarter-stats]. The highest pledged 
category is *Games* with more than 580 million dollars in 
successful projects and success rate of 36.55% 
[@www-kickstarter-stats]. 

*Kickstarter* uses the fundable project model where the would-be 
business owners or project managers submit their project along 
with the necessary project information and its funding goal.

> "The funding goal establishes a base target for the project 
> and a deadline (generally 30-days) to achieve the funding" 
> [@www-voelker]. 

The prospective artists and entrepreneurs typically display their 
projects in a video form where they have the opportunity to outline
the project along with its benefits and funding requirements 
[@www-voelker]. The video is shown on the *Kickstarter* project 
webpage along with the number of backers, the amount of funds 
received/pledged as well as the fundraising goal. As each project 
is timed, the time remaining in the *Kickstarter* promotion is 
shown on the project page as well. Since the platform is based on 
an *all or nothing* funding model, pledged funds are not available 
to the entrepreneurs until the end of the funding period which 
is determined by the goal-setting statement [@www-voelker]. The 
financial transcations occur only in cases where a projects meets 
its initial targets and funding expectations [@www-voelker]. If 
the initial target is exceeded, the project received all funding 
as well as the excess of its goal.

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
performance benchmarking. When it comes to connecting to 
MongoDB, our team had determined that the PyMongo driver is 
a logical choice not only due to Python's programming 
versatility and flexibility, but also due to the 
compatibility between Python dictionaries and MongoDB's 
BSON objects. This report introduces the reader to the 
related work in the MongoDB realm, as well as the Kaggle platform 
and the chosen dataset prior to presenting the project design 
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

> "When used in the context of web development, an API is typically 
> defined as a set of specifications, such as Hypertext Transfer Protocol 
> (HTTP) request messages, along with a definition of the structure of 
> response messages, usually in an Extensible Markup Language (XML) or 
> JSON format" [@www-apiwiki].

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

The Kickstarter Projects dataset is publicly available on the Kaggle website. 
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

### Technologies and tools used in this project are:

* Python version 3.6 and it's libraries Seaborn,Matplotlib,Pandas etc.
* PyMongo Driver, Bash Shell 
* Cloud services - MogoDB Atlas, 3 node replica cluster
* Cloud services - Digital Ocean, Ubuntu 18.04 ,MongoDB 3.6.3
* Cloud services - AWS, Linux, MongoDB 3.6.3

## Code Organization

Code is checked-in on GitHub at location 
https://github.com/cloudmesh-community/fa18-523-60/tree/master/project-report/bin
Our code is organized as described below , 

### bin

  - main.py 
  - load_csv.py
  - mongo_install.sh
  - mongo_uninstall.sh 
  
### dataset
  
  - link to dataset
  - steps to download using kaggle.com
  

## Architecture

TBD

## Observations and Visualizations

TBD

## Conclusion
TBD

## Acknowledgement
TBD

## Workbreakdown
TBD
