from api_calls import Calls


class Analyse:


    def treat_message(self, text, timestamp):
        calls = Calls()
        return calls.all_calls(text)
