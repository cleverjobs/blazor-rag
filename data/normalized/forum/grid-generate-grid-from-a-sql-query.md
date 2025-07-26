# Grid: Generate Grid from a SQL-Query

## Question

**Hen** asked on 11 Oct 2024

I would like to display the result of a dynamic SQL query, which therefore cannot be typed, in a grid. I tried it with AutoGenerateColumns=“true”, but it didn't work. I load my data into an IEnumerable<dynamic>. Is there a solution for this ?

## Answer

**Dimo** answered on 15 Oct 2024

Hi Hendrik, Binding the Grid to dynamic data is possible, but with some restrictions and caveats. For example, AutoGenerateColumns cannot be used. Please refer to: Grid Data Binding Scenarios - check the bullet about DataTable and ExpandoObject Regards, Dimo Progress Telerik
