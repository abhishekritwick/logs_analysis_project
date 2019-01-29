# logs_analysis_project
The python file you need to run is "newsdata_analysis.py".

I have created 4 different views for the code to run. Run these commands in order:
1. create view articlelog as select author,title,slug,log.id,path,log.time from articles join log on '/article/'||slug = log.path;
2. create view authorlog as select authors.name,authors.id,title,path,time from authors join articlelog on authors.id = articlelog.author;
3. create view totallog as select count(*) as totalcount,DATE(time) from log group by DATE(time);
4. create view errorlog as select count(*) as errorcount,DATE(time) from log where status like '%404%' group by DATE(time);

After the vagrant is up and running, i.e. after you have used the commands vagrant up and vagrant ssh respectively, you can use 
python newsdata_analysis.py to run the code.
There will be 4 options for user to input from, based on which the responding actions will be taken. Option 4 exits the program where as options 1-3 give results for the 3 problems asked to solve in the project.
