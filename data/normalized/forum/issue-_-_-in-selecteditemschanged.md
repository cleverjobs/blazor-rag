# Issue (?) in SelectedItemsChanged

## Question

**Gia** asked on 14 Apr 2020

Hi I have a grid like these <TelerikGrid Data="@List_GEST_Ordini_Teste_Filtrato" Height="auto" Pageable="true" Sortable="false" Groupable="false" PageSize="20" FilterMode="Telerik.Blazor.GridFilterMode.FilterMenu" Resizable="true" Reorderable="true" SelectionMode="GridSelectionMode.Single" SelectedItemsChanged="@((IEnumerable<ViewListaOrdini> employeeList)=> OnSelect(employeeList))"> .... In OnSelect I use the next, to move another page Navigation.NavigateTo("ordineediting", false); In 2.9 all works fine, but I've upgraded to 2.10 all stopped to work: OnSelect i called multiple indefinitly tnx

## Answer

**Marin Bratanov** answered on 14 Apr 2020

Hello Giampaolo, This seems to work fine for me with 2.10.0. Can you confirm that you have upgraded all assets, including JS Interop file (especially if you are using it from the CDN) by following the instructions: [https://docs.telerik.com/blazor-ui/upgrade/overview?](https://docs.telerik.com/blazor-ui/upgrade/overview?) There was a similar issue ( link with details ) in 2.9.0 and if the upgrade was not successful, you may still be hitting it. I am also attaching here two sample apps that seem to work fine for me so you can check if I am missing something and compare against them if they work fine for you. If you can reproduce the issue in either, please post here the needed changes so I can investigate. Regards, Marin Bratanov

### Response

**Giampaolo** answered on 14 Apr 2020

Hi I've found the issue In attach the example The problem is that the grid is bound to another list that sub-filter and order items from antoher list. Very strange: in 2.9 all worked fine, and now we get an error. I know that this is not the correct way to bind items to list... but it worked. I'll solve in other mode. Tnx

### Response

**Giampaolo** answered on 14 Apr 2020

Excuse me I cannot attach zip files <TelerikGrid Data=@GridDataToShow SelectionMode="GridSelectionMode.Single" SelectedItemsChanged="@((IEnumerable<Employee> employeeList)=> OnSelect(employeeList))" Pageable="true" Height="300px"> <GridColumns> <GridColumn Field=@nameof(Employee.Name) /> <GridColumn Field=@nameof(Employee.Team) Title="Team" /> </GridColumns> </TelerikGrid> @code { public List<Employee> GridDataToShow { get { return GridData.OrderBy(x=>x.EmployeeId).ToList(); } } public List<Employee> GridData { get; set; } public Employee SelectedEmployee { get; set; } protected override void OnInitialized() { GridData=new List<Employee>(); for (int i=0; i <15; i++) { GridData.Add(new Employee() { EmployeeId=i, Name="Employee " + i.ToString(), Team="Team " + i % 3 }); } }

### Response

**Marin Bratanov** answered on 15 Apr 2020

Hi Giampaolo, Thank you for getting back to me. It hadn't occurred to me to pre-sort the data. I made the following page where we can track this issue: [https://feedback.telerik.com/blazor/1461863-infinite-loop-in-selecteditemschanged-when-the-grid-is-bound-to-a-pre-filtered-sorted-collection-in-2-10-0.](https://feedback.telerik.com/blazor/1461863-infinite-loop-in-selecteditemschanged-when-the-grid-is-bound-to-a-pre-filtered-sorted-collection-in-2-10-0.) It offers a workaround and the results from the investigation will be posted there - either the release with a fix, or more details on why it won't be handled internally in the grid if that would be the case. Regards, Marin Bratanov
