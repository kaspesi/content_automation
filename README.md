# Daily News Shorts

Start `mongodb` with `docker-compose up -d --build`

Start `collector` with `python3 collect/main.py`


## Data Ingestion

[Web Scraping](Daily%20News%20Shorts%202c0634dfa4254d6584c2f87811f62235/Web%20Scraping%20220c92dca1714940ad0519a89cbf3ac9.md)

- Probably want to save some structure here so we can clean out the bold axios ‘**Why it matters**’ type of text
- Save text for each article in database
    - Can save in mongodb
    - Can save as text files
        - Format the text
    - Each article includes title, sub sections
    - Bold word leads each subsection
- Article format
    - URL
    - Title
    - Author?

## Data Cleaning

[Data Cleaning](Daily%20News%20Shorts%202c0634dfa4254d6584c2f87811f62235/Data%20Cleaning%202d132caf644d4556a0b0430ce47eb1b7.md)

- Clean the text:  might not need to clean the text I’m typical data science way, once we want to summarize and include initial punctuation
    - Remove links
    - Remove axios phrases:
        - Driving the news
        - Why it matters
        - The big picture
        - Etc

## Text Transformation

Name Ideas:  Daily Note

[https://medium.com/1-hour-blog-series/automatic-text-summarization-made-simpler-using-python-577e7622c57a](https://medium.com/1-hour-blog-series/automatic-text-summarization-made-simpler-using-python-577e7622c57a)

### Paraphrasing

- PARROT library
    - [https://towardsdatascience.com/how-to-paraphrase-text-using-python-73b40a8b7e66](https://towardsdatascience.com/how-to-paraphrase-text-using-python-73b40a8b7e66)

### Summarization:

- Pegasus Model
    - [https://youtu.be/Yo5Hw8aV3vY](https://youtu.be/Yo5Hw8aV3vY)

### Video Creation:

[https://github.com/Zulko/moviepy](https://github.com/Zulko/moviepy)

- Allows creating videos using python
- Need backgrounds
    - Maybe can generate a video using AI image/video generation from text
- Need to break up the

### Uploading Video to Youtube

[https://youtu.be/bMT9ZC9sBzI](https://youtu.be/bMT9ZC9sBzI)

- Need to use YouTube data api
- Need to authenticate using the browser, may need to automate this using selenium if google allows for this.  If not this may have to be done manually
