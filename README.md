# rasa_starterkit

### Prerequisites
Follow the Rasa installation guide at ```https://rasa.com/docs/rasa/user-guide/installation/```


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
