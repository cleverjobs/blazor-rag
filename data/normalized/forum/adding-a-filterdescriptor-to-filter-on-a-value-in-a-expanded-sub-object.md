# Adding a filterDescriptor to filter on a value in a expanded sub object?

## Question

**Jst** asked on 22 Mar 2023

I have an odata endpoint that I would like to filter records based on a boolean value in a sub object. How would I go about using FilterDescriptors to create the following bolded Query parameters in my OData call? [http://MyODATAEndPoint/MyRecords?$count=true&](http://MyODATAEndPoint/MyRecords?$count=true&) $expand=Flags($filter=IsCleared ne true)

## Answer

**Nadezhda Tacheva** answered on 24 Mar 2023

Hi John, The creation of an OData query is essentially out of the Grid scope and should be handled by the developer based on the desired information you need to return from the service and display in the Grid. As I understand the scenario, you are trying to create a query based on the filters applied to the Grid. For that purpose, you will need to get the current filters that the user selected. You may use the OnRead event and you can get the applied filter descriptors from the DataSourceRequest object of the event arguments. See example here: [https://docs.telerik.com/blazor-ui/components/grid/manual-operations#get-information-from-the-datasourcerequest.](https://docs.telerik.com/blazor-ui/components/grid/manual-operations#get-information-from-the-datasourcerequest.) Once you know what are the filter descriptors (and even if there are any), you will be able to create the correct query to return the matching results. I hope you will find the above information useful. In case you need any assistance with the general setup of the Gird to consume OData services, you may also take a look at this sample app. Regards, Nadezhda Tacheva
