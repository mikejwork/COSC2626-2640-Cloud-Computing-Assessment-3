# COSC2626-2640-Cloud-Computing-Assessment-3      
Timed Practical AWS Cloud System Development   
   
• Task 1: Design and develop a highly scalable application by applying the knowledge of distributed architecture 
and multiple cloud services    
• Task 2: Develop a professional project report   
• Task 3: Write a user' manual to introduce your product    
• Task 4: Deliver a presentation to introduce your project and demo your product     

### Personal Assignment notes:
From previous assessments within this subject i have become more confident with web applications using AWS.
I have changed my previous outlook on the assessment from an online store to a budgeting application, to track bank accounts
and savings, also enabling the user to input the stocks that they own, using a third party API be able to get prices of these stocks
and show a live price of their assets to the user.

## AWS Features / Plan
I will be hosting the site on AWS Elastic beanstalk which will automatically handle scaling and load balancing for me.
The site will be hosted on an EC2 Instance with Python Flask, using external market APIs, Javascript graph libraries, and more utilities from AWS

AWS CodePipeline is being utilised, which allows me to link my Elastic Beanstalk project to a github repository, and will automatically update the instance whenever a build is pushed to the main branch, extremely useful and saves me a considerable amount of time.
