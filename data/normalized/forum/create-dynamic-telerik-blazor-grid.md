# Create dynamic telerik blazor grid

## Question

**Hem** asked on 29 Nov 2023

<GridColumns> @foreach (DataRow column in gridColumnData.Rows ) { <GridColumn Field="@nameof(Person.Age)" Title="@column["columnname"].ToString()" /> } </GridColumns> how can i make Field properties also dynamic without creating object model when i display values without creating model i cant use filter mode it throws unhandled exception?

### Response

**Hemanath** commented on 29 Nov 2023

Is there any possible way to do this

## Answer

**Dimo** answered on 29 Nov 2023

Hello Hemanath, Each databound column must have a Field. If you don't want to define a model class, then please bind the Grid to a DataTable or ExpandoObject. Regards, Dimo Progress Telerik

### Response

**Hemanath** commented on 29 Nov 2023

Hello Dimo, I have tried to bind grid to a ExpandoObject data's are binding but the problem is when i use filtering properties it throws a exception .

### Response

**Hemanath** commented on 30 Nov 2023

Hello Dimo, When i tried to bound Grid to a ExpandoObject or DataTable I can't use filter properties .It throws unhandling Exception error. How to sort out this issue .

### Response

**Dimo** commented on 01 Dec 2023

Hemanath - did you see the Notes section and the second example there?
