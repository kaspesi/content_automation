from dotenv import load_dotenv
from tiktok.collect.tiktok import Tiktok

def main():
    """main routine"""
    url = "https://www.tiktok.com"
    # Starts the collector which collects data asyncronously in a seperate thread
    site = Tiktok(url)
    

if __name__ == '__main__':
    # only needed when running outside of containerized environment
    load_dotenv()
    main()