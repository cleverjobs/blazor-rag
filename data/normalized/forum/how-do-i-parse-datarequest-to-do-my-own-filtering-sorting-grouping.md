# How do I parse DataRequest to do my own filtering/sorting/grouping

## Question

**Joh** asked on 03 Aug 2021

I do NOT wish to expose my database structures to front-end clients of my API. I use flattened Data Transfer Objects (DTO) to communicate between client and server. So, I want to use the DataRequest pieces to generate my own queries against the database to retrieve the data, I see no harm in using Data Transfer Objects (DTO) in returning a DataResponse object. That is way more manual than your code samples or documentation shows. Can you point me to information about parsing filters, sort orders, paging, no grouping (thankfully). I'll take it from there. Oh, is there a decoupled control for building filters that could be applied to a grid? It seems the only two options are Menu or Row. It would seem a decoupled filter control would be terrific for saving a filter configuration as well.

## Answer

**Marin Bratanov** answered on 03 Aug 2021

Hi John, The following samples show how you can take the DataSourceRequest object the grid provides and send it (serialized) to an endpoint, that can work with it, and then return the required data: [https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server.](https://github.com/telerik/blazor-ui/tree/master/grid/datasourcerequest-on-server.) I hope it can serve as a good base for you to start your own implementation from. Perhaps you can even use it as-is because it does not require that you expose any of your database logic through the API, ultimately a collection of models gets serialized back to the client (a bit more complex with grouping, but still the same concept). You can also check the "Get Information From the DataSourceRequest" section from this article for a basic example on taking info out of the object to do with as you please: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations.) As for a separate Filter component - you can Follow its implementation here: [https://feedback.telerik.com/blazor/1445600-filter-component,](https://feedback.telerik.com/blazor/1445600-filter-component,) but I expect it will produce an event and a DataSourceRequest object so you can choose how to use them to update your view-model (much like OnRead does for the grid now). If you would still be interested in that, click the Vote and Follow buttons. Regards, Marin Bratanov
