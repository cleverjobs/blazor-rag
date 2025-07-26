# Grid data from MSSQL Stored Procedure with Entity Framework Core

## Question

**Dan** asked on 19 Sep 2024

Does anyone have some sample code showing how to populate a Telerik Blazor Grid with data from a MSSQL Stored Procedure? I am using a Blazor Server template and have got it populating from a table/class model, but not quite sure of the syntax for populating from a stored proc. I will then want to implement CRUD operations. Any help would be very much appreciated!

## Answer

**Dimo** answered on 20 Sep 2024

Hi Daniel, The Telerik UI components for Blazor don't communicate with databases directly. This is a major difference from the legacy Ajax controls. So, you need to implement your own CRUD service and then use it to populate the Grid or modify items through the Grid OnCreate, OnUpdate and OnDelete events. The exact implementation of the service depends entirely on your preferences and does not include Telerik API. You can follow any relevant online tutorial. Regards, Dimo Progress Telerik

### Response

**Daniel** commented on 30 Sep 2024

Thank you Dimo. I am using Entity Framework to connect and creating a context, models, etc to connect with the Telerik grid successfully. I was just trying to see if there is any example code of an Entity Framework service/API with CRUD for SQL Server. I have found lots of things on YouTube and elsewhere, but if there is something that shows specifically use with Telerik it would be helpful too. Particularly using OnRead to load data from the service/API on page changes etc.

### Response

**Dimo** commented on 30 Sep 2024

When using OnRead, you can benefit from the ToDataSourceResult() extension method, which works with IQueryable and IEnumerable. Alternatively, you can analyze the DataSourceRequest argument in the OnRead handler and implement data operations manually if the extension method cannot serve your purpose.
