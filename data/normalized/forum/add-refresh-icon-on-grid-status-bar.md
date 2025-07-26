# Add Refresh icon on grid status bar

## Question

**Cla** asked on 10 May 2024

In Kendo UI for ASP.NET MVC / JQuery the Grid component has the option to show a refresh icon on bottom bar / pager. In the blazor version i cannot see it. Please add a builtin refresh icon on grid as done in other libraries.

## Answer

**Dimo** answered on 14 May 2024

Hi Claudio, Our Kendo UI jQuery Grid and the ASP.NET MVC Grid make data requests directly. They are more tightly integrated with the application's data layer. On the other hand, our Blazor UI components do not communicate with data services. Instead, the Blazor app should refresh a databound UI component when its data changes. That's why a built-in refresh button doesn't make much sense. If you need users to refresh data manually for some reason, then consider a button that will call the Rebind () method of the Grid. You can place the button in the Grid ToolBar. Regards, Dimo Progress Telerik
