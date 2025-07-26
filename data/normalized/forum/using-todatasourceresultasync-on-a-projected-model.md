# Using 'ToDataSourceResultAsync' on a projected model

## Question

**Jer** asked on 06 Mar 2024

Hi, I'm attempting to do something that is probably dumb/unsupported. We have a paginated grid in our UI that we want to include a joined model in. Example: public class Item
{
[Key]
public Guid ItemId{ get; set; }=Guid.NewGuid();
public Guid? LatestLogId { get; set; }
}

public class ItemLog
{
[Key]
public Guid ItemLogId{ get; set; }

public Guid ItemId{ get; set; }
[ForeignKey("ItemId")]
public Item? Item { get; set; }

[MaxLength(250)] public string Message { get; set; }=null!;
} We use 'LatestLogId' in order to know what ItemLog to 'include' in the results in the UI I'm trying to project it into a Dto that includes both the Item and the LatestLog but running into some trouble calling 'ToDataSourceResultAsync' with that IQueryable<Dto> public async Task<DataSourceResult> GetItemReportPage ( DataSourceRequest pageRequest, Guid staffId, bool includeAll=false ) { var baseQuery=_appContext.Items
.AsQueryable(); if (!includeAll)
{
baseQuery=baseQuery.Where(x=> x.CreatedBy==staffId);
} var query=baseQuery.Select(item=> new ItemWithLatestLogDto
{
LatestLog=_appContext.ItemLogs.FirstOrDefault(x=> x.ItemLogId==request.LatestLogId)
})
.AsNoTracking(); var dataSourceResult=await query.ToDataSourceResultAsync(pageRequest); return dataSourceResult;
} When calling that I get an error that is something like this: System.InvalidOperationException: The LINQ expression 'DbSet <Item> ()
.Where(n=> n.CreatedById==__staffId_0)
.OrderByDescending(n=> new ItemWithLatestLogDto{ LatestLog=DbSet <ItemLog> ()
.Where(r=> (Guid?)r.ItemLogId==n.LatestLogId)
.FirstOrDefault() }
.CreatedDateTimeUtc)' could not be translated. Either rewrite the query in a form that can be translated, or switch to client evaluation explicitly by inserting a call to 'AsEnumerable', 'AsAsyncEnumerable', 'ToList', or 'ToListAsync'. See [https://go.microsoft.com/fwlink/?linkid=2101038](https://go.microsoft.com/fwlink/?linkid=2101038) for more information.
at Microsoft.EntityFrameworkCore.Query.QueryableMethodTranslatingExpressionVisitor. <VisitMethodCall> g__CheckTranslated|15_0(ShapedQueryExpression translated, <> c__DisplayClass15_0&)
at Microsoft.EntityFrameworkCore.Query.QueryableMethodTranslatingExpressionVisitor.VisitMethodCall(MethodCallExpression methodCallExpression)
at Microsoft.EntityFrameworkCore.Query.RelationalQueryableMethodTranslatingExpressionVisitor.VisitMethodCall(MethodCallExpression methodCallExpression)
at Microsoft.EntityFrameworkCore.Query.QueryableMethodTranslatingExpressionVisitor.VisitMethodCall(MethodCallExpression methodCallExpression)
at Microsoft.EntityFrameworkCore.Query.RelationalQueryableMethodTranslatingExpressionVisitor.VisitMethodCall(MethodCallExpression methodCallExpression)
at Microsoft.EntityFrameworkCore.Query.QueryableMethodTranslatingExpressionVisitor.VisitMethodCall(MethodCallExpression methodCallExpression)
at Microsoft.EntityFrameworkCore.Query.RelationalQueryableMethodTranslatingExpressionVisitor.VisitMethodCall(MethodCallExpression methodCallExpression)
at Microsoft.EntityFrameworkCore.Query.QueryableMethodTranslatingExpressionVisitor.VisitMethodCall(MethodCallExpression methodCallExpression)
at Microsoft.EntityFrameworkCore.Query.RelationalQueryableMethodTranslatingExpressionVisitor.VisitMethodCall(MethodCallExpression methodCallExpression)
at Microsoft.EntityFrameworkCore.Query.QueryCompilationContext.CreateQueryExecutor[TResult](Expression query)
at Microsoft.EntityFrameworkCore.Storage.Database.CompileQuery[TResult](Expression query, Boolean async)
at Microsoft.EntityFrameworkCore.Query.Internal.QueryCompiler.CompileQueryCore[TResult](IDatabase database, Expression query, IModel model, Boolean async)
at Microsoft.EntityFrameworkCore.Query.Internal.QueryCompiler. <> c__DisplayClass9_0`1. <Execute> b__0()
at Microsoft.EntityFrameworkCore.Query.Internal.CompiledQueryCache.GetOrAddQuery[TResult](Object cacheKey, Func`1 compiler)
at Microsoft.EntityFrameworkCore.Query.Internal.QueryCompiler.Execute[TResult](Expression query)
at Microsoft.EntityFrameworkCore.Query.Internal.EntityQueryProvider.Execute[TResult](Expression expression)
at Microsoft.EntityFrameworkCore.Query.Internal.EntityQueryable`1.System.Collections.IEnumerable.GetEnumerator()
at Telerik.DataSource.Extensions.QueryableExtensions.Execute[TModel,TResult](IQueryable source, Func`2 selector)
at Telerik.DataSource.Extensions.QueryableExtensions.CreateDataSourceResult[TModel,TResult](IQueryable queryable, DataSourceRequest request, Func`2 selector)
at Telerik.DataSource.Extensions.QueryableExtensions.ToDataSourceResult(IQueryable queryable, DataSourceRequest request) The Dto looks like this: public class ItemWithLatestLogDto: Item { public ItemLog? LatestLog { get; set; } public NewFileRequestWithLatestLogDto () {
}
} Is this a use-case supported by the method or do I need to find a different way of accomplishing this? Thanks!

### Response

**Workx** commented on 31 May 2024

Did you find a solution?

## Answer

**Svetoslav Dimitrov** answered on 11 Mar 2024

Hello Jeremy, The first thing you can try is to move the call to the DataSourceResultAsync method above the Select(). If this does not resolve the issue, you can try removing the AsNoTracking() method and see if that makes a difference. Regards, Svetoslav Dimitrov Progress Telerik
