from django.conf import settings
from urllib.request import urlopen
import json

# Create your views here.
def get_jsonparsed_data(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    return json.loads(data)

def get_quote(ticker):
    url = settings.FML_ROOTURL + "/quote/" + ticker + "?apikey=" + settings.FML_APIKEY
    return get_jsonparsed_data(url)

