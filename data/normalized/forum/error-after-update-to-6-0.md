# Error after Update to 6.0

## Question

**Hen** asked on 24 May 2024

Right from the start I get following errors in den Dircect Window: System.ArgumentNullException: Value cannot be null. (Parameter 'nullableType') at System.ArgumentNullException.Throw(String paramName) at System.Nullable.GetUnderlyingType(Type nullableType) at Telerik.Blazor.Common.Filter.FilterOperatorFactory.GetFilterOperatorsForType(Type type, ITelerikStringLocalizer localizer) at Telerik.Blazor.Components.Common.BoundColumnBase.ThrowIfInvalidDefaultFilterOperator() at Telerik.Blazor.Components.Common.BoundColumnBase.OnParametersSet() at Microsoft.AspNetCore.Components.ComponentBase.CallOnParametersSetAsync() at Microsoft.AspNetCore.Components.ComponentBase.RunInitAndSetParametersAsync() at Telerik.Blazor.Components.Common.ColumnBase.SetParametersAsync(ParameterView parameters) I can not load any Grid anymore. The error shows: System.ArgumentNullException Value cannot be null. (Parameter 'nullableType') I think it has something to do with "DefaultFilterOperator" but I cannot figure out it myself With 5.1.1 everything works just fine.

### Response

**Nadezhda Tacheva** commented on 27 May 2024

Hi Hendrik, We haven't received reports for such an issue so far. To move forward with the investigation, please provide an isolated runnable sample that reproduces the problem. This will allow me to debug it and find the root cause. Thank you in advance for your cooperation!

### Response

**Ryan** commented on 28 May 2024

I am experiencing the same issue on several, but not all grids since the upgrade. It goes away when I change the filter mode to None... obviously not what I want to do...

### Response

**Nadezhda Tacheva** commented on 31 May 2024

Hi Ryan, Can you provide a minimal reproducible example, so we can debug this? You may include some dummy data and mimic your exact Grid configuration.

### Response

**Daniel** commented on 05 Jun 2024

Hi, the same for us. Had to step back to v5.1.1... Any ideas what the problem might be?

### Response

**David** commented on 05 Jun 2024

I am getting the same issue on one of the grids in our Blazor WASM app, after upgrade. Error goes away if I set FilterMode to None, which is not a fix

### Response

**Nadezhda Tacheva** commented on 06 Jun 2024

Hi all, I am not able to confirm the root cause without a reproduction but I suspect the issue may be related to a regression that we had in 6.0.0 related to filtering nullable types. It has been fixed and we released a patch version a couple of days ago. Can you please upgrade to 6.0.2 and test again? If the issue persists, please provide an isolated sample that reproduces it, so we can investigate further.

### Response

**Hendrik** commented on 06 Jun 2024

With 6.0.2 it is still not working...

## Answer

**Michael** answered on 07 Jun 2024

It seems like this issue is caused when there is a GridColumn with parameter "Field" set to a value that is not a property of the grid item model. Before 6.0.0 this was possible and did not cause an exception. I have created a small example that lets you reproduce the error. To reproduce just let the unit test run for one of the configurations v5 or v6. With v5 the test succeeds, with v6 it does not. I hope this helps to fix the issue.

### Response

**David** commented on 07 Jun 2024

Looks like it fixed the issue for me

### Response

**Hendrik** commented on 09 Jun 2024

Thank you very much ! That fixed the problem !

### Response

**Nadezhda Tacheva** answered on 11 Jun 2024

Hi all, Thank you very much for your cooperation! The behavior is caused by a regression in the Grid that you may track here: [Regression] Filterable Grid throws if a column field is not bound to a field from the model. The workaround I'd suggest is to set the FieldType of the column. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Amanullah** commented on 04 Jul 2024

Hi, We tried to set Filterable="true" for a column field that is not bound to a field from the model and getting "An unhandled error has occurred.Reload". We are using following example: [https://blazorrepl.telerik.com/wSugvFui10jhcpZy00](https://blazorrepl.telerik.com/wSugvFui10jhcpZy00)

### Response

**Nadezhda Tacheva** commented on 08 Jul 2024

Hi Amanullah, The "test" column in this example is not bound to a field of the model that the Grid uses, so the Grid cannot filter it out of the box. That said, this column should either have Filterable="false " or you should implement your custom approach for filtering the custom data in it. The issue discussed in this thread is that even if the column is not filterable (has Filterable="false "), the Grid still throws and this is the case that the linked regression will cover.
