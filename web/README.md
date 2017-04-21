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
