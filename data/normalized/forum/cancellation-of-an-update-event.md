# Cancellation of an update event

## Question

**Mau** asked on 08 Jan 2021

I have an update event but how can I tell the grid the update didn't work out and everything has to be cancelled, This code doesn't work. private static async Task MainGridUpdateHandler(GridCommandEventArgs args) { var item=(EmployeeClusterVM) args.Item; if (item.EndDate <=item.StartDate) { args.IsCancelled=true; } try { EmployeeClusterLogic.UpdateEmployeeCluster(item); } catch (Exception e) { args.IsCancelled=true; } }

## Answer

**Marin Bratanov** answered on 08 Jan 2021

Hi Maurice, You can see how that can work here: [https://github.com/telerik/blazor-ui/tree/master/grid/remote-validation.](https://github.com/telerik/blazor-ui/tree/master/grid/remote-validation.) This sample project also shows how you can show such errors to the user. I would also recommend you use the Popup Edit Mode of the grid as it can use DataAnnotations for validation and so this date check can be implemented with a rule there, so the user won't be able to submit an update in the first place. You can find a sample rule to compare dates in the DateRangePicker Validation example. The only issue I can see in the provided snippet is that the method is static, and if it is declared in a component, that could cause issues with accessing it. Regards, Marin Bratanov
