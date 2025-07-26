# Is it possible to use asp.net core controls in Blazor project?

## Question

**Pin** asked on 06 Jan 2022

Hi, Would it be feasible to bring in the Telerik asp.net core package to a blazor project and use that as well? I know using the controls will obviously be different, but there are more available there so was wondering if I could do that to widen the possibilities? Is there any documentation on how to best go abut doing this if so?

## Answer

**Dimo** answered on 07 Jan 2022

Hi Matthew, Our ASP.NET Core components wrap our Kendo UI jQuery widgets. It is possible to wrap the Kendo UI widgets in Razor components. It requires extra effort to setup and there is no proper Blazor framework integration. Still, it can be a workaround if you really need a component that our Blazor suite still doesn't have. Regards, Dimo
