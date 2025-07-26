# onkeyup not firing in Blazor ui window control

## Question

**Joh** asked on 30 Nov 2021

I want to capture keys to implement short cut commands. I wrap the TelerikWindow in a <div @onkeyup> but the handler doesn't get called. Works if the TelerikWindow is removed. This is the Blazor test page @page "/test" <div @onkeyup="HandleKeyUp" tabindex="0" @ref="testRef"> @KeyPressed <TelerikWindow Visible="true" Width="1200px"> <WindowTitle> <strong>Wager Coverage</strong> </WindowTitle> <WindowActions> <WindowAction Name="Minimize"></WindowAction> <WindowAction Name="Maximize"></WindowAction> <WindowAction Name="Close"></WindowAction> </WindowActions> <WindowContent> <TelerikGrid Data="@MyData" Height="400px" Pageable="true" Sortable="true" Groupable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow" Resizable="true" Reorderable="true"> <GridColumns> <GridColumn Field="@(nameof(SampleData.Id))" Width="120px" /> <GridColumn Field="@(nameof(SampleData.Name))" Title="Employee Name" Groupable="false" /> <GridColumn Field="@(nameof(SampleData.Team))" Title="Team" /> <GridColumn Field="@(nameof(SampleData.HireDate))" Title="Hire Date" /> </GridColumns> </TelerikGrid> </WindowContent> </TelerikWindow> </div> @code { public string inputtext { get; set; } string KeyPressed; void HandleKeyUp(KeyboardEventArgs e) { KeyPressed=e.Key; } private ElementReference testRef; [Inject] IJSRuntime JSRuntime { get; set; } protected override async Task OnAfterRenderAsync(bool firstRender) { if (firstRender) { await JSRuntime.InvokeVoidAsync("SetFocusToElement", testRef); //await testRef.FocusAsync(); } } public IEnumerable<SampleData> MyData=Enumerable.Range(1, 30).Select(x=> new SampleData { Id=x, Name="name " + x, Team="team " + x % 5, HireDate=DateTime.Now.AddDays(-x).Date }); public class SampleData { public int Id { get; set; } public string Name { get; set; } public string Team { get; set; } public DateTime HireDate { get; set; } } }

## Answer

**Dimo** answered on 03 Dec 2021

Hello Lee, Try moving the <div> inside the <WindowContent>. Our popups (Windows, Dialogs, drop downs) render directly in the <body>. This ensures that they overlay any other content on the page, including scrollable containers. As a result, the Window ends up outside the <div> and the @onkeyup handler can't work for it. Regards, Dimo
