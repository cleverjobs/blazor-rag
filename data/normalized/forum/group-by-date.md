# Group by date

## Question

**Pet** asked on 07 Jun 2021

Hi, I have some measurement date in a database table: ... public int Number { get; set; } public DateTime Start { get; set; } public long ElapsedTime { get; set; } ... I want make a view similar in the attached image with expandable rows group by the date. In the Viewmodel I add a property to get the Date from Start to support GROUP BY Date: public IQueryable<MeasurementViewModel> GetMeasurements() { var result=_context.Measurement.Select(w=> new MeasurementViewModel { Date=w.Start.Date, Start=w.Start, Number=w.Number, ElapsedTime=w.ElapsedTime, }); ; return result; } What is better to use: Grid with Grouping and aggregat or TreeList? For TreeList I dont have parentID and childID. I think it is possible to calculate it. The standard Grid group example doesn't work: if I drag the Date column to the header only the waiting spinner is shown. A solution for the grid should be: without Text "Drag a column header..." and not changeable by user. The expandable date-header-rows sould show some aggregates per day: Count() and SUM(ElapsedTime). Is that possible? Best regards, Peter

## Answer

**Dimo** answered on 10 Jun 2021

Hello Peter, The described scenario is more suitable for a Grid, rather than a TreeList. This is because the TreeList is designed for hierarchical data and the "group" parents are actual items in the data. In your case, the data is not truly hierarchical and parents do not exist - they are only used to combine items with matching dates. Everything mentioned is possible to implement: To group the Grid by default, configure the Grid State programmatically in the component's OnStateInit event: [https://docs.telerik.com/blazor-ui/components/grid/grouping/overview#group-from-code](https://docs.telerik.com/blazor-ui/components/grid/grouping/overview#group-from-code) [https://docs.telerik.com/blazor-ui/components/grid/state#set-default-initial-state](https://docs.telerik.com/blazor-ui/components/grid/state#set-default-initial-state) To prevent users from ungrouping, use one of the following techniques: Hide the top panel where users drag column headers. In your case, this is the easier and more effective option: <TelerikGrid Class="grouped-grid" /> <style>.grouped-grid>.k-grouping-header { display: none;
} </style> Override user actions that are related to grouping: [https://docs.telerik.com/blazor-ui/knowledge-base/grid-static-group](https://docs.telerik.com/blazor-ui/knowledge-base/grid-static-group) Aggregates can be displayed in the group header or footers. Before you display the aggregates, you need to define them in the Grid declaration. [https://docs.telerik.com/blazor-ui/components/grid/grouping/aggregates](https://docs.telerik.com/blazor-ui/components/grid/grouping/aggregates) Regards, Dimo Progress Telerik

### Response

**Peter** answered on 11 Jun 2021

Hello Dimo, thank you. I try the grouping feature of the grid with hidden top panel . Exists a documentation, which k- classes are used in the Blazor components? The source code would be useful, which is available for Telerik® UI for ASP.NET Core, WinForms but not for Blazor. Regards, Peter

### Response

**Dimo** commented on 14 Jun 2021

Hey, Peter. We plan to provide the UI for Blazor source code in November 2021. I am afraid we don't have extensive documentation for the k-classes. So far the potential benefit does not seem to outweigh the amount of required effort, so we prefer to invest in other documentation tasks. Usually, a developer will need to customize a specific element, so inspecting it in the browser's dev toolbar will reveal the CSS class to work with. On the other hand, we have a comprehensive list with the variables used to compile the themes: [https://github.com/telerik/kendo-themes/blob/develop/docs/customization/variables-overview.md](https://github.com/telerik/kendo-themes/blob/develop/docs/customization/variables-overview.md)
