# fauzan-technical-test

Fauzan Fajar Saputra – Technical Test Documentation

Table of Contents

This project is a submission for a technical test that demonstrates skills in Backend Development, automation in collect data, and data processing. It includes three core tasks:

1.	Backend Development
2.	Automation Testing
3.	Data Processing

Environment Setup

To run the project, please ensure that the following dependencies are installed in your environment. You can use Express.Js and Python 3 and install the necessary libraries by running:
1.	Node and Express.Js
2.	Python 3.x
3.	Dependencies (npm install)
4.	Postman (for testing APIs).
5.	Linux based environment for cron jobs.
6.	SQLite (or another relational database management system)
 
Point 1:  Backend Development

Description

I developed a simple API server using Node.js and the Express.js framework. This server is designed to receive form data from a frontend via a POST endpoint, storing it in an in-memory array. It then retrieves this stored data via a GET endpoint, demonstrating my ability to build a fully functional RESTful API, manage the data flow between a client and a server, and leverage a web framework to accelerate the development process.

How to Run

1.	Install the Express.js framework using the command npm install express.
2.	Run the server with node server.js.
3.	To test the POST endpoint, send a request to http://localhost:3000/api/submit-form using Postman with JSON data in the body.
4.	To test the GET endpoint, send a request to http://localhost:3000/api/get-data.

Code Explanation
 
•	The code begins by importing the express library and initializing the Express application. The port is defined as 3000, which is the port the server will run on.
•	Next, the code uses the express.json() middleware. This middleware's function is to parse the JSON data sent in the body of an HTTP request. Without this middleware, the server wouldn't be able to read form data submitted from the frontend in JSON format.
•	The server uses an empty array called formDataStore to store simple temporary data. This acts as an in-memory "database," where all received data will be stored while the server is running.
•	The POST endpoint is at /api/submit-form. This endpoint's function is to receive form data from the client (frontend) and add it to the formDataStore. When a POST request is sent to this URL, the server will process the data in req.body, store it, and send a success response back to the client.
•	The GET endpoint is at /api/get-data. This endpoint returns all stored data. When a client (frontend) sends a GET request to this URL, the server retrieves the entire contents of the formDataStore array and returns it as a JSON response, allowing the client to access the stored data.
•	Finally, the code starts the server and makes it listen on the specified port.

Output
•	http://localhost:3000/api/submit-form
•	http://localhost:3000/api/get-data
 
Point 2: Automation Testing

Description

I implemented an automation solution for data management by creating two Python scripts. The first script collects data and saves it as a .csv file, and is scheduled to run three times daily at 08:00, 12:00, and 15:00 using cron tab. The second script acts as a data cleansing tool, automatically deleting files older than one month. This implementation showcases my skills in scripting, task scheduling, and routine data maintenance.
How to Run

1.	Ensure Python 3 is installed.
2.	Create the /home/cron directory.
3.	Add the provided Python scripts to a Linux-based environment.
4.	Set up the cron jobs by running crontab -e and adding the following lines:
0 8 * * * python3 /home/fauzanfs/Automation_Testing/data_collector.py
0 12 * * * python3 /home/fauzanfs/Automation_Testing/data_collector.py
0 15 * * * python3 /home/fauzanfs/Automation_Testing/data_collector.py
30 0 * * * python3 /home/fauzanfs/Automation_Testing/data_cleanser.py

Code Explanation

•	Data_collector.py
•	Data_cleanser.py
•	Crontab -e

Point 3: Data processing

Description

For this task, I manipulated data in a relational database using Structured Query Language (SQL). I wrote a series of queries to manage employee data, including basic operations like inserting new records and updating existing ones. I also performed aggregate calculations and used sorting and filtering to extract specific information, demonstrating my deep understanding of how to use SQL queries to answer business questions and manage data efficiently.

How to Run

1.	Ensure SQLite is installed and that the sqlite3 command is accessible from your terminal.
2.	Run the SQL queries using a database client or by piping a .sql file to the sqlite3 command.

Code Explanation

•	Creating employee table : A query is used to create the employee table with columns for Name, Position, JoinDate, ReleaseDate, Year_of_Experience, and Salary.
•	Input employee data into employee table
•	Adding new employee called Albert: Queries are used to populate the employee table with the initial data from the test. A separate query adds the new employee, Albert.
•	Update engineer salary to $85 : The query updates the Salary of all employees with the Position of 'Engineer' to 85.
•	Number of active employee salaries in 2021: The query calculates the total salary for all active employees in 2021.
•	Showing the 3 employees with the highest work experience: ORDER BY and LIMIT: The query sorts employees by Year_of_Experience in descending order and limits the result to the top 3.
•	Displays the names and experience of employees with engineering positions under 3 years: WHERE, a query filters employees by Position ('Engineer') and Year_of_Experience less than or equal to 3.
 
Conclusion

This project demonstrates my ability to integrate backend development, automation, and data processing. Each of these tasks is essential for the role and showcases my problem-solving skills in software development.

Attachments

•	server.js: Node.js backend server code.
•	data_collector.py: Data collection script.
•	data_cleanser.py: Data cleansing script.
•	database.sql: SQL queries for data processing.
