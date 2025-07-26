# Searching in FilterRow with Template for foreign value

## Question

**Dav** asked on 09 Nov 2020

Hi there, We are currently evaluating Telerik UI for Blazor. We are creating a component which uses the Grid to show data of type A. The class for type A has a foreign ID reference to type B. Right now we are showing the display name for this foreign value using the <Template> tag. This works great, but when searching using the Grid's FilterRow it seems the Grid is still searching in the foreign ID instead of its display name. I've tried using FilterDescriptors as per the documentation, but unfortunately did not get this to work. King regards, Davin

## Answer

**Stamo Gochev** answered on 11 Nov 2020

Hello Davin, As the "RoleId" field is of type "int", you are correct that using the "Template" configuration of the "GridColumn" tag is required in order to display the actual role name instead of the "RoleId" value. The case is the same for the filter row - by default, a NumericTextBox filter will be shown for the "RoleId" column. In order to customize it and use a DropDownList instead of a NumericTextBox, you can use the "FilterCellTemplate" configuration in a similar way as the "Template" tag. There is a demo for customizing the filter row that you can check out: [https://demos.telerik.com/blazor-ui/grid/custom-filter-row](https://demos.telerik.com/blazor-ui/grid/custom-filter-row) as well as a documentation article: [https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-row-template](https://docs.telerik.com/blazor-ui/components/grid/templates/filter#filter-row-template) that provide additional information on using the "FilterCellTemplate". For the concrete case, here is a sample initialization of a DropDownList that can be used: <GridColumn Field=@nameof(Employee.RoleId) Title="Position"> <EditorTemplate>... </EditorTemplate> <Template>... </Template> <FilterCellTemplate> <TelerikDropDownList Data="@Roles" DefaultText="Unknown" Value="@RoleId" TextField="@nameof(Role.RoleName)" ValueField="@nameof(Role.RoleId)" Width="100%" PopupHeight="auto" ValueChanged="@(async (int roleId)=> { RoleId=roleId; var filter=context.FilterDescriptor.FilterDescriptors[0] as FilterDescriptor; filter.Value=RoleId; await context.FilterAsync(); })"> </TelerikDropDownList> </FilterCellTemplate> </GridColumn> The code is almost identical to the DropDownList that is used in the "EditorTemplate" tag with an additional "ValueChanged" handler that receives the chosen "roleId" value and sets it to the "FilterDescriptor.Value" field and then makes a call to "await context.FilterAsync()", which triggers the actual filtering and returns the filtered results. The configuration can be customized further depending on your exact requirements, e.g. a ComboBox can be used instead or you can add additional filtering components. I am attaching a runnable updated version of the "ForeignSearch.razor" file with the above suggestions applies, so you can check it out. Regards, Stamo Gochev

### Response

**Joeri** answered on 17 Nov 2020

Hi, I'm working with Davin on the same project, thank you for your solution! However, a follow-up question remains for us: how can we achieve filtering in foreign records with the GridSearchBox on the toolbar?

### Response

**Stamo Gochev** answered on 19 Nov 2020

Hi Joeri, The search box feature works with string fields only (but "RoleId" is a number) and it does not have the same customization options compared to the filter cells. What I can suggest in this case is to further customize the filter row UI to better suit your needs. Regards, Stamo Gochev
