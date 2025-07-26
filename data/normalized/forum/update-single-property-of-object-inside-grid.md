# Update single property of object inside grid

## Question

**WimWim** asked on 27 Feb 2023

Hi, I'm using onread to fetch odata from a backend system. I also have signalR setup that listens for changes on the objects in the list. I would like to be able to update a single property of an object when an signalr event is received. I'm aware of the Rebind() method, but this forces the entire list to be loaded again. Since i have a lot of events firing and multiple clients, it would make more sense if i could get the objects from the gridref.Data property and update only the affected record and property. Think of this as a grid as a stock-ticker overview, where values are updated very frequently. Do we have a solution for this? Wim

## Answer

**Dimo** answered on 02 Mar 2023

Hi Wim, Updating a single property in a complex object is not straight-forward in Blazor due to the way parameter changes are tracked. What the Grid basically does, is react to changes in its parameters and render the new data collection as table rows in a loop. From this point on, we rely on the Blazor framework diffing algorithm to update the UI. Fewer UI updates can occur if the Grid is databound via Data parameter, compared to refreshing with OnRead handler. In this case, Blazor is able to distinguish persisting data item object instances. On the other hand, OnRead usually produces completely new data item object instances, leading to a complete refresh. Perhaps you can consider switching from OnRead to Data binding if this will help you achieve the desired optimization. Alternatively: Throttle the Grid updates a bit. Experiment with custom data binding inside the OnRead handler. For example, implement some local caching of the old data and when the new data arrives, find and modify the appropriate data item values. Then, set args.Data to the modified cached collection instead of the new DataSourceResult.Data collection. Regards, Dimo Progress Telerik
