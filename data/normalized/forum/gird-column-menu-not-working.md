# Gird Column Menu not working

## Question

**Lar** asked on 06 Sep 2024

Hello, I am trying to use the Grid Column Menu and even the most basic example from the docs throws an error or just freezes the page. I am using the latest version of Telerik (6.0.2) I already have other Telerik Grids and components working well in another pages. Here is the link from the docs. Here is the code in my page: @page "/tests" @rendermode InteractiveServer <h3>Testing</h3> <TelerikGrid Data="@GridData" Pageable="true" PageSize="5" FilterMode="@GridFilterMode.FilterMenu" Sortable="true" ShowColumnMenu="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="80px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </GridColumns> </TelerikGrid> @code { private IEnumerable<SampleData> GridData=Enumerable.Range(1, 30).Select(x=> new SampleData { Id=x, Name="name " + x, Team="team " + x % 5, HireDate=DateTime.Now.AddDays(-x).Date }); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; } } }

### Response

**Dimo** commented on 10 Sep 2024

@Larchi - here is my answer from your ticket. Please notify us when you post a duplicate forum thread and support ticket. Otherwise we may not notice that, which will lead to double work. Please enable detailed errors, so that you can see what is the exact error message in the browser console. Alternatively, you can see it in the application output window in Visual Studio. My guess is that the app is using Per page / component interactivity location and the TelerikRootComponent is missing or not configured correctly. Please refer to [https://docs.telerik.com/blazor-ui/components/rootcomponent/per-component-interactivity-location](https://docs.telerik.com/blazor-ui/components/rootcomponent/per-component-interactivity-location) If my assumption is incorrect, please provide the exact error message or a runnable test app.

### Response

**Larchi** commented on 10 Sep 2024

Thanks for the answer, I think it's maybe a good idea to share with others in the form the answers of tickets. It's frankly a bit confusing as the Per page / component is the default when creating a new project now. I ended up opting for the simple solution of just changing it in the "App.razor" and adding the 2 bold parts and it's working well now: <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <base href="/" /> <link rel="stylesheet" href="bootstrap/bootstrap.min.css" /> <link rel="stylesheet" href="app.css" /> <link rel="stylesheet" href="SolarNexus.styles.css" /> <link rel="icon" type="image/png" href="favicon.png" /> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js"></script> <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> <HeadOutlet @rendermode="InteractiveServer" /> </head> <body> <Routes @rendermode="InteractiveServer" /> <script src="_framework/blazor.web.js"></script> </body> </html> Hope you have a great day Dimo
