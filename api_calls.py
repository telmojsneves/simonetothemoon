import requests
import json


class Calls:

    def all_calls(self, text):

        self.hapiness_measure(text)




    def hapiness_measure(self, text):
        accessKey = '2f30bab0f7ce4bb797b4d54371d44b1f'

        request_url_sentiment = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"

        request_url = "https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0/languages"


        headers = {'Ocp-Apim-Subscription-Key': accessKey}

        body = json.dumps (
            {
                "documents": [
                    {
                    "id": "string",
                    "text": text
                    }
                ]
            }
        )


        r = requests.post(request_url_sentiment, data=body, headers=headers)


        print r.text

        print "\n\n\n"
        print "TODO"

        #Key 1: 2f30bab0f7ce4bb797b4d54371d44b1f
        #Key 2: 2b571d00ca5549afad2734486b9cd611
        #https://westcentralus.api.cognitive.microsoft.com/text/analytics/v2.0
