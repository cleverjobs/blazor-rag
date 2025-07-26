# Dynamically build list of FilterFields based on data source

## Question

**Bil** asked on 22 May 2023

Is it possible to dynamically build the list of FilterFields for a TelerikFilter based on search field data stored in a database? We have complicated nested JSON to search through and so normal IQueryable operations aren't quite yet available to us, we will have to do some massaging of the DataSourceRequests either client or server-side.

## Answer

**Bill** answered on 25 May 2023

For future reference, here's an example of how it was done (including an answer to an issue with filter operators not changing): [https://www.telerik.com/forums/filter-operations-not-changing-by-type-for-dynamically-built-filter-fields](https://www.telerik.com/forums/filter-operations-not-changing-by-type-for-dynamically-built-filter-fields)

### Response

**Bill** answered on 22 May 2023

I realize now how silly this question is in Blazor- just @foreach and loop through to build the list
