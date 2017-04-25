# Web

This part of the Botai project is dedicated to connect to a trading platform and use the machine learning algorithms developed.

In order to connect to these king of platform we need a to 3-tier architecture with a minimal interface.

This application needs to make rest calls towards conversion rate platforms.
Process the datas in order to fit the input of the algortihms.
Store it somewhere and erase the out-of-date datas.

## Technologies Used

In order to accomplish that we have decided to use the **Spring-boot** framework for its easy-to-use and easy-to-deploy usage. 
Spring-boot is also __***well adapted to build a rest architecture***__.
Spring-boot inheriths from [Spring documentation](http://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/html/) which will make us learn the good practices and will avoid us to get stuck.
Once the application will be working we will use Spring-security to secure it.
Finally we will use Angular 2 framework to have a minimal interface.
The whole thing will be deploy with maven.


# How is it working

The application is scheduled to frequently calls (every 5 minutes or so) an API to refresh the values obtain from the Forex.
The application stores these values in a database (Combo MySQL + Hibernate).
The application is then calling the machine learning algorithm with a defined set of values. (We will improve this step by making the algorithm querying the database frequently independently).
The algorithm generates an action to do in a json format that the application will consume and store in the database.

