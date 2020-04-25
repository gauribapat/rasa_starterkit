## dissatisfied restaurant search 
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - utter_ask_satisfied
* deny
    - utter_apologize

## satisfied restaurant search 
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - utter_ask_satisfied
* affirm
    - utter_noworries

## question bot
* bot_challenge
  - utter_iamabot
