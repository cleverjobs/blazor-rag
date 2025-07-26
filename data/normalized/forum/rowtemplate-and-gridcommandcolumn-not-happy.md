# RowTemplate and GridCommandColumn not happy

## Question

**EdEd** asked on 29 Dec 2019

Hi, I am trying to use a row template as show below. However, the command buttons never show. What am I missing? Thanks ... Ed <RowTemplate Context="ctx"> <td> <strong>@ctxName</strong> </td> <td> <strong>@ctx.Number</strong> </td> @for (int i=0; i <14; i++) { <td> somedata </td> } <td> @* this is where the grid command buttons are supposed to show *@</td> @* . . . *@<GridColumns> <GridColumn Field="Name" Title="Room Type" Width="150px" Resizable="true" /> <GridColumn Field="Number" Title="Room" Width="70px" Resizable="true" /> @foreach (var item in Data) { <GridColumn Field="@item.Name" Title="@item.Title" Width="70px" Resizable="true"> </GridColumn> } <GridCommandColumn Width="300px"> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton OnClick="@((args)=> SelectDashboardModel(args.Item as DataModel))" Icon="edit"> Edit </GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns>

## Answer

**Ed** answered on 29 Dec 2019

Sorry, this was asked and answered before. Never mind.

### Response

**Marin Bratanov** answered on 30 Dec 2019

Hi Ed, To provide some information for someone else finding this thread - the row template takes the row rendering entirely away from the grid, so it removes a lot of built-in functionality, editing being part of that: [https://docs.telerik.com/blazor-ui/components/grid/templates#row-template](https://docs.telerik.com/blazor-ui/components/grid/templates#row-template) Perhaps the following feature will allow you to add buttons that will do something out of the box, but that is subject to research and implementation first: [https://feedback.telerik.com/blazor/1422740-conditional-command-buttons-shown-on-condition-based-on-model-values-and-or-invoking-cud-operations-programmatically.](https://feedback.telerik.com/blazor/1422740-conditional-command-buttons-shown-on-condition-based-on-model-values-and-or-invoking-cud-operations-programmatically.) In the meantime, you should implement editing on your own inside templates, and there are two main approaches you can take: a field in the model that lets you toggle the rendered content to show editors based on a generic button click (another generic button can delete, neither has to be a CommandButton from the grid) generic buttons can employ an external editor, here are two examples (both use command buttons, but they don't have to, you need the Click handler and the current model only): [https://demos.telerik.com/blazor-ui/grid/editing-custom-form](https://demos.telerik.com/blazor-ui/grid/editing-custom-form) and [https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form](https://github.com/telerik/blazor-ui/tree/master/grid/custom-popup-form) Regards, Marin Bratanov
