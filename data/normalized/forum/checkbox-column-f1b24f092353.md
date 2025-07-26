# checkbox column

## Question

**Ran** asked on 16 Oct 2019

Hi, I am trying to do something simple but having trouble. All I want is a grid that displays columns for a name and an IsActive property. I tried using: <GridCheckboxColumn Field="@(nameof(AppRole.IsActive))" Title="Is Active"/> but got nowhere with it. The basic code is show below. How can I center the checkbox in the column and make not editable unless the are in edit mode? Also, I want the checkboxes centered in the column. Any help would be great. Thanks ... Ed <TelerikGrid Data=@GridData Pageable="true" Groupable="true" Sortable="true" OnUpdate="@UpdateHandler" OnDelete="@DeleteHandler" OnCreate="@CreateHandler" OnEdit="@EditHandler"> <GridColumns> <GridColumn Field="Name" /> <GridColumn Field="@(nameof(AppRole.IsActive))" Title="Is Active"> <Template Context="ctx"> @{ var r=ctx as AppRole; var chk=r.IsActive ? "checked" : ""; <input type="checkbox" checked="@chk" /> } </Template> </GridColumn> <GridCommandColumn Width="300px"> <GridCommandButton Command="Save" Icon="save" ShowInEdit="true">Update</GridCommandButton> <GridCommandButton Command="Edit" Icon="edit">Edit</GridCommandButton> <GridCommandButton Command="Delete" Icon="delete">Delete</GridCommandButton> <GridCommandButton Command="Cancel" Icon="cancel" ShowInEdit="true">Cancel</GridCommandButton> </GridCommandColumn> </GridColumns> <GridToolBar> <GridCommandButton Command="Add" Icon="add">Create Role</GridCommandButton> </GridToolBar> </TelerikGrid>

## Answer

**Marin Bratanov** answered on 16 Oct 2019

Hi Ed, The GridCheckboxColumn is used only for row selection, not for data binding/display. To display and edit boolean data, you need to use the standard GridColumn. When bound to a boolean field, it displays True/False as text by default (example here ) and if you want something different, you need to use a template, as you have found. If you want to center the contents, add a div element around your custom checkbox and style those two elements as desired. To prevent editing, simply disable the checkbox in the Template. Regards, Marin Bratanov

### Response

**Coen** answered on 22 Jul 2020

Just a note on the template. I found out that the next code works better to set the value of the checkbox in the grid: @{ var r=ctx as AppRole; <input type="checkbox" disabled @bind=r.IsActive /> }

### Response

**Jonathan** answered on 06 Oct 2020

Hi What does the template code look like ? thx

### Response

**Steve** commented on 08 Sep 2021

Here's what I did recently: <GridColumn Width="50px" Field="@(nameof(PicklistValueInfo.IsActive))" Title="Active"> <Template Context="ctx"> @{ var r=ctx as PicklistValueInfo; <TelerikCheckBox Enabled="false" Value="r.IsActive" /> } </Template> </GridColumn>

### Response

**Leland** answered on 06 Sep 2023

I was able to get something like this to work in one of my projects: <GridColumn Title="Is Active" Editable=false> <Template> <TelerikCheckBox @bind-Value="@(((AppRole)context).IsActive)" /> </Template> </GridColumn> The checkboxes are always visible and the values are editable with a single click. Note that this sidesteps the TelerikGrid's OnUpdate and OnEdit handlers, but the GridData will be be updated to reflect any changes through the binding. Additional logic can be provided in the TelerikCheckBox's OnChange handler.
