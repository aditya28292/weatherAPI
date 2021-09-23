
# WEATHER API

This Flask project will give json response  with weather data after API call.




## Authors

- [@aditya](https://github.com/aditya28292)

  
## Run Locally

Clone the project

```bash
  git clone https://github.com/aditya28292/weatherAPI weatherAPI
```

Go to the project directory

```bash
  cd weatherAPI
```

Install dependencies

```bash
  pip install flask
  pip install requests
```

Start the server

```bash
  python weatherapimain.py
```
Get the response on postman

    1. Download Postman desktop client and open it.
    2. Create New HTTP Request 
    3. Select GET request and enter api urls as per below
    4. "http://127.0.0.1:5000/weather?city=Boston&country=US&"
    5. city and country are variables. Rest of the syntex is constant. 
        Examples = City: "New York", "Mumbai", "Salta" etc... Country: "us", "in", "ar" etc...
        Please refer to ISO 3166 link below for the city codes or country codes.
    4. Click on Send and check Body in response tab.
    5. Select Pretty for better understanding of response. 
   - [ISO 3166](https://www.iso.org/obp/ui/#search)

Get the response on browser

    1. Open browser and enter api url as given above
    2. Download and add JSONview extension in Chrome browser for better understanding of response.
  
 
## Environment Variables

To run this project, you will need to add the following environment variables to [ENV_VARIABLES] header of env_variable.ini file

`API_KEY`
`BASE_URL`



## Acknowledgements

 - [Awesome platform to get real time accurate weather data](https://openweathermap.org/current)
 
  
