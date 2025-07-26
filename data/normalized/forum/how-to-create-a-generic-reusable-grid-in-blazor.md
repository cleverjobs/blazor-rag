# How to create a generic reusable grid in blazor

## Question

**Hyp** asked on 25 Feb 2024

I attempted to develop a versatile grid component for Blazor to facilitate reusability. @typeparam TItem <TelerikGrid Data="Data" SelectionMode="GridSelectionMode.Multiple" Pageable="true" PageSize="3" Page="1" Sortable="true" SortMode="@SortMode.Multiple" FilterMode="GridFilterMode.FilterMenu" EditMode="@GridEditMode.Popup" Resizable="true" Reorderable="true" ConfirmDelete="true"> <GridSettings> <GridValidationSettings Enabled="true"> </GridValidationSettings> <GridPopupEditSettings MaxWidth="600px" MaxHeight="300px" Class="custom-popup" Title="Update Details"> </GridPopupEditSettings> <GridPopupEditFormSettings Orientation="@FormOrientation.Horizontal" ButtonsLayout="FormButtonsLayout.Center" Columns="3"> </GridPopupEditFormSettings> </GridSettings> <GridToolBarTemplate> <GridCommandButton Command="ExcelExport" Icon="@SvgIcon.FileCsv"> Export to Excel </GridCommandButton> <GridCommandButton Command="Add" Icon="@SvgIcon.Plus"> Add Employee </GridCommandButton> </GridToolBarTemplate> <GridExport> <GridExcelExport FileName="EmployeeDetails Sheet" AllPages="true" /> </GridExport> <GridColumns> @GridCols <GridCommandColumn> <GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil"> Edit </GridCommandButton> <GridCommandButton Command="Delete" Icon="@SvgIcon.Trash"> Delete </GridCommandButton> <GridCommandButton Command="Cancel" Icon="@SvgIcon.Cancel" ShowInEdit="true"> Cancel </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> @code
{
[Parameter]
public IEnumerable <TItem>? Data{get; set;}

[Parameter]
public RenderFragment <TItem>? GridCols { get; set; }

} This is the code for the reusable generic grid component. @page "/emp"
@inject HttpClient Http
@using System.Text.Json; <h1> Employee Details </h1> @if (employees==null)
{ <p> <em> Loading... </em> </p> }
else
{ <GenericGrid TItem="EmpDetails" Data="@employees"> <GridCols> <GridColumn Field="@nameof(EmpDetails.Name)" Title="Employee Name" /> <GridColumn Field="@nameof(EmpDetails.Age)" Title="Age" /> <GridColumn Field="@nameof(EmpDetails.Place)" Title="Place" /> </GridCols> </GenericGrid> } When utilizing the Generic component, the column fields are not being generated as expected. Could someone assist in resolving this issue?

## Answer

**shiva** answered on 16 Apr 2024

As you are wrapping the GridColumn components in GridCols renderfragment, the GridColumn need the grid data to render the rows and the GridCols renderfragment is not passing that data, hence, the rows are not being rendered. Change the code in the following way to fix it: @code
{
[ Parameter ] public IEnumerable<TItem>? Data{ get; set;}

[ Parameter ] public RenderFragment<IEnumerable<TItem>>? GridCols { get; set; } } <GridColumns> @GridCols(Data) <GridCommandColumn> <GridCommandButton Command="Save" Icon="@SvgIcon.Save" ShowInEdit="true"> Update </GridCommandButton> <GridCommandButton Command="Edit" Icon="@SvgIcon.Pencil"> Edit </GridCommandButton> also handle the null checks for Data. Hope this helps.
