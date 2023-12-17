Readings: VPC
Below you will find reading material and additional resources that support today’s topic and the upcoming lecture.

After you’ve completed the reading, answer the following:

How can one host within a VPC any services that need to be public?1. Open a door: Put your service in a public subnet and give it a public IP address like an Elastic IP. This is simple, but less secure.
Use a bouncer: Put your service in a private subnet and use a NAT gateway or load balancer to handle public traffic. This is more secure, but slightly more complex.
What are examples of services that would live in the publicly-accessible part of the VPC? The privately-accessible part? Web servers: Websites, web applications, and APIs that need to be accessed by users on the internet. public vpc are websites,public appas and external tools private vpc are important data and servers and development and testing areas 
Load Balancers: Distributing traffic among multiple instances of a public service. Databases: Storing sensitive data that should not be publicly accessible.
Internal APIs: APIs used by other services within the VPC but not accessible to the public.
Management tools: Server management tools for controlling and monitoring resources.
CDN (Content Delivery Network): Caching static content for faster delivery to users worldwide.
What are the trade-offs of using a VPC vs traditional infrastructure? Scalability,Easy hybrid cloud deployment,Better performance,Better security
Reading
What is a Virtual Private Cloud(VPC)Scalability:
