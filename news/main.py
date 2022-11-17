from dotenv import load_dotenv
from collect.collector import Collector

def main():
    """main routine"""
    url = "https://www.axios.com"
    # Starts the collector which collects data asyncronously in a seperate thread
    collectors = [ Collector(url) ]

if __name__ == '__main__':
    # only needed when running outside of containerized environment
    load_dotenv()
    main()