# Instacart Basket Analysis using MongoDB and Performance Benchmarking on VM and Cloud :hand: fa18-523-60, fa18-523-64, fa18-523-72

| Izolda Fetko, Nishad Tupe, Vishal Bhoyar
| ifetko@iu.edu, ntupe@iu.edu, vbhoyar@iu.edu
| Indiana University
| hid: fa18-523-60, fa18-523-64, fa18-523-72
| github: https://github.com/cloudmesh-community/fa18-523-60/edit/master/project-report/report.md
| code: TBD

---

Keywords: Online Grocery Shopping, Market Basket Analysis, Instacart, 
MongoDB, PyMongo, Kaggle.com Public API, Virtual Machine, Mongo Atlas

---

### Abstract

In today's busy world, time is a valuable asset. People 
are trying to save time and money in all segments of their 
lives, one of them being grocery shopping. Instacart is an 
e-commerce platform that helps them save both. This technology 
allows its app and website users to shop at their favorite 
stores as well as combine products from more than one store 
in the same order, without having to make the trips to those 
stores. Our project focuses on this interesting concept and 
conducts an Instacart market basket analysis while utilizing 
MongoDB as the data storage apparatus. The goal of our project 
is two-fold, the first part includes evaluating the benefits of 
this NoSQL database technology for the online shopping analysis 
purposes that can ultimately be applied to other e-commerce 
platforms. The second part entails a MongoDB performance 
benchmarking by testing it on a local machine, a virtual 
machine, and on a cloud service - Mongo Atlas.

### Introduction

The modern world is increasingly becoming busier each year. 
The number of daily tasks has exponentially increased compared 
to the days when our parents were in the same life stage as we 
are now. This increase in daily tasks is even more noticeable 
in the urban areas where people are, in their commute to and 
from those tasks, continuously being slowed down by traffic 
jams, construction, and other hurdles. In addition to the time 
constraint, cost of living is steadily increasing in all areas, 
with some urban area costs reaching the all-time highs. Due to 
these changes, humans are becoming very creative in finding ways 
to save their precious time and cut down the cost of living. In 
their search, a large number of individuals are turning towards 
the online shopping which allows them to fulfill their needs 
without all the hassle. The online shopping concept has been 
established by large companies such as Amazon, and it is slowly 
sneaking into other industries and services. One of those industries 
includes the large grocery stores and wholesale chains such as 
Krogers and Costco. These two companies are partnered with the 
grocery delivery service and platform which is the topic of our 
report - its name is Instacart [@www-partnerships]. 

This e-commerce platform was founded in 2012 by a former Amazon 
employee, Apoorva Mehta, who is the company's current 
CEO [@www-wikinstacart]. The service is mainly offered through 
the company website, but it also offers an Android and iOS 
version of a smartphone app [@www-apps]. To deliver its services, 
the company uses a team of "personal shoppers" to "procure grocery 
items from a variety of stores" in the desired geographical 
area [@www-apps]. The app allows one to place an order from a 
specific store or multiple stores while also offering substitutions 
for all items in case the originally chosen items are out of 
stock [@www-bold]. Once an order is placed, the app offers a live 
view of the actions performed by the "personal shopper" with 
timestamps for each step taken as well as their GPS location [@www-bold]. 
This is a very valuable feature as it helps Instacart users to 
prepare for the delivery. The service is paid for through the 
Android Pay or Apple Pay, depending on the app used [@www-pay], 
and the receipts are sent via email to the customers [@www-bold]. 
According to the Data and Machine Learning Advisor of the company, 
Jeremy Stanley, 2017 yielded more than 200,000 users and over 
3 million orders placed [@www-stanley]. These results are a great 
indicator of how software technologies and big data are slowly 
making changes in the way of how we think of grocery shopping and 
overall retail shopping in general.

In our project, we focus on the market basket analysis of the 
Instacart customers, more specifically on the 3 million orders 
that are publicly available via the Kaggle platform. The application 
built by our team allows a seamless download of the dataset via 
Kaggle's public API and data import into MongoDB. 
Once in this NoSQL database, the data is ultimately joined and wrapped 
into a form ready for data analysis. The exploratory analysis is completed
with use of PyMongo and the visualizations are completed with help of Python 
and its packages such as Numpy, Pandas, Matplotlib, Altair, and Seaborn. 
In this segment, the project touches upon statistics such as Average Order 
Size, Average Item Quantity per Order, Time of Order, Most Frequently Purchased 
Items, Most Frequently Purchased Categories of Items, and similar. The final 
stage of the project includes technology benchmarking, where our team 
is comparing MongoDB performance on a local machine, on a virtual machine,
and on a cloud service – Mongo Atlas. We are hoping that 
the results and the underlying idea of our research will not only encourage
other researchers to consider MongoDB as a suitable medium in future Big 
Data applications, considering its cloud capabilities, but also encourage 
them to become more curious about the Big Data involving online shopping.
The online retail market is rapidly expanding in all areas. Global 
companies are not the only ones who offer their products online any more.
Small, local stores are slowly starting to offer these services and 
compete with market leaders. This is in return slowly expanding the 
network of interconnected technologies, in other words, Internet of 
Things (IoT) realm. In this regard, the capabilities of the IoT are very 
impressive, but have an enormous potential to get even more fascinating. 
Currently, Amazon Alexa is capable of placing online orders on Amazon. 
Given the rate AI technology is accelerating nowadays, perhaps virtual 
assistants will have the capability of placing orders on non-native 
platforms in the near future as well.

## Requirements
TBD

## Design
TBD

## Architecture
TBD

### Dataset Description

In the recent years, data science has become one of the 
most important drivers of the modern economy. It is used 
to uncover actionable insights into the consumer markets, 
for conveying powerful messages drawn from big data to 
shareholders and consumers, as well as building technologies 
that are continuously improving the quality of life around 
the globe [@www-datascience]. This "growing importance of 
data science has, in turn, led to the growth and importance 
of data scientists" [@www-datascience]. An online platform 
that allows the continuous idea sharing, learning, and 
collaboration for those individuals is Kaggle.com.

Kaggle.com is a website, a virtual space where data
enthusiasts flock to explore project topics, work on 
their own projects, and participate in lucrative 
competitions [@www-kaggle]. This platform was created 
in 2010 by Anthony Goldbloom and Ben Hamner, and today 
it includes a community of more than one million data 
scientists and machine learners [@www-kaggle-blog]. According 
to the company's CEO (Anthony Goldbloom), the earliest competitions 
included  "participants who called themselves computer scientists, 
statisticians, econometricians and bioinformaticians" [@www-kaggle-blog]. 
Over time, those "silo-ed" communities came together, "shared 
different approaches and ideas through the forums and Kaggle Kernels"
[@www-kaggle-blog] which resulted in forming of the well-known platform we 
see today. According to the Kaggle documentation, the platform supports various 
types of datasets, such as CSV, Excel (although recommended to be 
uploaded as CSV), JSON, SQLite, BigQuery, and other [@www-kaggle-datasets].
Other file formats constitute PNG imagery files, NPZ specialty file formats, 
as well as complex hierarchical data formats like HDF5 [@www-kaggle-datasets]. 
Kaggle also supports archives, in other words, "files compressed using 
the ZIP file format as well as other common archive formats like 7z" 
[@www-kaggle-datasets]. The datasets are organized in a list on the Datasets 
webpage, and can be filtered in a few different ways: by searching a 
common term in the search bar; by choosing the dataset type from the drop-down 
menu; by choosing the dataset size; and/or by choosing one of the available tags 
in the Tags submenu. "Tags are added by dataset owners to indicate the 
topic of the dataset", as well as techniques that can be used to explore 
the dataset (e.g., "classification"), "or the type of the data itself 
(e.g., "text data")" [@www-kaggle-datasets].

To easily obtain those datasets, Kaggle offers their newly created 
Public API option to its users. API stands for "Application Programming 
Interface" "through which interactions happen between an enterprise and 
applications that use its assets" [@www-apiwiki]. "When used in the 
context of web development, an API is typically defined as a set of 
specifications, such as Hypertext Transfer Protocol (HTTP) request 
messages, along with a definition of the structure of response messages, 
usually in an Extensible Markup Language (XML) or JSON format" [@www-apiwiki].
Kaggle Public API  was launched in February 2018 and can be used for 
"creating datasets, kernels", or simply "connect with Kaggle" [@www-kaggleapi]. 
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

The importance of the Kaggle.com public API is significant. It minimizes the 
need for its users to manually download large datasets, hence saving them 
time when working on important projects. It is also helping students in 
expanding their knowledge and programming experience through practical 
examples and real-life data that can be later implemented in their 
professional work. 

As aforementioned, the Instacart Market Basket Analysis dataset is publicly 
available on the Kaggle website. It is a relational set of data files describing 
customers' orders over the time. It contains information for over 3 million
online grocery orders placed by more than 200 thousand anonymous Instacart users.
It includes data who users who placed at least four and no more than one hundred 
orders in the same year [@www-kaggle-data].

The dataset includes five separate CSV file which include product, order, aisle,
department, and order product. All entities in this group of files are associated with 
each other with unique ids. The product, aisle, and department are considered to bethe 
dimension entities while an order is the quantitative fact entity. The order details 
are available by a week day and by a day hour level [@www-kaggle-data].

### Litrature review

Mongo DB and Python both are open source technologies. One can get started quickly building 
an application on MongoDB using any of the languages that leverage a MongoDB's driver.
MongoDB offers a native driver called PyMongo to fit Python developer community needs. 
"MongoDB stores data in documents, however, they are not like Microsoft Word or Adobe 
PDF documents but rather JSON documents based on the JSON specification" [@www-pymongo]. 
There are several advantages of storing data in document format and some of them are 
flexible schema and ability to store arrays which are faster to process using native 
commands of Python scripts [@www-pymongo]. In June 2018, students of Indiana University 
of Bloomington Izolda Fetko, Rashmi Ray,  and Nishad Tupe explored the France accidents 
dataset using MongoDB, PyMongo, and Tableau to provide safety recommendations. They used 
the newest release of the MongoDB driver called the  *Mongo BI connector* that allows BI 
tools such as  Tableau to interact with MongoDB. The BI connector converts the Tableau's 
SQL-like commands on structured data into the native MongoDB commands while fetching data 
[@www-mongotab]. The team also used Pymongo and other web technologies to build the website 
that can store, update, and process records live and can be accessed by the global audience. 
As MongoDB is a NoSQL engine, it scales easily for multiple tables as single JSON object, 
and makes query retrieval speed faster than RDBMS, while avoiding complex joins. However, 
their research also shows that Tableau and MongoDB is a lousy marriage predominantly because 
Tableau was built before the NoSQL and Big Data was popular and is not yet mature to process 
the relational data [@www-mongoknowi]. Tableau's slow processing of joins, when connected 
directly to MongoDB, was one of the main reason authors decided to join the CSV files using 
Pandas data frame and use MongoDB as a backend tool. This tool allows a stable platform for 
the user-friendly BI tools such as Tableau to perform analytics on large datasets with 
millions of rows and also stand as a robust database on which one can build applications 
[@www-mongotab]. In the final step, authors created a website and provided links to various 
dashboards using technologies such as HTML, CSS, JavaScript, Bootstrap, Flask, JQuery.js, 
and Chartist.js [@www-mongotab]. Our project fosters a similar idea however instead of using 
the BI tools we will be creating a python application that can run seamlessly on any of the 
underlying environment - virtualized,  physical, or on a cloud. The basic idea here is 
building a packaged application to perform exploratory analysis on the Instacart basket 
data and perform the benchmarking of elapsed time and other constraints on hardware 
environment such as virtual machine, local machine, and cloud.

## Implementation
TBD

## Benchmark
TBD

## Conclusion
TBD

## Acknowledgement
TBD

## Workbreakdown

- Keywords - Izolda Fetko fa18-523-60
- Abstract - Izolda Fetko fa18-523-60
- Introduction - Izolda Fetko fa18-523-60
- Requirements - TBD
- Design - TBD
- Architecture - TBD
- Dataset Description - Izolda Fetko fa18-523-60
- Literature Review - Nishad Tupe fa18-523-64
- Implementation - TBD
- Benchmark - TBD
- Conclusion - TBD
- Acknowledgement - TBD
