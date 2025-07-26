# In the Grid it does not filter when the data type in SQL is text

## Question

**oni** asked on 22 Sep 2022

Hello, I am using TelerikGrid with the FilterMode and OnRead property, but when I try to filter by a column that the data type in SQL is Text, it does not bring me results.

## Answer

**Timothy J** answered on 22 Sep 2022

I believe this is more of a SQL Server issue and not a Telerik issue. See stackoverflow issue

### Response

**onivia** commented on 29 Sep 2022

Not quite because it means that the ToDataSourceResultAsync() method of telerik where I query, is not optimized for the text data type. // code DataSourceResult result=await _db.Products.Where(p=> p.CodigoEstado==1) .Include(p=> p.CodigoEstadoNavigation) .Include(p=> p.IdCategoriaProductoNavigation) .ToDataSourceResultAsync(request);

### Response

**Timothy J** commented on 29 Sep 2022

Let me make sure I understand: You are attempting to filter the results on a SQL Server 'text' based column using a DataSourceRequest, correct? You want the method ToDataSourceResultAsync to generate the correct SQL code (eventually) to filter as described above, correct? It looks like you are also using EF, correct?
