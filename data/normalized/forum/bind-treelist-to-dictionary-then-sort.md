# Bind TreeList to Dictionary, Then Sort??

## Question

**TedTed** asked on 07 Jun 2022

Hi, I'm trying to bind the tree list to a list of Dictionary<string. object> objects, where the TreeListColumn.Field equals the key in the Dictionary for that row. This works fine for displaying the data in the tree. However, when I try to set the sorting state by specifying a column name to sort by, I get the following error inside Telerik: Error: System.ArgumentException: Invalid property or field - 'Name' for type: DynamicEntityBase at Telerik.DataSource.Expressions.MemberAccessTokenExtensions.CreateMemberAccessExpression(IMemberAccessToken token, Expression instance) at Telerik.DataSource.Expressions.ExpressionFactory.MakeMemberAccess(Expression instance, String memberName) at Telerik.DataSource.Expressions.ExpressionFactory.MakeMemberAccess(Expression instance, String memberName, Boolean liftMemberAccessToNull) at Telerik.DataSource.Expressions.PropertyAccessExpressionBuilder.CreateMemberAccessExpression() at Telerik.DataSource.Expressions.MemberAccessExpressionBuilderBase.CreateLambdaExpression() at Telerik.DataSource.SortDescriptorCollectionExpressionBuilder.Sort() at Telerik.DataSource.Extensions.QueryableExtensions.Sort(IQueryable source, IEnumerable`1 sortDescriptors) at Telerik.Blazor.Data.TelerikTreeListDataSource`1.SortItems(IEnumerable`1 tree) at Telerik.Blazor.Data.TelerikTreeListDataSource`1.SortItems(IEnumerable`1 tree) at Telerik.Blazor.Data.TelerikTreeListDataSource`1.SortItems(IEnumerable`1 tree) at Telerik.Blazor.Data.TelerikTreeListDataSource`1.SortItems(IEnumerable`1 tree) at Telerik.Blazor.Data.TelerikTreeListDataSource`1.SortTree() at Telerik.Blazor.Data.TelerikTreeListDataSource`1.InitData(IEnumerable`1 sourceData) at Telerik.Blazor.Data.TelerikTreeListDataSource`1.ProcessData(IEnumerable data) at Telerik.Blazor.Components.Common.DataBoundComponent`1.ProcessDataInternal() at Telerik.Blazor.Components.Common.DataBoundComponent`1.OnParametersSetAsync() at Telerik.Blazor.Components.TelerikTreeList`1.OnParametersSetAsync() at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) Is there a work around for this, or can sorting by done by some other method? We want to use a Dictionary since we are dynamically creating the data to bind to instead of hard-coding a specific POCO for each page.

## Answer

**Dimo** answered on 09 Jun 2022

Hello Ted, I guess you have something similar to REPL example - TreeList bound to Dictionary. I need to admit that this scenario is currently not supported (I mean the sorting and filtering), so I created a feature request for Dictionary binding on your behalf. In the meantime, if you must bind to a dynamic object, consider an Expando instead - here is a similar example with a Grid. Regards, Dimo Progress Telerik

### Response

**Ted** commented on 09 Jun 2022

Dimo, Thanks for the reply. FYI, an Expando object does not work either and gives the same error when sorting, I added a test here: [https://blazorrepl.telerik.com/mmOUkjbU35zdKs1D09](https://blazorrepl.telerik.com/mmOUkjbU35zdKs1D09) I feel like this is a bug that needs to be fixed.

### Response

**Dimo** commented on 10 Jun 2022

Ted - you are right. I changed the item type from Feature Request to Bug, and updated the text content. I am sorry for the trouble. It looks like dynamic types are out of the game. I hope you will be able to bind the TreeList to a predefined model type, until we fix the issue.
