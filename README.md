#### Title : EastAdvantage Take home exam
#### Author : Cyrene Brylle Carulasan


# Technical Examination
Create an address book application where API users can create, update and delete
addresses.
The address should:
- contain the coordinates of the address.
- be saved to an SQLite database.
- be validated



* Application Description:
This Rest api project is built in Django framework with 
library the Django Rest Framework, key feature and tools included are the ff.

1. Redis cache
2. sqlite database
3. JWT authentication
4. Swagger API documentation
5. Dockerize

* Summary
1. Docker desktop installtion
2. RUN docker-compose.yml
3. See Swagger API documentation
4. Test API using postman 
5. Perform Crud Operation


* Here is the ff. steps to run this project in your local computer

#### Step 1. Make sure you have "Docker desktop" in your machine.

        This docker website helps you to install Docker.

        For Windows
        https://docs.docker.com/desktop/install/windows-install/

        Linux
        https://docs.docker.com/desktop/install/ubuntu/

        Mac
        https://docs.docker.com/desktop/install/mac-install/


        Note : Open docker desktop before running the docker compose,
               Redis wont start if the docker is down.

#### Step 2. RUN docker-compose.yml
        2.1 : Open your terminal in the root folder where the "docker-compose.yml" is located.
        Now run this command in your terminal
        >>>> docker-compose up --build

        Note : Don't forget the --build command, this tells docker
               to install dependencies and build a docker image.

#### Step 3. See Swagger API documentation to verify the system is up and running.

        Here's the link
        http://127.0.0.1:9000/api/schema/swagger-ui/


********************You are almost done with the setup!***********

#### Step 4. Test API using postman 

        4.1 : Download and install postman is in this page
              https://www.postman.com/downloads/

              If you encounter issue of installing you can refer this YT link
              https://www.youtube.com/watch?v=5Fk6ef_mj9w 

              Credits to : Amit.Thinks

        4.2 : Import Postman collection and the environment variable

              You can find the collection in root folder "postman-collection"
            
              For the collection 
              postman-collection\addresses.postman_collection.json

              For the environment variables
              postman-collection\project.postman_environment.json


              Note: Once you finished import you must see the "project" folder
                    under collection and enviroment, to set the environment please select
                    in the dropdown upper right corner.


#### Step 5. Perform Crud Operation
        
        Send request by clicking "Send" button

        POST, GET, PATCH, DELETE

        1. POST token
        2. POST Create Address Book
        3. GET List Address Book
        ......



#************************************ Thats it! ***************************************


## License

MIT License

Copyright (c) 2024 Brylle Carulasan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.















    



