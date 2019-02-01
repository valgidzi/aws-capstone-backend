## teachers' corner API
This is the API for _**teachers' corner**_ - a web app designed to help ESL teachers create lesson materials. It was built with Django, has a PostgreSQL database, and was deployed to AWS. I developed this API for my [capstone project](https://github.com/Ada-C10/capstone) at [Ada Developer's Academy](https://www.adadevelopersacademy.org/), which required learning three new technologies to build and deploy a product in 4 weeks. The repo for the frontend React app can be found [here](https://github.com/valgidzi/capstone-frontend).

### Endpoints
#### Get the learner level for a text:
```
POST /textscore/
```
#### Get the most difficult words from a text:
```
POST /difficultwords/
```
#### Get the learner definitions for a word:
```
GET /definitions/?word=<word>
```
#### Save a handout to the database:
```
POST /handouts/
```
#### List all handouts:
```
GET /handouts/
```
#### Get an individual handout:
```
GET /handouts/:id/
```

### Installation
1. Fork and clone this repo.
2. Create and start a virtual environment. 
3. Install the project dependencies from requirements.txt.
4. Obtain a Django secret key from [MiniWebTool](https://www.miniwebtool.com/django-secret-key-generator/).
5. Obtain an API key from [Macmillan's Learner Dictionary API](https://dictionaryapi.com/products/api-learners-dictionary).
5. Add the Django secret key and the API key to your environment variables.
6. Create a PostgreSQL database and add the credentials to settings.py.
7. Run the migrations, start the development server, and open localhost:8000 in your browser.

### Additional Information
- [Product Plan](https://gist.github.com/valgidzi/e037125c8837582d2210fecd686c9555)
- [Final Presentation](https://docs.google.com/presentation/d/e/2PACX-1vTpgkRBOeK0xTDHuPom7tVmaXhq6Qss1ogIvHlEAFZghKgFtRJ6Ep9M0Un5tplXUoNs0-VTWZDgld-S/pub?start=false&loop=false&delayms=3000)
