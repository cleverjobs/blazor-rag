# Grid edit fails when EditMode='Incell' and item type is DynamicObject...

## Question

**Ron** asked on 23 Apr 2023

My grid defined like this: <TelerikGrid TItem="TableItemRowWrapper" EditMode="GridEditMode.Incell" The type TableItemRowWrapper defined like this: public class TableItemRowWrapper: DynamicObject, IDictionary <string, object> When clicking on a cell - and it should go to edit mode - I have this error: Value cannot be null. (Parameter 'property') System.Private.CoreLib at System.ArgumentNullException.Throw(String paramName) at System.Linq.Expressions.Expression.Property(Expression expression, PropertyInfo property) at Telerik.Blazor.Extensions.ReflectionExtensions.GetNestedExpression[TItem](Object item, String field) at Telerik.Blazor.Components.Common.Grid.Cells.TableEditCell`5.get_FieldExpression() at Telerik.Blazor.Components.Grid.GridEditCell`1.BuildRenderTree(RenderTreeBuilder __builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment, Exception& renderFragmentException) Inside GetNestedExpression I can see this: Expression.Property(
expression,
expression.Type.GetPropertyInfo(namePart)
); All this tells me that GetPropertyInfo returns null, but I cannot figure out on what namePart and why...

## Answer

**Svetoslav Dimitrov** answered on 26 Apr 2023

Hello Ron, Is the ExpandoObject nested inside a custom model? If that is the case we have an open bug report for this behavior - Grid does not support ExpandoObject properties nested in a custom model. The behavior of this bug is that the Grid renders the data as expected, but the data operations (such as editing) fail. If this is indeed the behavior you experience you can Vote for that bug report and click the Follow button to receive email notifications on status updates. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Ron Hary** commented on 27 Apr 2023

I do not use ExpandoObject, but DynamicObject...
