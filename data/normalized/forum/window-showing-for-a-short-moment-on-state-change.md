# Window showing for a short moment on state change

## Question

**Mar** asked on 03 Jun 2022

I have a parent component with a TelerikWindow. The parent component has a bool value that is used via @bind-Visible (two-way binding) to show or hide the TelerikWindow. Once the window was visible (i.e. the bound parameter is set to true), a call to StateHasChanged() causes the window to become visible for a short moment (<1 sec). Since I am using two-way binding at this point, I would expect that hiding the window in both the parent and TelerikWindow components would cause the visibility value to be set to false, so that when StateHasChanged() is called, the window will not become visible again, even for a brief moment.

### Response

**Marin Bratanov** commented on 04 Jun 2022

Does this value come as a parameter from a parent component? Likely, re-rendering takes it from a parent that has not been properly updated. I am not aware of cases when the window won't lower the flag when two-way binding is used, unless the application fails to maintain its own state up the component tree - this is not something the Telerik component can do, as components are encapsulated. If this is not the case, please post a sample in REPL that showcases the issue so we can take a look.
