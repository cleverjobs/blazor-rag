# Grid, using OnRead with Filter raises exception Serverside in ToDataSourceResult(request)

## Question

**Han** asked on 12 Mar 2024

The exception is only raised when applying a filter , sorting up and down works ok. Using "contains" filter. If I remember correctly, this worked before and I did not change my code AFAIK. Controller side looks like this: [HttpPost]
[SwaggerResponse(StatusCodes.Status200OK)]
[SwaggerResponse(StatusCodes.Status404NotFound)]
[Route(ApiUrlConstants.DataSourceRequestSubUrl)]
public IActionResult DataSourceRequest(string projectIdentifier, [FromBody] DataSourceRequest request)
{
if (!TryGetProject(projectIdentifier, out var project))
return this.NotFoundResult(nameof(projectIdentifier), projectIdentifier);
var collection=GetCollection(project).Select(MapItemTypeToDto);
var resultData=collection.ToDataSourceResult(request);
return Ok(resultData);
} WebUI/Client side OnRead event looks like this (the request is sent to server without any further changes): private async Task ReadItems(GridReadEventArgs args)
{
var dataSourceResult=CollectionClient?.HasValidPath ?? false
? await CollectionClient.DataSourceRequestAsync(args.Request)
: new();
args.Data=dataSourceResult?.Data;
args.Total=dataSourceResult?.Total ?? 0;
} which raises an exception in my API server , log looking like this: fail: Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddleware[1]
An unhandled exception has occurred while executing the request.
System.ArgumentException: Provided expression should have string type (Parameter 'stringExpression')
at Telerik.DataSource.Expressions.ExpressionFactory.LiftStringExpressionToEmpty(Expression stringExpression)
at Telerik.DataSource.Expressions.FilterOperatorExtensions.GenerateToLowerCall(Expression stringExpression, Boolean liftMemberAccess)
at Telerik.DataSource.Expressions.FilterOperatorExtensions.GenerateCaseInsensitiveStringMethodCall(MethodInfo methodInfo, Expression left, Expression right, Boolean liftMemberAccess)
at Telerik.DataSource.Expressions.FilterOperatorExtensions.GenerateContains(Expression left, Expression right, Boolean liftMemberAccess)
at Telerik.DataSource.Expressions.FilterOperatorExtensions.CreateExpression(FilterOperator filterOperator, Expression left, Expression right, Boolean liftMemberAccess)
at Telerik.DataSource.Expressions.FilterDescriptorExpressionBuilder.CreateBodyExpression()
at Telerik.DataSource.FilterDescriptor.CreateFilterExpression(ParameterExpression parameterExpression)
at Telerik.DataSource.FilterDescriptorBase.CreateFilterExpression(Expression instance)
at Telerik.DataSource.Expressions.FilterDescriptorCollectionExpressionBuilder.CreateBodyExpression()
at Telerik.DataSource.CompositeFilterDescriptor.CreateFilterExpression(ParameterExpression parameterExpression)
at Telerik.DataSource.FilterDescriptorBase.CreateFilterExpression(Expression instance)
at Telerik.DataSource.Expressions.FilterDescriptorCollectionExpressionBuilder.CreateBodyExpression()
at Telerik.DataSource.Expressions.FilterExpressionBuilder.CreateFilterExpression()
at Telerik.DataSource.Extensions.QueryableExtensions.Where(IQueryable source, IEnumerable`1 filterDescriptors)
at Telerik.DataSource.Extensions.QueryableExtensions.CreateDataSourceResult[TModel,TResult](IQueryable queryable, DataSourceRequest request, Func`2 selector)
at Telerik.DataSource.Extensions.QueryableExtensions.ToDataSourceResult(IQueryable queryable, DataSourceRequest request)
at Telerik.DataSource.Extensions.QueryableExtensions.ToDataSourceResult(IEnumerable enumerable, DataSourceRequest request)
at SNG.LccNion.API.Controllers.ProjectSubCollectionBaseController`2.DataSourceRequest(String projectIdentifier, DataSourceRequest request) in S:\Sources\LCCNion\Source\SNG.LccNion.API\Controllers\ProjectSubCollectionBaseController.cs:line 85
at lambda_method21(Closure, Object, Object[])
at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.InvokeActionMethodAsync()
at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.Next(State& next, Scope& scope, Object& state, Boolean& isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.InvokeNextActionFilterAsync()
--- End of stack trace from previous location ---
at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.Rethrow(ActionExecutedContextSealed context)
at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.Next(State& next, Scope& scope, Object& state, Boolean& isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ControllerActionInvoker.InvokeInnerFilterAsync()
--- End of stack trace from previous location ---
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker. <InvokeNextResourceFilter> g__Awaited|25_0(ResourceInvoker invoker, Task lastTask, State next, Scope scope, Object state, Boolean isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.Rethrow(ResourceExecutedContextSealed context)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.Next(State& next, Scope& scope, Object& state, Boolean& isCompleted)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker.InvokeFilterPipelineAsync()
--- End of stack trace from previous location ---
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker. <InvokeAsync> g__Logged|17_1(ResourceInvoker invoker)
at Microsoft.AspNetCore.Mvc.Infrastructure.ResourceInvoker. <InvokeAsync> g__Logged|17_1(ResourceInvoker invoker)
at Microsoft.AspNetCore.Routing.EndpointMiddleware. <Invoke> g__AwaitRequestTask|7_0(Endpoint endpoint, Task requestTask, ILogger logger)
at SNG.LccNion.API.JWTAuth.JwtMiddleware.Invoke(HttpContext context, IEnumerable`1 authenticationServices) in S:\Sources\LCCNion\Source\SNG.LccNion.API\StartupConfigs\JWTAuth\JWTMiddleware.cs:line 60
at Microsoft.AspNetCore.Authorization.AuthorizationMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Authentication.AuthenticationMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Session.SessionMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Session.SessionMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Localization.RequestLocalizationMiddleware.Invoke(HttpContext context)
at Microsoft.AspNetCore.Diagnostics.DeveloperExceptionPageMiddlewareImpl.Invoke(HttpContext context) Wich does not really help finding out was the problem is. Sorting on any column works ok. It just seems filtering is broken somehow. Also tried other filter options: "Equals" (no results, no error, even though it should match something), "StartsWith" same error Pretty sure I am doing something wrong, - but what? BTW I have the same trouble using a dropdownlistbox with an OnRead handlerevent. Some version info: Telerik.DataSource v3.0.1 Telerik.UI.for.Blazor 5.1.1 VS 2022, .NET8 TIA, Hans

## Answer

**Hans** answered on 19 Mar 2024

I found the cause and provided solution. The DataSource API controller endpoint looked like this: [ HttpPost ]
[ SwaggerResponse(StatusCodes.Status200OK) ]
[ SwaggerResponse(StatusCodes.Status404NotFound) ]
[ Route(ApiUrlConstants.DataSourceRequestSubUrl) ] public IActionResult DataSourceRequest ( string projectIdentifier, [FromBody] DataSourceRequest request ) { if (!TryGetProject(projectIdentifier, out var project)) return this.NotFoundResult( nameof (projectIdentifier), projectIdentifier); var collection=GetCollection(project).Select(MapItemTypeToDto); var resultData=collection.ToDataSourceResult(request); return Ok(resultData);
} Moving the MapItemTypeToDto from the .Select() into the ToDataSourceResult() call fixed the issue. Probably because MapItemTypeToDto returns an object type rather than a specific type. The working endpoint looks like this: [ HttpPost ]
[ SwaggerResponse(StatusCodes.Status200OK) ]
[ SwaggerResponse(StatusCodes.Status404NotFound) ]
[ Route(ApiUrlConstants.DataSourceRequestSubUrl) ] public IActionResult DataSourceRequest ( string projectIdentifier, [FromBody] DataSourceRequest request ) { if (!TryGetProject(projectIdentifier, out var project)) return this.NotFoundResult( nameof (projectIdentifier), projectIdentifier); var collection=GetCollection(project); var resultData=collection.ToDataSourceResult(request, MapItemTypeToDto); return Ok(resultData);
} I am not sure if the built-in datasource filtering takes place before or after the "MapItemTypeToDto" processing. Anyway, I vaguely remember moving this around for specificatlly this reason, so this also explains why it was working before :s Regards - Hans

### Response

**Dimo** answered on 15 Mar 2024

Hello Hans, This error can occur if you try to filter by a property, which is not a standard .NET primitive type. Since you want to use "contains", then the data item property must be a string. Grid data operations (sorting, filtering, editing and grouping) rely on standard .NET primitive types, which have predictable implementation, API members and behavior. If you are trying to filter by a custom type, this is unfortunately not supported. Sometimes applications use custom types (or structs) that are similar to a standard type, but include some enhancements. In this case, my primary recommendation is to expose a standard primitive property in the Grid model, and set it to the column Field. The new property may have a custom getter or setter that are coupled with the custom type. The other option is to implement custom filtering via OnRead data binding. In the OnRead handler, you won't be able to use the ToDataSourceResult() method for filtering. One option is to strip the filter descriptors from the DataSourceRequest object in the OnRead handler ( args.Request ) and filter the result data manually after the ToDataSourceResult() call. Another way is to skip ToDataSourceResult() completely and implement all data operations with custom code. If you are actually using a standard .NET type and the problem seems to be different, then please provide a runnable example that includes your Grid mode class definition and some dummy data. Regards, Dimo Progress Telerik

### Response

**Hans** commented on 19 Mar 2024

Hi Dimo Creating a minmal example will be quite tedious. So before I get into that, I investigated a little more. // in ExpresssionFactory.cs internal static Expression LiftStringExpressionToEmpty ( Expression stringExpression ) { if (stringExpression.Type !=typeof ( string ))
{ throw new ArgumentException( "Provided expression should have string type", "stringExpression" ); // raises exception here } if (IsNotNullConstantExpression(stringExpression))
{ return stringExpression;
} return Expression.Coalesce(stringExpression, EmptyStringExpression);
} Obviously, this routine expects a `stringExpression.Type` to be `string` but is of type `object` - which makes me suspicious about the serialization/deserialization process. The datasourcerequest is Posted as Json to my API (in a different process), and there it gets to be deserialized. stringexpression looks like this in the debugger - stringExpression {[Dynamic]} System.Linq.Expressions.Expression {System.Linq.Expressions.DynamicExpression1}
+ Arguments Count=1 System.Collections.ObjectModel.ReadOnlyCollection <System.Linq.Expressions.Expression> + Binder {Microsoft.CSharp.RuntimeBinder.CSharpGetMemberBinder} System.Runtime.CompilerServices.CallSiteBinder {Microsoft.CSharp.RuntimeBinder.CSharpGetMemberBinder}
CanReduce true bool
DebugView ".Extension <System.Linq.Expressions.DynamicExpression1> {\r\n .Invoke (.Constant<System.Runtime.CompilerServices.CallSite`1[System.Func`3[System.Runtime.CompilerServices.CallSite,System.Object,System.Object]]>(System.Runtime.CompilerServices.CallSite`1[System.Func`3[System.Runtime.CompilerServices.CallSite,System.Object,System.Object]]).Target)(\r\n .Constant<System.Runtime.CompilerServices.CallSite`1[System.Func`3[System.Runtime.CompilerServices.CallSite,System.Object,System.Object]]>(System.Runtime.CompilerServices.CallSite`1[System.Func`3[System.Runtime.CompilerServices.CallSite,System.Object,System.Object]]),\r\n $item)\r\n}" string
+ DelegateType {Name="Func`3" FullName="System.Func`3[[System.Runtime.CompilerServices.CallSite, System.Linq.Expressions, Version=8.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e],[System.Object, System.Private.CoreLib, Version=8.0.0.0, Culture=neutral, PublicKeyToken=7cec85d7bea7798e]]"} System.Type {System.RuntimeType}
NodeType Dynamic System.Linq.Expressions.ExpressionType
+ System.Linq.Expressions.IArgumentProvider.ArgumentCount '((System.Linq.Expressions.IArgumentProvider)stringExpression).ArgumentCount' threw an exception of type 'System.Diagnostics.UnreachableException' int {System.Diagnostics.UnreachableException}
System.Linq.Expressions.IArgumentProvider.ArgumentCount 1 int
+ Type {Name="Object" FullName="System.Object"} System.Type {System.RuntimeType}
+ _arg0 Count=1 object {System.Collections.ObjectModel.ReadOnlyCollection <System.Linq.Expressions.Expression> }
+ Static members The property that I am trying to filter on is a Dto, and its property `DisplayName` is a read/writable string. Q: Are there some specific JsonEncoder types I need to add to my JsonSerializerOptions ? Thanks for bearing with me.
