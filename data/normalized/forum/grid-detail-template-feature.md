# Grid Detail Template feature

## Question

**PerPer** asked on 29 Apr 2021

Are there any plans to support the equivalent of ASP.Net Core Grid Detail Template in UI for Blazor? Detail template in ASP.NET Core Grid Component Demo | Telerik UI for ASP.NET Core

## Answer

**Marin Bratanov** answered on 30 Apr 2021

Hello Per, This feature has been supported for quite some time, here are its demo and documentation: live demo: [https://demos.telerik.com/blazor-ui/grid/hierarchy](https://demos.telerik.com/blazor-ui/grid/hierarchy) documentation page: [https://docs.telerik.com/blazor-ui/components/grid/hierarchy](https://docs.telerik.com/blazor-ui/components/grid/hierarchy) You may also find interesting the following sample project on loading data for the hierarchy (detail template) on demand only when it expands: [https://github.com/telerik/blazor-ui/tree/master/grid/load-on-demand-hierarchy](https://github.com/telerik/blazor-ui/tree/master/grid/load-on-demand-hierarchy) Regards, Marin Bratanov

### Response

**Gary** commented on 20 Jul 2021

Is it possible to get that tab on a nested grid in Blazor, like the ASP.net core example? Just in general what components would I use in the details template?

### Response

**Marin Bratanov** commented on 20 Jul 2021

You can use the TabStrip, Gary: [https://demos.telerik.com/blazor-ui/tabstrip/overview,](https://demos.telerik.com/blazor-ui/tabstrip/overview,) the asp.net core demo uses a telerik tab strip component inside the detail template too.
