MOTIVATION FOR PROJECT
This project helps gain better understanding of all the concepts learned throughout the course and allowed me to implement the knowledge I gathered.

Project Overview
This project is about: The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.

The project requires 3 Auth0 profiles with permissions as below:
    - Casting Assistant
        - has limited access
        - get:actors
		- get:movies
    - Casting Director
        - has limited access
        - delete:actors
		- get:actors
		- get:movies
		- post:actors
		- update:actors
		- update:movies
	- Executive Producer
		- has all the permissions
		- delete:actors
		- delete:movies
		- get:actors
		- get:movies
		- post:actors
		- post:movies
		- update:actors
		- update:movies

Auth0 details used during the testing:

    - Domain - dev-jdd6v-si.us.auth0.com
	
    - Client Id - z9n4IAz9fX4I0QYcKdgIzAvuZhJhW1ty
	
	- Casting assistant access token:
	
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwYzBlMDljODMwMDZmMWIyMjQ2IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTIyNDg0OSwiZXhwIjoxNjQxMjMyMDQ5LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.A1DEm_87T5kpDuUXHUy99o9BFeZN9EX-y7W0isdqiNOsCqbFs8mWnC9vSQb2ctHmHOqR1dKeFLGT9WJ1nt8NtlDTHavvWJkhjLtpxEESGXL5ggjGRfN7K91X0juIamDXv2ut3m-YuH98fxF_kgD-eNbnrhnclgsGHaigC7q7B_9pwbp6Qze_BzA5r0UAVxYvesfbtkqjRBJovM2-EdFarHtfmX0sLL6ublrMgNrwySWassFVQyniZQw3oML6MDA21pWyM0xcIvH3vkbKoz3YvfLmh6430yQ7S-GC4o7-icSG4clWeX7Oo5OKvlWQ9W7LwWMe0tXnDg0CsTGJKThHsQ
	
	- Casting director access token:
	
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwOTRmYTJjZDEwMDY5ZWU2Mjc5IiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTIyNDc4NywiZXhwIjoxNjQxMjMxOTg3LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicG9zdDphY3RvcnMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.rqfi7Ppxsur8TBi7w_yM3bLYWDdnYK-S1H2rKX9MfagEsQj9lZhziHp2bgbykHw_o5i_MQwo2i4fJ12Rf5MJFxz7kW2GF_nizi97SYKKBffTVPaj4-XQVlPJs7ds5Vzy_P9JlobpngD4XUY1D3aTYofGXYD96RJ-oFn8cl_VmU1mee3Z-xDkVbo7hwuTD9hZwGel0804oYezRlmom7U9InZqejQDAlaozUOpWsTDyhE598sDnUxjI1FxJcRP49F8HN_9P85Gxnaw-aIXqq9cDvRah-XC-I-aQ_iF9oZlYwtGhR0YxSnWCWGEc9zbL8acH6xbBge1659zJE7YEzX3Kw
	
	- Executive producer access token:
	eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlVScURuVWxJWlFYQko5MWFOVkdWOCJ9.eyJpc3MiOiJodHRwczovL2Rldi1qZGQ2di1zaS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjFkMTgwNWZmYTJjZDEwMDY5ZWU2MjZlIiwiYXVkIjoiY2FzdGluZ2FnZW5jeSIsImlhdCI6MTY0MTIyNDQ4NSwiZXhwIjoxNjQxMjMxNjg1LCJhenAiOiJ6OW40SUF6OWZYNEkwUVljS2RnSXpBdnVaaEpoVzF0eSIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiLCJ1cGRhdGU6YWN0b3JzIiwidXBkYXRlOm1vdmllcyJdfQ.dpBNNVA6R0gpMGCoWZmNzlRaJnbrOUyQd4zGcZSoDtgDSZEXNwRKaTGmE6pJGb7Jy2Gho6ZmWzpSRht1UUqHUf9bCVx4pEV2E7IS3dgfsn32IAbZjHgoB8kwS9eTLd7wmyzVxaYmV4IwhbU7eO1RTllcVWDHKPuO2k96ZQ2x9p-ZScIZeYWWWPr5MRuqVJkaxQ0feO_12Jgah0oUFq1cpnQVByyLiWJ5i91D43B9FL-9q0Wktv2-qU4Xv2MPCRAvYjVM52RlQcKimH6W0NPsa-_y2P9qUCXeUn8mk2sbyNjkfIXlXSJnewiQfa36h0IFrUVhh1-jlXyeTNxfz3Xl3g

URL where the project is hosted via heroku - https://casting-agency19.herokuapp.com/

API Endpoints for the project:
Endpoints:

GET /actors
returns a list of all actors

GET /movies
returns a list of all movies

POST /actors
create a new actor

POST /movies
create a new movie

PATCH /actors/<int:actor_id>
update an existing actor

PATCH /movies/<int:movie_id>
update an existing movie

DELETE /actors/<int:actor_id>
delete an existing actor

DELETE /movies/<int:movie_id>
delete an existing movie
