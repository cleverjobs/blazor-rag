# GridSearchBox - Search Operators like "or", as feature or programmatically?

## Question

**Chr** asked on 17 Oct 2020

Hi, does the GridSearchBox today support search operators, like searching for "USA or UK"? If not, is this a planned feature? Or can I as a developer hook into something like a "onSearch" event and provide my own search logic? Thank you!

## Answer

**Marin Bratanov** answered on 18 Oct 2020

Hello Christian, The Searchbox searches in string fields with the "Contains" operator. You can read more about its behavior in its documentation section: Toolbar Search Box. There are not plans to implement such heuristic searches. If you are looking for such behavior, you can use your own custom textbox in the grid toolbar and handle its string to build filters yourself. You can find example of building filters manually here: Filter From Code. You can also use the OnRead event to see what kind of filter descriptor the searchbox makes by default so you can adopt a similar approach. For example, you could use OnRead anyway to optimize regular data queries, and amend it according to yoru custom search logic. You can see how to see what's in the request here: Get Information From the DataSourceRequest. I suggest you review the core concepts of the manual data source operations article (of which the "get information" section is just a small part) to see how this concept works and how it provides you with great flexibility in defining your data retrieval logic. There are also many more examples linked from the beginning of the article, including ones for remote operations on the server. Regards, Marin Bratanov
