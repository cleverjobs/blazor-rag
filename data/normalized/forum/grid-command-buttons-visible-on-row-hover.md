# Grid command buttons visible on row hover

## Question

**Dat** asked on 23 Oct 2019

Is it possible to make the grid command buttons visible on mouse hover of the row? Sometimes I feel have a grid full of buttons adds a little unnecessary visual noise.

## Answer

**Marin Bratanov** answered on 24 Oct 2019

Hello Patrick, When the following feature becomes available, you will be able to define your custom buttons with the desired styling: [https://feedback.telerik.com/blazor/1422740-conditional-command-buttons-shown-on-condition-based-on-model-values-and-or-invoking-cud-operations-programmatically.](https://feedback.telerik.com/blazor/1422740-conditional-command-buttons-shown-on-condition-based-on-model-values-and-or-invoking-cud-operations-programmatically.) At the moment, you must have a dedicated column for them anyway, so even if you write a CSS rule that hides them initially the real estate would still be consumed by the column. Nevertheless, here's an example you can start from: <style>.k-grid tbody tr.k-button. OnlyHover { display:none;
}.k-grid tbody tr:hover.k-button. OnlyHover { display:inline-flex;
} </style> <TelerikGrid Data=@MyData EditMode="@GridEditMode.Inline" Pageable="true" Height="500px" OnUpdate="@UpdateHandler" OnEdit="@EditHandler" OnDelete="@DeleteHandler" OnCreate="@CreateHandler" OnCancel="@CancelHandler"> <GridToolBar> <GridCommandButton Command="Add" Icon="add"> Add Employee </GridCommandButton> </GridToolBar> <GridColumns> <GridColumn Field=@nameof(SampleData.ID) Title="ID" Editable="false" /> <GridColumn Field=@nameof(SampleData.Name) Title="Name" /> <GridCommandColumn> <GridCommandButton Class="OnlyHover" Command="Save" Icon="save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Class="OnlyHover" Command="Edit" Icon="edit"> Edit </GridCommandButton> <GridCommandButton Class="OnlyHover" Command="Delete" Icon="delete"> Delete </GridCommandButton> <GridCommandButton Class="OnlyHover" Command="Cancel" Icon="cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> Regards, Marin Bratanov
