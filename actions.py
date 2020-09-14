from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
import random
import requests


class ActionCheckStatus(Action):

    def name(self):
        return "action_check_status"

    def run(self, dispatcher, tracker, domain):
        # return a random status, just a mockup
        statuses = ["received", "rejected", "interview", "unknown"]
        status = random.choice(statuses)
        dispatcher.utter_message("Yes, your application has been "+status+".")
        return [SlotSet("status", status)]


class ActionCheckPositions(Action):

    def name(self):
        return "action_check_positions"

    def run(self, dispatcher, tracker, domain):
        # return hard-coded open positions, this would normally come from an API
        positions = {
            "technical": [
                "machine learning engineer",
                "ML product success engineer"
            ],
            "business": []
        }
        position_type = tracker.get_slot("role_type")
        if position_type == "any":
            relevant_positions = positions["technical"] + positions["business"]
        else:
            relevant_positions = positions.get(position_type, [])

        if len(relevant_positions) > 1:
            position_text = ", ".join(relevant_positions[:-1])
            position_text+=" and "+relevant_positions[-1]+" are the open positions."
        elif len(relevant_positions) == 1:
            position_text = relevant_positions[0] + " is an open posiiton"
        else:
            position_text = "There are no open positions"

        dispatcher.utter_message(position_text)

        return [SlotSet("positions", relevant_positions)]


class ActionGetProfile(Action):

    def name(self):
        return "action_get_profile"

    def run(self, dispatcher, tracker, domain):
        name = tracker.get_slot("PERSON")
        data = 'Name : {}\nAge : 26\nRole : Software Engineer'.format(name)
        dispatcher.utter_message("Employee Profile\n" + str(data))
        return []

