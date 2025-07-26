# New search on Blazor Grid

## Question

**Pau** asked on 24 May 2021

Hi The documentation reads: Fields - a list of string that denotes the fields names that the grid should search in. By default, the grid looks in all string fields in its currently visible columns, and you can define a subset of that. Question 1: Why only string fields? In the Netherlands we have a numeric field which is unique for all persons living in the netherlands, many customers search for people using this number, So now i have to make this fields a string to let the user search on it? Question 2: Lets say i have 2000 records, only 140 records are fetched so far, how is the search working, only on these 140 records? I can imagine that my rest server is called to let me make a query with a where clause based on the entered search value. Eric

## Answer

**Marin Bratanov** answered on 24 May 2021

Hi Eric, You can Follow the implementation of other field types here: [https://feedback.telerik.com/blazor/1485012-allow-searchbox-to-work-with-other-data-types.](https://feedback.telerik.com/blazor/1485012-allow-searchbox-to-work-with-other-data-types.) The thread also explains why it cannot happen right now and what kind of feedback we need to implement it. Feel free to join the discussion. I've also added your Vote to it on your behalf which raises its priority, and clicking the Follow button will send you emails for any status updates (such as when we know which release will have it). The searchbox works with the data the grid has - if you supply all the data, it will work on all the data. If you use OnRead to fetch data on demand, typing in the searchbox will fire OnRead with filter descriptors added for the columns it can affect. Regards, Marin Bratanov Progress Telerik
