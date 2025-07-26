# Predictable stack layout heights

## Question

**Joe** asked on 30 May 2025

Can you tell me how to get a consistent height for my huge "Create New" button? I expected it to just use the space it needed instead of being 5X the size it is. .gsi-height-32px{
height: 32px !important;
} <TelerikStackLayout Height="100%" Width="100%" Orientation="StackLayoutOrientation.Vertical"> <TelerikButton OnClick="@OnCreate" Class="gsi-width-100pct gsi-height-32px"> Create New </TelerikButton> <TelerikGrid Data=@Patients SelectedItems="SelectedPatients" Pageable=true PageSize="20" Height="100%" SelectionMode=GridSelectionMode.Single SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Person> m)=> OnPatientSelected(m))"> <GridColumns> <GridColumn Field=@nameof(Person.FirstName) Title="First Name" /> <GridColumn Field=@nameof(Person.LastName) Title="Last Name" /> <GridColumn Field=@($ "{ nameof ( Patient )}. { nameof ( Patient.DateOfBirthDisplay )}") Title="Date of Birth" Width="125px" /> <GridColumn Field=@($ "{ nameof ( Patient )}. { nameof ( Patient.GenderDisplay )}") Title="Sex" Width="100px" /> <GridColumn Field=@nameof(Person.LastSessionTimestampDisplay) Title="Last Session" /> </GridColumns> </TelerikGrid> </TelerikStackLayout>

## Answer

**Dimo** answered on 03 Jun 2025

Hello Joel, The Telerik StackLayout component relies on flexbox styles. You can get familiar with the mechanism, then inspect the currently applied styles, and make the desired changes: [https://blazorrepl.telerik.com/mfYUkxvu20rP5lmU35](https://blazorrepl.telerik.com/mfYUkxvu20rP5lmU35) Regards, Dimo Progress Telerik

### Response

**Joel** answered on 27 Jun 2025

Ultimately, I fixed this by switching to the GridLayout. However, I still don't like how the treelist doesn't fill the area: <TelerikGridLayout Class="grid-layout"> <GridLayoutRows> <GridLayoutRow Height="28px" /> <GridLayoutRow /> </GridLayoutRows> <GridLayoutItems> @if (Groups?.Count> 0)
{ <GridLayoutItem Row="1"> <TelerikButton OnClick="@(()=> SetTreeListExpandedItems())" Class="gsi-width-100pct gsi-padding-0"> Expand/Collapse Groups </TelerikButton> </GridLayoutItem> } <GridLayoutItem Row="2"> <TelerikTreeList @ref=@TreeListRef Data="@Groups" SelectedItems="@SelectedGroups" IdField="@nameof(Gsi.Customer.Models.Group.Id)" ParentIdField="@nameof(Gsi.Customer.Models.Group.ParentId)" OnStateInit="((TreeListStateEventArgs<Gsi.Customer.Models.Group> args)=> OnStateInitHandler(args))" Pageable="true" PageSize="10" Sortable="false" SelectionMode="TreeListSelectionMode.Single" FilterMode="@TreeListFilterMode.FilterMenu" SelectedItemsChanged="@((IEnumerable<Gsi.Customer.Models.Group> m)=> OnGroupSelected(m))"> <TreeListColumns> <TreeListColumn Field="Name" Title="Group Filter" Expandable="true"> <Template> @{
var item=context as Gsi.Customer.Models.Group; <img height="32" width="32" src="@item.ImageUrl" /> @item.Name
} </Template> </TreeListColumn> </TreeListColumns> </TelerikTreeList> </GridLayoutItem> </GridLayoutItems> </TelerikGridLayout>

### Response

**Dimo** commented on 30 Jun 2025

The TreeList appears to be missing a Height="100%" setting.
