# Grid Filtering

## Question

**Pet** asked on 04 May 2019

Hi, in the demo [https://demos.telerik.com/blazor-ui/grid/filtering](https://demos.telerik.com/blazor-ui/grid/filtering) an extra filter row is always shown and the possible filter operators (==, !=,>, <, ...) are missing. How can I filter age> 40? I need a filter similar to the Kendo UI grid: Filter button in column header and extra filter popup window with all operators, similar [https://dojo.telerik.com/oQIyaHuD.](https://dojo.telerik.com/oQIyaHuD.) Is that possible? Best regards, Peter

## Answer

**Marin Bratanov** answered on 06 May 2019

Hello Peter, You are not missing anything. At the moment, the grid filtering only supports one operation per field type as explained in the following article: [https://docs.telerik.com/blazor-ui/components/grid/filtering.](https://docs.telerik.com/blazor-ui/components/grid/filtering.) The Blazor grid component is very young (literally, a couple of months old), and we are building it from the ground up so it fits the appropriate Blazor patterns and approaches. This means that it will take some time for it to catch up to other suites that have been in development for over a decade. We have improvements in the filtering area on our radar, and we intend to have more advanced features in the grid as soon as possible. Regards, Marin Bratanov

### Response

**Peter** answered on 06 May 2019

Hi Marin, an universal filter is important. The actual implementation of the EqualsTo/Contains operator is only a starting point. Mostly the Kendo UI grid behavior is enough: For all columns all possible operators, combined with AND. With the grid compont of Telerik UI for WinForms I can create more complex filter. A good approach is also the table filter in DBeaver: The result of the filters (the part after WHERE in SQL statement) is shown over the table in a textbox and can be edited. The user can create a basic filter by the UI (like in Kendo UI) and modify it later in the textbox - replace AND by OR, set brackets around part of the filter text ... Regards, Peter

### Response

**Marin Bratanov** answered on 06 May 2019

Hello Peter, Yes, the current filter is just a starting point. We intend to add a filtering menu with more options in a future version. For your convenience, I made the following page where you can follow the progress of this task by clicking the Follow button: [https://feedback.telerik.com/blazor/1406081-grid-filter.](https://feedback.telerik.com/blazor/1406081-grid-filter.) I have already added your vote. Regards, Marin Bratanov

### Response

**Oumaima** answered on 04 Feb 2020

Hi, How do I add a default filter on a Bazor Telerik grid ? I have a filter on a Date, which is working just fine, but I would like to select by default the last month data. Thank you in advance.

### Response

**Marin Bratanov** answered on 05 Feb 2020

Hi Oumaima, You can Vote for and Follow the implementation of programmatic filtering in the following page: [https://feedback.telerik.com/blazor/1440874-ability-to-set-filters-programatically.](https://feedback.telerik.com/blazor/1440874-ability-to-set-filters-programatically.) It is closely related to this one, so you may want to Follow that too: [https://feedback.telerik.com/blazor/1414050-save-grid-layout-state](https://feedback.telerik.com/blazor/1414050-save-grid-layout-state) You may also find interesting this one and if so - Vote and Follow it as well: [https://feedback.telerik.com/blazor/1407773-custom-filter-components-filter-template](https://feedback.telerik.com/blazor/1407773-custom-filter-components-filter-template) Regards, Marin Bratanov

### Response

**Sander** answered on 16 Mar 2020

Hello, I followed the instructions for installing Blazor Telerik. Everything works fine, accept the filtering. I used this example: @page "/" <TelerikGrid Data=@GridData Pageable="true" Height="400px" FilterMode="GridFilterMode.FilterMenu"> <GridColumns> <GridColumn Field=@nameof(Employee.Name) /> <GridColumn Field=@nameof(Employee.AgeInYears) Title="Age" /> <GridColumn Field=@nameof(Employee.HireDate) Title="Hire Date" /> <GridColumn Field=@nameof(Employee.IsOnLeave) Title="On Vacation" /> </GridColumns> </TelerikGrid> @code { public List<Employee> GridData { get; set; } protected override void OnInitialized() { GridData=new List<Employee>(); var rand=new Random(); for (int i=0; i <100; i++) { GridData.Add(new Employee() { EmployeeId=i, Name="Employee " + i.ToString(), AgeInYears=rand.Next(10, 80), HireDate=DateTime.Now.Date.AddDays(rand.Next(-20, 20)), IsOnLeave=i % 3==0 }); } } public class Employee { public int? EmployeeId { get; set; } public string Name { get; set; } public int? AgeInYears { get; set; } public DateTime HireDate { get; set; } public bool IsOnLeave { get; set; } } } but returns an unexpected error: An unhandled exception occurred while processing the request. NullReferenceException: Object reference not set to an instance of an object. Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragmentBase.Dispose()

### Response

**Svetoslav Dimitrov** answered on 16 Mar 2020

Hello Sander, Could you check in your _Imports.razor file for the following using statements: @using Telerik.Blazor
@using Telerik.Blazor.Components Another thing you should check for is the <TelerikRootComponent> in the MainLayout.razor (located in your Shared folder ). It should look like this: @inherits LayoutComponentBase <TelerikRootComponent> <div class="sidebar"> <NavMenu /> </div> <div class="main"> @Body </div> </TelerikRootComponent> You can find more information on the steps described above in: This article: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need](https://docs.telerik.com/blazor-ui/getting-started/what-you-need) This tutorial: [https://docs.telerik.com/blazor-ui/getting-started/server-blazor](https://docs.telerik.com/blazor-ui/getting-started/server-blazor) Regards, Svetoslav Dimitrov

### Response

**Sander** answered on 19 Mar 2020

The TelerikRootComponent did the job. Thank you

### Response

**Svetoslav Dimitrov** answered on 19 Mar 2020

Hello Sander, I am glad to hear that everything works now as expected! Regards, Svetoslav Dimitrov
