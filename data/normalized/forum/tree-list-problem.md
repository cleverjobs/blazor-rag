# Tree List problem.

## Question

**Jac** asked on 18 Oct 2022

I Want to programically clear current sellection from Tree List. How to do that? I tried two way binding with SelectedItems but clearing the collection does not clear sellection in the UI... Need help please.

## Answer

**Dimo** answered on 21 Oct 2022

Hello Jacek, Most probably, you need to replace the SelectedItems object reference. So instead of calling.Clear(), assign a new IEnumerable. Regards, Dimo Progress Telerik
