
# Python Server Code

The libraries I have used are mentioned in the requirements.txt file.


## Steps Involved
1. Cleaning CSV file
2. Adding mapped_industry column to company_info and event_info
3. generated emails for all entities in people_info based on the email_pattern column.
4. Created Industry mappings for possible industries for the companies listed in the company_info.csv file
5. Seeded the database using the csv files and made a table for each file.
6. Wrote down a simple Flask server, having a single request.
7. Created db connection for the llm to access.
8. Did a lot of research on how to use Open Ai for this purpose along with Langchain to help build this application.
## Main Functionalities
I was not able to take out enough time to deploy this on a server for production purpose (and my sincere apologies for that). 

The api listens on a localhost and port 5000 i.e 
http://127.0.0.1:5000/

We have a single request url:
http://127.0.0.1:5000/query

In the body, json is passed in with query as key followed by the question as value. e.g.

```json
{
  "query": "tell events taking place in the next 4 months related to tech industry and not taking place in Singapore"
}

```

By sending a request in this manner you will get a response like this,

```json
{
    "columns": [
        "event_name",
        "event_venue",
        "event_country",
        "event_start_date",
        "event_end_date",
        "event_description",
        "url"
    ],
    "message": "",
    "rows": [
        [
            "2nd Edition of Global Conference on Gynecology & Women's Health",
            "Best Western Plus Hotel & Conference Center",
            "Maryland, USA",
            "Thu, 17 Oct 2024 00:00:00 GMT",
            "Sat, 19 Oct 2024 00:00:00 GMT",
            "The upcoming scientific gathering, \"2nd Edition of Global Conference on Gynecology and Womens Health\" (Gynec 2024), organized by Magnus Group, is set to be a significant event. This Hybrid Event is scheduled to take place during October 17-19, 2024, in Baltimore, Maryland, USA, and virtually.",
            "https://gynecology.magnusconferences.com/"
        ],
        [
            "2nd Edition of Global Conference on Gynecology & Women's Health",
            "Best Western Plus Hotel & Conference Center",
            "Maryland, USA",
            "Thu, 17 Oct 2024 00:00:00 GMT",
            "Sat, 19 Oct 2024 00:00:00 GMT",
            "The upcoming scientific gathering, \"2nd Edition of Global Conference on Gynecology and Womens Health\" (Gynec 2024), organized by Magnus Group, is set to be a significant event. This Hybrid Event is scheduled to take place during October 17-19, 2024, in Baltimore, Maryland, USA, and virtually.",
            "https://gynecology.magnusconferences.com/"
        ],
        [
            "2nd Edition of Global Conference on Gynecology & Women's Health",
            "Best Western Plus Hotel & Conference Center",
            "Maryland, USA",
            "Thu, 17 Oct 2024 00:00:00 GMT",
            "Sat, 19 Oct 2024 00:00:00 GMT",
            "The upcoming scientific gathering, \"2nd Edition of Global Conference on Gynecology and Womens Health\" (Gynec 2024), organized by Magnus Group, is set to be a significant event. This Hybrid Event is scheduled to take place during October 17-19, 2024, in Baltimore, Maryland, USA, and virtually.",
            "https://gynecology.magnusconferences.com/"
        ],
        [
            "2nd Edition of Global Conference on Gynecology & Women's Health",
            "Best Western Plus Hotel & Conference Center",
            "Maryland, USA",
            "Thu, 17 Oct 2024 00:00:00 GMT",
            "Sat, 19 Oct 2024 00:00:00 GMT",
            "The upcoming scientific gathering, \"2nd Edition of Global Conference on Gynecology and Womens Health\" (Gynec 2024), organized by Magnus Group, is set to be a significant event. This Hybrid Event is scheduled to take place during October 17-19, 2024, in Baltimore, Maryland, USA, and virtually.",
            "https://gynecology.magnusconferences.com/"
        ]
    ]
}
```

Moreover, the api will not respond to unrelated questions, eg, if you ask about something irrelevant, like capital of USA, it will respond as follows

```json
//request
{
  "query": "What is the capital of usa"
}
//response
{
    "columns": [],
    "message": "Unrelated Question. Please ask something related to events/companies or people attending them!",
    "rows": []
}

```
## Key Challenges

The backend did consume alot of time. Primarily, cleaning the csv file took alot of effor and making it fit before I could move it to the Postgres database.

Likewise, another challenging task was working on the process of converting natural language to sql using llm and langchain. There was a lot of research involved here. 

I had to write many prompts and provided many examples for the llm itself to give quality responses. 

## Suggested Improvements
This project is very limited in its capabilities, and might not return correct answers in many cases.

If I had more time, further research could be needed to fine tune it. Furthermore, we could also make it flexible for more databases.

I could have also taken some more time out, for implementing other tasks like security, making db connections more flexible etc
