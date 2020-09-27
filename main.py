import requests
import json

class Data:
    def __init__(self):
        self.API_KEY = "tSfm0WZvoS7w"
        self.PROJECT_TOKEN = "tYTa3nJV2TD8"
        self.RUN_TOKEN = "tBE6MT-55cW_"
        self.data = self.getData()

    # returns dictionary {state name : num of cases}
    def getData(self):
        response = requests.get(f'https://www.parsehub.com/api/v2/projects/{self.PROJECT_TOKEN}/last_ready_run/data',
                                params={"api_key": self.API_KEY})
        data = json.loads(response.text)
        states = {}

        # Use data['name'] here because of the way the webscraper information is formatted
        for content in data['name']:
            content['active_cases'] = content['active_cases'].replace(",", "")
            states[content['name']] = int(content['active_cases'])

        return states

    # returns number of active cases for a given state
    def getCases(self, stateName):
        if stateName in self.data:
            return self.data[stateName]

        return "0"

    def sortAlphabetical(self):
        # Will return a dictionary of 50 states
        list_of_states = self.data.keys()

        # List of sorted states
        sorted_states = sorted(list_of_states)
        sorted_dict = {}

        # Adds state and corresponding case count to dict
        for state in sorted_states:
            case_count = self.data.get(state)
            sorted_dict[state] = case_count

        return sorted_dict

    def sortLowToHigh(self):
        # Will return a dictionary of 50 states
        list_of_cases = self.data.values()

        # Flips keys and values into new dictionary
        flipped_dict = {value: key for key, value in self.data.items()}

        # List of sorted cases
        sorted_cases = sorted(list_of_cases)
        sorted_dict = {}

        # Adds case count and corresponding state to dict
        for case in sorted_cases:
            state_name = flipped_dict.get(case)
            sorted_dict[state_name] = case

        return sorted_dict

    def sortHighToLow(self):
        # Will return a dictionary of 50 states
        list_of_cases = self.data.values()

        # Flips keys and values into new dictionary
        flipped_dict = {value: key for key, value in self.data.items()}

        # List of sorted cases
        sorted_cases = sorted(list_of_cases, reverse=True)
        sorted_dict = {}

        # Adds case count and corresponding state to dict
        for case in sorted_cases:
            state_name = flipped_dict.get(case)
            sorted_dict[state_name] = case


        return sorted_dict

stateData = Data()