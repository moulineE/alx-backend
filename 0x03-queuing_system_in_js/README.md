# 0x03. Queuing System in JS

## Introduction
This project focuses on implementing a queuing system in JavaScript using Node.js, Express.js, and Redis. The project covers various aspects such as setting up a Redis server, using Redis for basic and advanced operations, implementing job queues with Kue, building an Express.js application interacting with Redis and queues, and testing the functionality.

## Authors
- Johann Kerbrat, Engineering Manager at Uber Works

## Project Description
This project aims to build a queuing system in JavaScript using the following technologies:
- JavaScript (ES6)
- Redis
- Node.js
- Express.js
- Kue

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:
- Running a Redis server on your machine
- Performing simple operations with the Redis client
- Using a Redis client with Node.js for basic operations
- Storing hash values in Redis
- Dealing with async operations with Redis
- Using Kue as a queue system
- Building a basic Express.js app interacting with a Redis server
- Building a basic Express.js app interacting with a Redis server and queue

## Requirements
- All code will be compiled/interpreted on Ubuntu 18.04, Node 12.x, and Redis 5.0.7
- All files should end with a new line
- Required files: `package.json`, `.babelrc`
- Run `$ npm install` when you have the `package.json`
- Code files should use the `.js` extension

## Tasks
1. **Install a Redis instance**
    - Download, extract, and compile Redis
    - Start Redis server
    - Set and retrieve values using the Redis client
    - Copy `dump.rdb` to the project root

2. **Node Redis Client**
    - Install `node_redis` using npm
    - Write a script to connect to the Redis server and log connection status

3. **Node Redis client and basic operations**
    - Write a script to perform basic Redis operations using callbacks

4. **Node Redis client and async operations**
    - Modify the previous script to use ES6 async/await with promisify

5. **Node Redis client and advanced operations**
    - Store hash values in Redis and retrieve them using the client

6. **Node Redis client publisher and subscriber**
    - Create scripts to act as Redis client publisher and subscriber

7. **Create the Job creator**
    - Create a queue with Kue and create jobs with specified data

8. **Create the Job processor**
    - Create a queue process to listen to new jobs and process them accordingly

9. **Track progress and errors with Kue: Create the Job creator**
    - Create a job creator with error handling and progress tracking

10. **Track progress and errors with Kue: Create the Job processor**
    - Create a job processor with error handling and progress tracking

11. **Writing the job creation function**
    - Write a function to create jobs and test it

12. **In stock?**
    - Create an Express.js server to manage product listings and reservations

## Resources
- Redis quick start
- Redis client interface
- Redis client for Node.js
- Kue (deprecated but still used in the industry)

## Getting Started
1. Clone the GitHub repository: [alx-backend](https://github.com/moulineE/alx-backend)
2. Navigate to the directory `0x03-queuing_system_in_js`
3. Follow the instructions in each task to complete the project

## How to Run
1. Make sure you have Node.js and Redis installed on your machine.
2. Navigate to the project directory.
3. Run `$ npm install` to install dependencies.
4. Follow the instructions provided in each task to run the scripts or start the server.

## Testing
- For testing, run `$ npm test` followed by the test file name.
