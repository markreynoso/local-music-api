# local-music-api
---
### NW Music Scene API
Version: 1.0.0
ULR: [nwmusicscene.herokuapp.com](https://www.nwmusicscene.herokuapp.com)

NW Music Scene is a growing database of bands local to the Pacific Northwest. Finding local music is not always easy, so this project is looking to make finding and supporting your local musicians easier and more intuitive. 

The NW Music Scene API is a searchable database which can be used to lookup more information about a band you know, or search based on styles you prefer and we will find bands that match your prefernce. All responses are returned in JSON format.
* See full band list
* Search based on band name
* Search based on style preferences

### Authors
---
* [markreynoso](https://github.com/markreynoso/local-music-api)

### Dependencies
---
* beautifulsoup4==4.6.0
* click==6.7
* Flask==0.12.2
* Flask-API==1.0
* Flask-Migrate==2.1.1
* Flask-PyMongo==0.5.1
* Flask-Script==2.0.6
* gunicorn==19.7.1
* itsdangerous==0.24
* Jinja2==2.10
* Mako==1.0.7
* markdown-generator==0.1.3
* MarkupSafe==1.0
* pymongo==3.6.1
* python-dateutil==2.6.1
* python-editor==1.0.3
* six==1.11.0
* Werkzeug==0.14.1
* write-me==1.0

### Getting Started
---
##### *Prerequisites*
* [python (3.6+)](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/)
* [git](https://git-scm.com/)

##### *Installation*
First, clone the project repo from Github. Then, change directories into the cloned repository. To accomplish this, execute these commands:

`$ git clone https://github.com/markreynoso/local-music-api.git`

`$ cd local-music-api`

Now now that you have cloned your repo and changed directories into the project, create a virtual environment named "ENV", and install the project requirements into your VE.

`$ python3 -m venv ENV`

`$ source ENV/bin/activate`

`$ pip install -r requirements.txt`
##### *Serving Locally*
Once you have cloned the application and installed the requirements, you can serve the project on your local machine by executing this command from your terminal, on the same level as `run.py`.
`$ flask run`
Once you have executed this command open your browser, and go to `locahost:5000/`.
### Test Suite
---
##### *Running Tests*
This application uses [unittest](https://docs.python.org/3/library/unittest.html) as a testing suite. To run tests, run:

``$ python3 -m unittest``

To view test coverage, run:

``$ coverage report -m``
##### *Test Files*
The testing files for this project are:

| File Name | Description |
|:---:|:---:|
| `./tests/test_local-music-api.py` | Test local music api. |

### URLs
---
The URLS for this project can be found in the following modules:

| URL module | Description |
|:---:|:---:|
| /api/bands | Return full database list of bands. |
| /api/bands/search? | Return band with search name, if exists.<br>To search, use `name={search name}`.<br>Will only return exact match. |
| /api/bands/match? | Return list of bands matching your style(s) preference.<br>To match styles, use `styles={style}` for single and to add styles separate with underscore `_`,<br>i.e. `styles={style1}_{style2}`.<br>Will return a list of bands with matching styles. |


### Development Tools
---
* *python* - programming language
* *flask* - web framework
* *mongodb* - nosql database

### License
---
This project is licensed under MIT License - see the LICENSE.md file for details.
### Acknowledgements
---
* Coffee
* [Bandcamp.com](https://www.bandcamp.com) - initial population of database was procured by scraping all bands identified in the Pacific Northwest region. 

*This README was generated using [writeme.](https://github.com/chelseadole/write-me)*
