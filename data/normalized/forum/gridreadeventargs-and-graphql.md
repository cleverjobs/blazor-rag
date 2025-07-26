# GridReadEventArgs and GraphQL

## Question

**RobRob** asked on 09 Nov 2022

I see that there is a Demo page for ASP.NET Core components to bind a Grid component to a GraphQL data source. Is there a version for Telerik UI for Blazor?

## Answer

**Dimo** answered on 11 Nov 2022

Hi Rob, I assume that you are referring to this online demo - Telerik UI for ASP.NET Core Grid GraphQL Service Binding. Unlike our ASP.NET Core components, our Blazor components do not make data requests and expect the application to provide the data. This applies when you bind the Grid with the Data parameter and the OnRead event. If you use OnRead, It is possible to serialize the send the DataSourceRequest object to a remote server, if this will make the task easier. Regards, Dimo
