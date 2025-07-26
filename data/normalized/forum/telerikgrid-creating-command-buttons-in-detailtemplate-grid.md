# TelerikGrid Creating Command Buttons in DetailTemplate Grid

## Question

**Ste** asked on 16 Jun 2022

I am in the learning phase of Telerik currently, so I assume that I am missing something obvious here. I have the following code: <TelerikGrid Data="@EquipmentList" Groupable="true" Pageable="true"> <DetailTemplate> <TelerikGrid Data="@context.TaskList"> <GridColumns> <GridColumn Field="TaskTitle" Title="Task"> </GridColumn> <GridColumn Field="TaskDetail" Title="Detail"> </GridColumn> <GridCommandColumn> <GridCommandButton Command="OpenPDFCommand" Icon="file" OnClick="@(()=> FileService.OpenPDF(TaskPDF))"> Test Command </GridCommandButton> </GridCommandColumn> </GridColumns> </TelerikGrid> </DetailTemplate> <GridColumns> <GridColumn Field=EquipmentName> </GridColumn> </GridColumns> </TelerikGrid> This is the beginning of a maintenance task tracking site. The basic format of data is List<Equipment> and Equipment has List<MaintenanceTask> in it -- so a List within a List. I can get the data to show properly, but when I add the Command column to start adding functionality to the page, I get two errors that I don't fully understand: 1)
The child content element 'ChildContent' of component 'GridCommandColumn' uses the same parameter name ('context') as enclosing child content element 'DetailTemplate' of component 'TelerikGrid'. Specify the parameter name like: ' <ChildContent Context="another_name"> to resolve the ambiguity C:\Users\StevenDeam.ASIMOV\source\repos\JM3Telerik\JMWeb\Pages\Maintenance\MaintenanceMain.razor

2)
The name 'context' does not exist in the current context JMWeb C:\Users\StevenDeam.ASIMOV\source\repos\JM3Telerik\JMWeb\Pages\Maintenance\MaintenanceMain.razor 9 I did test adding a bogus context: <GridCommandColumn> <ChildContent Context="test"> This changed the error to say the namespace "test" could not be found. I am missing something on how the commandcolumn relates to the grid it seems. And none of the documentation that I can find shows the context of a commandcolumn needing to be changed.

### Response

**Steven** commented on 16 Jun 2022

I did test adding a bogus context: <GridCommandColumn> <ChildContent Context="test"> This changed the error, and said that the namespace "test" could not be found.

## Answer

**Steven** answered on 16 Jun 2022

I found the appropriate help page, [https://docs.telerik.com/blazor-ui/knowledge-base/nest-render-fragment](https://docs.telerik.com/blazor-ui/knowledge-base/nest-render-fragment) this seems to answer my question.
