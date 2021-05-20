## task
> Please provide a workable implementation for a REST API endpoint
documented in the attached swagger file.
- API receives some client information and returns a structure that
includes location details associated to the IP address;
- To fetch location information from IP you can use this service
http://ip-api.com/json/<ip_address>
- Please also provide unit tests for the implementation.

## solution
> install requirements.txt

> run *uvicorn main:app --reload* and go to http://localhost:8000/docs

> run test with *python -m pytest .*