# Web Scraping

### Structure:

- Collector
    - Site
        - Article

************************Collector:************************  Collects multiple sites worth of news

**********Site:********** Keeps track of the articles on a site, reads them, and returns to collector

To collect:

- Title
- Category
- Chunk
    - Main body
    - Bullets []
- Images?

Axios bodies vary in structure.  Most are paragraphs with ordered lists, containing information about the 

![Screen Shot 2022-11-15 at 11.27.49 PM.png](Web%20Scraping%20220c92dca1714940ad0519a89cbf3ac9/Screen_Shot_2022-11-15_at_11.27.49_PM.png)

![Screen Shot 2022-11-15 at 11.27.19 PM.png](Web%20Scraping%20220c92dca1714940ad0519a89cbf3ac9/Screen_Shot_2022-11-15_at_11.27.19_PM.png)

![Screen Shot 2022-11-15 at 11.25.54 PM.png](Web%20Scraping%20220c92dca1714940ad0519a89cbf3ac9/Screen_Shot_2022-11-15_at_11.25.54_PM.png)

Need to accumulate the `ul` with each `p` since the content is related.  Lets keep the `ul` bullets text seperate from the `p` text for now, and combine them in the transformation step.

[Chromium Attempt](Web%20Scraping%20220c92dca1714940ad0519a89cbf3ac9/Chromium%20Attempt%209b2285126d0b498aa9e413e305070723.md)