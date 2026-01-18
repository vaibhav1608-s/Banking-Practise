FROM python:3.11-slim 
#WHICH version to use

#in container make a folder myapp and put all the files over there 
WORKDIR /myapp

#copy all the file from my current directory
COPY . . 

#how to run the files which were copied , -r means read ,--no-cache-dir -> install them but dont store on local macheine
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#cmd tells dockere what command to run when the container start 
#unicon is used to start the server in fast api 
#--host 0.0.0.0-> this will listen on all the port 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
 