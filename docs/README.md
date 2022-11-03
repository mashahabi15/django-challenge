### Selling Platform Project

This project consists of 4 apps:
* users: Sign up and login
* stadiums: Defining new stadium and its seats
* matches: Defining new matches in stadium and define seats of a match
* reservations: Reserve tickets

All models are defined in ERD file in the current directory. (**selling_platform_erd.pdf**)
One challenge in this project is to prevent race conditions when reserving tickets. My solution to this problem is as
 follows(It takes more time to implement so I describe it here):
We can define a reservation topic via Kafka(or any other message broker). Each message in this topic is a request for reservation.
The consumer serves each message one by one to reduce race condition.(I used the term _reduce_ because we cannot use this solution
in a distributed system) It also has some delays because reservation request is not responded immediately.
