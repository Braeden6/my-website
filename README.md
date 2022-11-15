# My Website 
### All hosted on [Microsoft Azure](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/get-started/what-is-azure) 
## Description
This website is a current passion project of mine, Braeden. It started out as a way to show off my resume and coding skills. It has developed into a learning tool and something that I have fun developing in my free time. 

File structure setup for this project:
```bash
website (this repo)
    ├── server (backend repo)
    │   ├── package.json
    │   ├── package-lock.json
    │   ├── Dockerfile.development
    │   ├── Dockerfile
    │   └── Other files ...
    ├── client (frontend repo)
    │   ├── package.json
    │   ├── package-lock.json
    │   ├── Dockerfile
    │   └── Other files ...
    ├── data (check data links)
    │   └── all csv files
    ├── env.py
    ├── docker-compose.yml
    ├── uploadData.py
    └── README.md
```

## Pages
This main portion of this website include: [a main page](https://braedensconsulting.com/), this just the landing page with a short description of me; [my resume](https://braedensconsulting.com/myResume), my most update to date resume; [map explorer](https://braedensconsulting.com/map), you get a world map view and can request data about countries like earthquakes, weather, and more to come; [resume builder](https://braedensconsulting.com/resumeBuilder), build your own resume with my format and save to the database, if logged in. </br>
I am planning to add more ideas as a go.
## Data Links
* [locations.csv](https://developers.google.com/public-data/docs/canonical/countries_csv)
* [earthquakes.csv](https://www.kaggle.com/datasets/usgs/earthquake-database)

# Repos and Technologies
## Frontend
The [Frontend Repository](https://github.com/Braeden6/website-frontend) has two branches, main and development, each with there own CI/CD deployment pipeline. All code edits are push to development, tested with the development test website then merge to main once ready. </br>
### Technologies:
- [React](https://reactjs.org/docs/getting-started.html): library for building user interface
- [Bootstrap](https://react-bootstrap.github.io/): helps with layout and design
- HTML: structure, used mostly in JSX files
- CSS: layout, imported in JSX files
- [Vite](https://vitejs.dev/): frontend tooling (see script dev/build)
- JavaScript: main programming language
- [NPM](https://www.npmjs.com/): package manager
- [Mapbox-gl](https://docs.mapbox.com/help/tutorials/use-mapbox-gl-js-with-react/): used for map in `/map` route
- [MSAL](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-overview): microsoft login system
- [Docker](https://www.docker.com/): container with linux as the OS
## Backend
The [Backend Repository](https://github.com/Braeden6/website-backend) has the same setup as the frontend, two branches and CI/CD deployment pipeline
### Technologies:
- [NPM](https://www.npmjs.com/): package manager
- [MSAL](https://learn.microsoft.com/en-us/azure/active-directory/develop/msal-overview): microsoft login system
- [Express JS](https://expressjs.com/): web framework, GET/POST/DELETE/PUT RESTful api style for HTTP requests
- [Node.js](https://nodejs.org/en/about/): server environment, runs JavaScript
- JavaScript: main programming language
- [Docker](https://www.docker.com/): container with linux as the OS
- [Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/introduction): No SQL database hosted on Azure
