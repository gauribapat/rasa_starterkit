# rasa_starterkit
Starter Code for a Conversational AI bot with Rasa. Developed for EECS 498 (Conversational AI) at the University of Michigan.

## Rasa
Full Documentation can be found at ```https://rasa.com/docs/```

## What's in This Example?
This starter code demonstrates a basic framework for building a restaurant search assistant with a front-end webpage built with Flask.

Files:
- **rasa/data/nlu.md** contains training examples for the NLU model  
- **rasa/data/stories.md** contains training stories for the Core model  
- **rasa/actions.py** contains logic for a RestaurantForm action
- **rasa/config.yml** contains the model configuration
- **rasa/domain.yml** contains the domain of the assistant  
- **rasa/endpoints.yml** contains the webhook configuration for the custom action  
- **rasaApp/** contains code for the Flask server
- **bin/run** script file to start Flask server

### Prerequisites
1. Follow the Rasa Open Source installation guide at ```https://rasa.com/docs/rasa/user-guide/installation/```
2. Pull this starter code from Github


### Train the Rasa Model
```bash
cd rasa
rasa train 
```

### Running the Application

1. Start the Business Logic Server
from the project root:
```bash
chmod +x bin/run 
./bin/run
```

2. Start the Rasa Action Server and the Rasa Server
```bash
cd rasa # in a seperate terminal tab
rasa run 
rasa run actions # in another seperate terminal tab
```

3. Navigate to ```http://localhost:8080```


