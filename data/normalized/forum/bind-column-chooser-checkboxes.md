# Bind Column Chooser checkboxes

## Question

**Lar** asked on 19 Mar 2021

I have clients that want to set preferences on which columns in a grid they want visible/hidden when the app loads. Is there a way to bind the checkbox values in a column chooser to a dataset?

## Answer

**Kristian** answered on 24 Mar 2021

Hello Larry, Visibility of the columns in the grid is captured inside the GridState. If you set a new state, the grid (and the column chooser) will apply it. In the attachments, you can find an example I prepared for you where a static column visibility state is set to the grid when a button is pressed. When you look at the code, you will see that the API allows you to set the columns state by its index. If you have only the column fields, you can use this approach to get the index of each column by its Field - [https://docs.telerik.com/blazor-ui/components/grid/state#get-current-columns-visibility-order-field](https://docs.telerik.com/blazor-ui/components/grid/state#get-current-columns-visibility-order-field) Regards, Kristian Progress Telerik

### Response

**Larry** answered on 24 Mar 2021

Based off of that, I tried setting binding to the Visible property in the columns to bit/boolean values I get from a DB table [ using LINQ to pull the values into a model - something like Visible="@ColumnVisibleModel.ColumnNameFlag" ] and that looks like it set the GridState such that the column chooser's selected/deselected checkboxes matched up with which columns were visible/hidden. Thank you!

### Response

**Larry** answered on 24 Mar 2021

This may be for a separate thread but it goes along with why I started this one. I also want to be able to update whether or not a column is loaded visible or hidden as an end-user checks/unchecks the column chooser, something like this (which breaks the app as it doesn't recognize @onselectionchange (same as @onchange) with an exception "'Telerik.Blazor.Components.GridColumnMenuChooserItem' does not have a property matching the name '[onselectionchange|onchange]'") <GridSettings> <GridColumnMenuSettings Lockable="false" FilterMode="@ColumnMenuFilterMode.FilterMenu"> <GridColumnMenuChooser> <Template> @{ var columns=context.Columns; foreach (var column in columns) { <GridColumnMenuChooserItem Title="@column.DisplayTitle" ColumnId="@column.Id" @onselectionchange="(args=> UpdatePreference(UserLogin, column.Id)"> </GridColumnMenuChooserItem> } } </Template> </GridColumnMenuChooser> </GridColumnMenuSettings> </GridSettings>

### Response

**Kristian** answered on 29 Mar 2021

Hi Larry, GridColumnMenuChooserItem is a custom component and it doesn't expose the same event as the built-in HTML components. The approach you could use here is to track when the state of the grid has changed. To do that, use the EventCallback - OnStateChanged: [https://docs.telerik.com/blazor-ui/components/grid/state#events](https://docs.telerik.com/blazor-ui/components/grid/state#events) This event is called every time when the state of the grid has changed - including change the column visibility from the column chooser. The changes in the column visibility will arrive with PropertyName - ColumnStates. When you handling this event, you should consider that it's possible to receive other changed in the columns as well. For example, if the column is reordered, the same event with PropertyName - ColumnStates will arrive. If you want to filter only changes in the visibility of the columns, you should cache the current columns visibility and check if the new version has changes there. Regards, Kristian Progress Telerik
