# DataSourceRequest.ToODataString not encoding '#' character.

## Question

**Jst** asked on 01 Jul 2021

I'm trying to pass a string containing a '<strong>#</strong>' character to an OData api and DataSourceRequest.ToODataString() is not encoding the character.&nbsp; Is it suppose to?

## Answer

**Svetoslav Dimitrov** answered on 06 Jul 2021

Hello John, The ToODataString() method is used to create the portion of the URI after the base URL. A base URL would be the place location the data resides ("[https://demos.telerik.com/kendo-ui/service-v4/odata/Orders?")](https://demos.telerik.com/kendo-ui/service-v4/odata/Orders?")) and the ToODataString() method creates the QueryOptions which might include the applied filters, sorts, page size, and skipped items. The ToODataString() method would not encode HTML elements such as the <strong> tag as this is not part of the QueryOptions. Could you follow up with some additional details on the need to provide HTML elements to the Data service? Regards, Svetoslav Dimitrov Progress Telerik
