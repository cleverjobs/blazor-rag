# Need help with custom column's template

## Question

**Iva** asked on 04 Jan 2021

Hello! I'm trying to implement some user's menu in column's template like this: <TelerikGrid Data="@MyData" Height="100%" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> <GridColumn Filterable="false" Title="Menu" Lockable="false" Sortable="false" ShowColumnChooser="false" VisibleInColumnChooser="false" ShowColumnMenu="false"> <Template> @{ <button class="btn btn-default dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> Menu </button> <div class="dropdown-menu"> <a class="dropdown-item" style="cursor: pointer">Edit</a> <a class="dropdown-item" style="cursor: pointer">Delete</a> </div> } </Template> </GridColumn> </GridColumns> </TelerikGrid> @code { public IEnumerable<SampleData> MyData=Enumerable.Range(1, 1).Select(x=> new SampleData { Id=x, Name="name " + x, Team="team " + x % 5, HireDate=DateTime.Now.AddDays(-x).Date }); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; } } } But menu is not fully showing and hide by grid's footer setting z-index for dropdown doesnt help Please help....

## Answer

**Marin Bratanov** answered on 05 Jan 2021

Hello Ivan, This type of behavior is why we render our popups not in the place of declaration, but as high in the content as possible. Parent elements can have rules like overflow:hidden or other rules that can affect popups in a similar fashion. Thus, what I can suggest is that you consider using the ContextMenu component we offer for this task, you can see how to integrate it with the grid (or any other custom content) in its documentation and demos. Regards, Marin Bratanov
