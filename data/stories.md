## happy path: back and forth b/w menu options and main menu, and bye
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "1"}
  - action_menu_option_message
* inform{"number": "0"}
  - action_main_menu_message  
* inform{"number": "2"}
  - action_menu_option_message  
* inform{"number": "0"}
  - action_main_menu_message
* goodbye
  - utter_goodbye

## happy path: back and forth b/w menu options and main menu
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "3"}
  - action_menu_option_message
* inform{"number": "0"}
  - action_main_menu_message  
* inform{"number": "1"}
  - action_menu_option_message  
* inform{"number": "0"}
  - action_main_menu_message
* inform{"number": "2"}
  - action_menu_option_message      

## happy path: menu option
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "3"}
  - action_menu_option_message

## happy path: menu option and thanks
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "2"}
  - action_menu_option_message  
* thank
  - utter_you_got_it    

## happy path: menu option and bye
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "3"}
  - action_menu_option_message
* goodbye
  - utter_goodbye 

## happy path: welcome and back to main menu
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "0"}
  - action_main_menu_message

## happy path: welcome and back to main menu and thanks
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "0"}
  - action_main_menu_message
* thank
  - utter_you_got_it    

## happy path: two menu options thank and bye
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "1"}
  - action_menu_option_message
* inform{"number": "4"}
  - action_menu_option_message
* thank
  - utter_you_got_it  
* goodbye
  - utter_goodbye

## happy path: menu option and back to main menu
* greet
  - action_welcome_message
  - action_main_menu_message
* inform{"number": "4"}
  - action_menu_option_message
* inform{"number": "0"}
  - action_main_menu_message    

## say goodbye
* goodbye
  - utter_goodbye
