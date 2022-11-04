# django-testing

Simple project containing:
 - login page
 - logout
 - home page
 
# Build

### If you want to be able to modify the project with live reload

Clone this project to your local machine

Make sure __docker__ is installed and running in your machine (with docker-compose)

Your folder structure should look like this:
```
django-testing
├── .github
│   └── workflows
│       └── publish-image.yml
├── ci/
├── src
│   ├── .env
│   ├── docker-compose.yml
│   └── web/
│       ├── ..
│       ..
└── README.md
```
Navigate to django-testing/src

Build the image using compose:
```bash
docker-compose -f docker-compose.yml build
```
Once built, run the image:
```bash
docker-compose -f docker-compose.yml up
```


## Django unit tests

unit tests found in src/web/app/mysite/tests
When the container is __running__, tests can be ran with:
```bash
docker-compose exec web python manage.py test
```
output should look like:
```bash
Found 1 test(s).
Creating test database for alias 'default'...
SiteLogin
System check identified no issues (0 silenced).
creating user named 'admin'...
...user named 'admin' created with password 'secret'
.
----------------------------------------------------------------------
Ran 1 test in 0.159s

OK
Destroying test database for alias 'default'...
```

## Coverage.py

Coverage library is used and can be used to run project tests
Instead of running tests with previous command, we can use `coverage run` to replace `python` in the `docker-compose exec web python manage.py test` command

```bash
docker-compose exec web coverage run manage.py test
```
Then you can generate the report in the format that you would like, ([see the docs](https://coverage.readthedocs.io/en/6.5.0/cmd.html#execution-coverage-run))

In this project we generate a html report, you can do this with:
```bash
docker-compose exec web coverage html 
```
output should be:
```bash
Wrote HTML report to htmlcov/index.html
```
*note: you can change output folder name, just read the docs :)*


## CI
**This is the fun part where we will try to:**
 - build the image
 - run the tests using coverage
 - generate the html report and save it as an artifact
 - upload the html report to github pages
 - upload the web image to ghcr (github container registry)
 - optional: enjoy life
 
All this in a single workflow
Workflow stuff can be found here (https://github.com/JulesFF/django-testing/actions)
Coverage report can be found here (https://julesff.github.io/django-testing/)
