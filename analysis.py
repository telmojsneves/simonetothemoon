from api_calls import Calls


class Analyse:


    def treat_message(text, timestamp):
        calls = Calls()
        calls.all_calls(text)

        print "hello"
