# Explain ToDataSourceResult

## Question

**Ron** asked on 20 Sep 2022

Hi, I have this code... protected void OnRead ( GridReadEventArgs args ) {
DataTable oDataTable=TiMain.DataSource.ToTable();
DataSourceResult oDataSourceResult=oDataTable.ToDataSourceResult(args.Request);

args.Data=(oDataSourceResult.Data as IEnumerable<Dictionary<string, object>>)
.Select(oRow=> oRow.ToDictionary(
oCell=> oCell.Key,
oCell=> (oCell.Value==DBNull.Value ? null: oCell.Value)
))
.ToList();

args.Total=oDataTable.Rows.Count;
} According to my understanding of the documentation ToDataSourceResult should return only with rows that fit the page. But it always return all - sever hundred - of rows regardless of the current page... Have I missed something?

## Answer

**Tsvetomir** answered on 22 Sep 2022

Hi, Ron, Indeed, the ToDataSourceResult () method is implemented to help with handling the data operations and minimizing the load on the database. It has several overloads that handle different scenarios such as when it is working with DataTable, IEnumerable, and IQueryable. When the ToDataSourceResult() is used over an IQueryable collection, then the query is executed in the database and not all records are withdrawn. However, in the current case, in the first line of code in the OnRead event handler, the ToTable() method is used: DataTable oDataTable=TiMain.DataSource.ToTable(); The documentation of the ToTable() method states that " a new DataTable instance that contains the requested rows and columns". Essentially, this method fetches all of the data items from the respective table. After that when the ToDataSourceResult() method is called, it detects that the data is already present and it only applies paging to the data. We have a dedicated article that explains the usage of the DataSource package as well as several practical examples. What I can recommend is that instead of passing a DataTable, pass an IQueryable collection. This way, the query will be executed in the database and no unnecessary items will be fetched. Regards, Tsvetomir
