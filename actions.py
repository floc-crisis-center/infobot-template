from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionWelcome(Action):

    def name(self) -> Text:
        return "action_welcome_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_welcome_message")    
        return []

class ActionMainMenu(Action):

    def name(self) -> Text:
        return "action_main_menu_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_main_menu_message")    
        return []        


class ActionMenuOption(Action):

    def name(self) -> Text:
        return "action_menu_option_message"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        option = int(tracker.get_slot("number"))
        maxOptions = int(tracker.get_slot("maxOptions"))

        if option == 0:
            dispatcher.utter_message(template="utter_main_menu_message")
        elif option <= maxOptions:
            tmpl1 = "utter_main_menu_option_" + str(option)
            tmpl2 = tmpl1 + "_d"
            dispatcher.utter_message(template=tmpl1)
            dispatcher.utter_message(template=tmpl2)
        else:
            dispatcher.utter_message(template="utter_sorry")
            dispatcher.utter_message(template="utter_main_menu_message")    

        return []
