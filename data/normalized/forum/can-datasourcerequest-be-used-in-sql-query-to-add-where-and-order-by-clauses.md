# Can DataSourceRequest be used in SQL query to add WHERE and ORDER BY clauses?

## Question

**Adr** asked on 06 May 2021

I have a Telerik Blazor Grid that I want to be able to use built in column filtering, column sort and paging. There is a large amount of data to be displayed in the grid approx. 200,000+ rows hence the need for paging. Ideally I want to do all the filtering, sorting and paging within the SQL query so that the SQL server will do the heavy lifting and only send back the required single page of data based on the applied filters, sorting and page number. I have the Telerik.DataSource.DataSourceRequest object from the grid that contains all the grid state for currently applied filters, sorting and page number, is there a way I can use this object to generate my SQL query e.g. create the WHERE clause based on the filters and the ORDER BY clause based on the sorting and the page of data based on the page number? I am using ServiceStack OrmLite which is returning an IQueryable from the SQL database then I'm using the extension method .ToDataSourceResultAsync(gridRequest); I seems that the grid state in the gridRequest is happening in memory on the data sent back from the SQL query in the IQueryable object and not on the SQL database. Is there a way I can do the filtering etc on the SQL database within the query rather than in memory? Example: DataSourceResult processedData=null; using ( var db=_dbConnectionFactory.Open())
{
Telerik.DataSource.DataSourceRequest gridRequest=dataSourceRequestWrapper.ToDataSourceRequest(); var q=db.From<PersonTable>().Limit( 0, 100 );

processedData=await db.Select(q).AsQueryable().ToDataSourceResultAsync(gridRequest);

db.Close();
} return processedData; This produces a SQL query like: SELECT TOP 100 "PersonId",
"FirstName",
"Surname",
"Age" FROM "dbo"."PersonTable" Ideally with using the extension method .ToDataSourceResultAsync(gridRequest); I would like to see the SQL query look more like based on the grid being sorted by the Age column descending and a single text filter applied to the Surname column to filter on 'Smith': SELECT TOP 100 "PersonId",
"FirstName",
"Surname",
"Age" FROM "dbo"."PersonTable" WHERE "Surname" LIKE 'Smith%' ORDER BY "Age" DESC

## Answer

**Marin Bratanov** answered on 06 May 2021

Hi Adrian, The .ToDataSourceResult extension method generates a LINQ query and it is up to the underlying data source to implement the actual SQL query from it. For example, EntityFramework uses that LINQ query we do on its IQueriable to generate a succesful SQL query. It is up to the backend you are using to make that translation and if you are not happy with the results you get, you can always extract the information from the DataSourceRequest object and make the queries yourself, instead of using the .ToDataSourceResult method. I suspect that the thing that might be throwing off your app is the .AsQueryable() method call. In the sample projects we made it it used to showcase that the Telerik extension method supports IQueriable collections, but it is important that the app does not materialize that collection before the query runs. If the db.Select(q) materializes the data, you won't get the benefits of the real SQL operation. Regards, Marin Bratanov

### Response

**Adrian** answered on 07 May 2021

You are correct the data is being materialized too soon, it appears the ServiceStack OrmLite doesn't support IQueriable. We are heavily invested in OrmLite on this project and don't want to move to EF Core, so have decided to hand roll our own filtering, sorting and paging by generating the SQL queries ourselves. Based on this post: [https://www.telerik.com/forums/converting-datasourcerequest-filters-to-sqlserver-parameterized-query-in-controller-read-method](https://www.telerik.com/forums/converting-datasourcerequest-filters-to-sqlserver-parameterized-query-in-controller-read-method) I have managed to create the required queries and it is correctly returning the page of filtered data from SQL Server. However when I try and call .ToDataSourceResultAsync(gridRequest) on the IEnumerable<T> of results which has 100 rows in it the result is a DataSourceResult object where the Data property has zero count of items. Can you give me some suggestions as to why calling this extension method on a fully populated IEnumerable<T> would return 0 items in the resulting object?

### Response

**Marin Bratanov** commented on 07 May 2021

Hi Adrian, I am not in a position to support and investigate such custom implementations and my best guess is that something is different between the case that the original post had and the situation on your end. Perhaps they get a data table and that makes a difference. I also see them calculating the total on their own which is an indication that something is kind of wrong there, or that the .ToDataSourceResult does not work on the entire dataset - the Total calculation generally is a separate query, at least at this point. That said, if you will be performing all the operations yourself in the SQL query, I do not see a reason to use .ToDataSourceResult at all - its purpose is to generate the query for you so the underlying framework will execute it as fast as it can. Now that it has been executed in the database itself, I see no need to repeat it, the result from the database should already have only the current page of records if the query was implemented correctly. If it wasn't - adding more filtering can merely result in the data being even more skewed and wrong. --Marin
