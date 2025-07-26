# server paging (onread) search leads to linq to EF query transtale error

## Question

**Ale** asked on 05 Oct 2022

grid configuration OnRead="@Service.ReadComponents" TItem="@ComponentModel" Resizable="true" SelectionMode="GridSelectionMode.Single" FilterMode="@GridFilterMode.FilterMenu" EditMode="@GridEditMode.Inline" Height="100%" Pageable="true" Sortable="true" Groupable="false" SortMode="@SortMode.Single" @bind-Page="@Service.GridPageIndex" PageSize="@Service.GridPageSize" PageSizeChanged="@Service.PagerPageSizeChanged" OnUpdate="@Service.UpdateComponentAsync" OnCreate="@Service.CreateComponentAsync" @ref="@Grid"> if use grid filter, the server-side query is completed successfully: "skip": 0,
"page": 1,
"pageSize": 20000,
"sorts": [],
"filters": [
{
"logicalOperator": 0,
"filterDescriptors": [
{
"member": "VersionName",
"operator": 8,
"value": "test"
}
]
}
],
"groups": [],
"aggregates": [],
"groupPaging": false if try to use the search: "skip": 0,
"page": 1,
"pageSize": 20000,
"sorts": [],
"filters": [
{
"logicalOperator": 1,
"filterDescriptors": [
{
"member": "ProductName",
"operator": 8,
"value": "test"
},...
"member": "LabHourlyRateCurrency.Value",
"operator": 8,
"value": "test"
}
]
}
],
"groups": [],
"aggregates": [],
"groupPaging": false it leads to The LINQ expression 'DbSet() .Join( inner: DbSet(), outerKeySelector: s=> EF.Property(s, "VersionId"), innerKeySelector: p=> EF.Property(p, "Id"), resultSelector: (o, i)=> new TransparentIdentifier( Outer=o, Inner=i )) .Join( inner: DbSet(), outerKeySelector: s=> EF.Property(s.Inner, "ProductId"), innerKeySelector: p0=> EF.Property(p0, "Id"), resultSelector: (o, i)=> new TransparentIdentifier, Product>( Outer=o, Inner=i )) .Join( inner: DbSet(), outerKeySelector: s=> EF.Property(s.Outer.Outer, "JurisdictionId"), innerKeySelector: a=> EF.Property(a, "Id"), resultSelector: (o, i)=> new TransparentIdentifier, Product>, ApprovalJurisdiction>( Outer=o, Inner=i )) .OrderBy(s=> s.Outer.Inner.Name) .ThenBy(s=> s.Outer.Outer.Inner.Version) .ThenBy(s=> s.Inner.Name) .Where(s=> s.Outer.Inner.Name.ToLower().Contains("2 card") && s.Outer.Outer.Inner.Version.ToLower().Contains("2 card") && s.Outer.Inner.Name.ToLower().Contains("test1") || s.Outer.Outer.Inner.Version.ToLower().Contains("test1") || s.Inner.Name.ToLower().Contains("test1") || s.Outer.Outer.Outer.FileApprovalNumber.ToLower().Contains("test1") || new ProductSubmissionCostModel{ SubmissionId=s.Outer.Outer.Outer.Id, ProductId=s.Outer.Outer.Inner.ProductId, ProductName=s.Outer.Inner.Name, VersionName=s.Outer.Outer.Inner.Version, Jurisdiction=s.Inner.Name, SubmissionDate=s.Outer.Outer.Outer.DateSubmission, FileApprovalNumber=s.Outer.Outer.Outer.FileApprovalNumber } .InvoiceNumber.ToLower().Contains("test1") || new ProductSubmissionCostModel{ SubmissionId=s.Outer.Outer.Outer.Id, ProductId=s.Outer.Outer.Inner.ProductId, ProductName=s.Outer.Inner.Name, VersionName=s.Outer.Outer.Inner.Version, Jurisdiction=s.Inner.Name, SubmissionDate=s.Outer.Outer.Outer.DateSubmission, FileApprovalNumber=s.Outer.Outer.Outer.FileApprovalNumber } .ChargeType.ToLower().Contains("test1") || new ProductSubmissionCostModel{ SubmissionId=s.Outer.Outer.Outer.Id, ProductId=s.Outer.Outer.Inner.ProductId, ProductName=s.Outer.Inner.Name, VersionName=s.Outer.Outer.Inner.Version, Jurisdiction=s.Inner.Name, SubmissionDate=s.Outer.Outer.Outer.DateSubmission, FileApprovalNumber=s.Outer.Outer.Outer.FileApprovalNumber } .LabHourlyRateCurrency.Value.ToLower().Contains("test1"))' could not be translated. Either rewrite the query in a form that can be translated, or switch to client evaluation explicitly by inserting a call to 'AsEnumerable', 'AsAsyncEnumerable', 'ToList', or 'ToListAsync'. See server code: var result=await _mapper.ProjectTo <ComponentModel> (
_corpDbContext.Component
.Include(_=> _.Function))
.OrderBy(_=>_.ComponentIdentifier)
.ToDataSourceResultAsync(request.DataSourceRequest);
return new DataEnvelope <ComponentModel> ()
{
Data=result.Data.Cast <ComponentModel> ().ToList(),
Total=result.Total
}; server Telerik.DataSource version 2.1.1

## Answer

**Svetoslav Dimitrov** answered on 10 Oct 2022

Hello Aleksandr, Can you send me a minimal runnable reproduction so that we can further investigate if this issue stems from the Grid component? I am asking because "The LINQ expression could not be translated" issue is pretty generic and is not pointing me toward anything specific in the Grid. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Aleksandr** commented on 21 Oct 2022

so, as we investigated the problem in the model binding field, ail: Microsoft.AspNetCore.Diagnostics.ExceptionHandlerMiddleware[1]
An unhandled exception has occurred while executing the request.
System.InvalidOperationException: The LINQ expression 'DbSet <Component> ()
.OrderBy(c=> c.ComponentIdentifier)
.LeftJoin(
inner: DbSet <Gfunction> (),
outerKeySelector: c=> EF.Property <string> (c, "FunctionId"),
innerKeySelector: g=> EF.Property <string> (g, "Code"),
resultSelector: (o, i)=> new TransparentIdentifier<Component, Gfunction>(
Outer=o,
Inner=i
))
.Where(c=> (c.Inner ?? new Gfunction()).Code.ToLower()=="i")' **could not be translated.** as a solution, we can flatten the model @Svetoslav Dimitrov is it possible to get the expression generated by ? ToDataSourceResultAsync( request.DataSourceRequest )

### Response

**Aleksandr** commented on 22 Oct 2022

i am just wonder who generate this "c.Inner ?? new Gfunction()).Code.ToLower()=="i"" expression

### Response

**Aleksandr** commented on 22 Oct 2022

seems the problem is in automapper, changed mapping a little bit, now getting The LINQ expression 'DbSet <Component> ()
.OrderBy(c=> c.ComponentIdentifier)
.Where(c=> new ComponentModel{
Id=c.Id,
ComponentIdentifier=c.ComponentIdentifier,
ComponentAttribute1=c.ComponentAttribute1,
CRC16Checksum=c.Crc16checksum,
MD5Hash=c.Md5hash,
Kobetron=c.Kobetron,
Media=c.Media,
Notes=c.Notes,
ImageLocation=c.ImageLocation,
Notif=c.Notif,
UserName=c.UserName,
LastUpdated=(DateTime?)c.LastUpdated
}
.GFunction.Key.ToLower()=="i")' good to know where to dig

### Response

**Aleksandr** commented on 22 Oct 2022

finally made it work
