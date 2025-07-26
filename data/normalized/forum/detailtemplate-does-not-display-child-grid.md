# DetailTemplate does not display child grid

## Question

**Nah** asked on 15 Sep 2023

Hello, good afternoon. I'm following this page's documentation to build a hierarchy grid. I just copied and pasted the code from the "Expand Rows From Code" example into my project just to see how it works (we are migrating Razor projects to Blazor). I can see the grid is displayed with the "+" button to expand child grids on each row and even the button to expand all the rows at the top as it is shown in the image below: Both do nothing, and DetailTemplate doesn't show up. Some technical stuff:.NET 5 The project is an MVC project with Blazor components in it Telerik UI For Blazor 4.5.0 NuGet package Visual Studio 2019 I cannot provide a code sample of how my project is structured. Is the company's property. I hope this helps. I tried following the documentation without success.

### Response

**Nahuel** commented on 15 Sep 2023

I also tried this example as well (attaching an event to the onRowClick event). The same behaviour, when I click on the row or the "+" to expand the child grid nothing happens.

### Response

**Dimo** commented on 15 Sep 2023

Possible JavaScript error on the page or a missing telerik-blazor.js file. Check the browser console. This sounds like a general problem with our product setup and not something specific to the Grid.

### Response

**Nahuel** commented on 15 Sep 2023

I appreciate the response but I don't have any JS errors by the time I compile my solution. The console shows no errors whatsoever and the blazor.server.js file is already included in the _Layout.cshtml file

### Response

**Dimo** commented on 16 Sep 2023

Nahuel, I was talking about our own script file telerik-blazor.js, not the framework file blazor.server.js. What happens if you replace the Grid with a simple <TelerikCalendar /> with no parameters? Does the Calendar date selection and navigation arrows work? If not, then there is surely some more general problem with the overall setup. I will need some code or even an example to investigate it. If the Calendar works, then try a component with a popup - a <TelerikDatePicker /> (code below). Does it work too? If yes, then the issue is related to the Grid. If not, then the issue may be related to the <TelerikRootComponent>. In either case, I will again need something to look at. You can also take the non-working code from the production app and put it in an empty new Blazor app with our components installed. Does it work then? If not, send this isolated app. <TelerikDatePicker Value="@DateValue" />

@code {
DateTime DateValue { get; set; }=DateTime.Now;
}

### Response

**Nahuel** commented on 18 Sep 2023

The telerik-blazor.js file is already present as well. I also followed the setup based on the code of this repository but with no success. One thing, if I try including the blazor.server.js file and start the Blazor server by hand first, the application is not serving from the blazor file (it gives a 404 code) and in consequence, I have a "Blazor is not defined" error while trying to start the server. I also tried putting the telerik-blazor.js file in <script> tags inside the Index.cshtml file itself like this: <script src="~/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js"></script> Although the file loads successfully, the component is still non-responsive. Neither the grid nor the <TelerikDatePicker /> work at all. Unfortunately, I cannot provide a code sample of this. What I can share is a snippet of how are we configuring our project, we have a main container that loads DLLs, and these DLLs are from several MVC projects. Assemblies are loaded like this: Startup.cs public void ConfigureServices ( IServiceCollection services ) {

[...] string _pluginsPath=$" {Path.GetDirectoryName(Assembly.GetExecutingAssembly().Location)} {Path.DirectorySeparatorChar} Plugins"; string [] _pluginsDlls=Directory.GetFiles(_pluginsPath).Where(s=> s.EndsWith( ".plugin.dll", StringComparison.CurrentCultureIgnoreCase)).ToArray();



List<Assembly> _pluginsAssemblies=new (); foreach ( string _dll in _pluginsDlls)
{
Assembly _pluginAssembly=Assembly.LoadFrom(_dll); if (_pluginAssembly.GetTypes().Where(t=> t.IsAssignableTo( typeof (IPlugin))).Any())
{
_pluginsAssemblies.Add(_pluginAssembly);
}
} foreach (Assembly item in _pluginsAssemblies)
{
services.AddControllersWithViews()
.AddApplicationPart(item)
.AddRazorRuntimeCompilation();





services.Configure<MvcRazorRuntimeCompilationOptions>(options=>
{ options.FileProviders.Add( new EmbeddedFileProvider(item)); });
}



services.AddServerSideBlazor();
services.AddTelerikBlazor();

} Assemblies are loaded and their content is served from their corresponding Index.cshtml file. For this component, in particular, we have it like this: Index.cshtml: @using LHP.Common.Entities;
@using LHP.WebUI.Common.ExtensionMethods;
@using LHP.WebUI.Maintenance.Plugin.Views.Shared.Component;



@model Layout;
@{ var sessionInformation=this.User.Identity.GetSessionInformationV2( this.Context.Request);
}



<component type="typeof(MaintenanceGrid)" param-SessionInformation="sessionInformation" render-mode="ServerPrerendered" /> And the component is called MaintenanceGrid.razor: <TelerikRootComponent>
<TelerikDatePicker Value="@DateValue" />
<div class="content-header" style="width: 100%;" id="Maintenance">
<div class="container-fluid">
<div id="MC-index">
<div class="row" id="divFilters">
</div>
<div class="row mt-3" id="divGrid">
<TelerikGrid Data=@MainGridData
Pageable="true">
<GridColumns>
<GridColumn Title="ID" Field=@nameof(MainGridItem.Id) />
<GridColumn Title="Nombre" Field=@nameof(MainGridItem.Description) />



</GridColumns>
<DetailTemplate>
<TelerikGrid Data="@MainGridData">
<GridColumns>
<GridColumn Title="ID" Field=@nameof(MainGridItem.Id) />
<GridColumn Title="Nombre" Field=@nameof(MainGridItem.Description) />
</GridColumns>
</TelerikGrid>
</DetailTemplate>
</TelerikGrid>



</div>
</div>
</div>
</div>
</TelerikRootComponent> @code { [Parameter] public SessionInformation SessionInformation { get; set; } public List<MaintenanceCounterpartyModel> Counterparties { get; set; } public List<MaintenanceCounterpartyLegalModel> LegalEntities { get; set; } DateTime DateValue { get; set; }=DateTime.Now; private List<MainGridItem> MainGridData { get; set; } private class MainGridItem { public int Id { get; set; } public string Name { get; set; } public string Description { get; set; } } protected override void OnInitialized() { MainGridData=new List<MainGridItem> { new MainGridItem { Id=1, Name="Item 1", Description="Description 1" }, new MainGridItem { Id=2, Name="Item 2", Description="Description 2" }, }; base.OnInitialized(); } } All this configuration produces this: The date picker is there, the button that should open the datepicker doesn't show up correctly but I'm pretty sure some styles are missing and the grid with the "+" button is there, the date picker doesn't open and the grid doesn't expand.

### Response

**Dimo** commented on 19 Sep 2023

Does the Blazor framework work at all in your app? For example, does this button text update when you click on it: <button @onclick="@( ()=> ButtonCounter++ )">@ButtonCounter clicks so far</button>

@code {
private int ButtonCounter { get; set; }
} If not, then address the more general issue first, and our components will probably start working. If yes, then I need a small app for inspection. You don't have to send your actual app - create one from scratch, which is similar to this one. I updated the components version and verified that it works. Or, make changes to it to break it.===On a side note, the CSS issue with the DatePicker button is probably due to mismatch between the theme version and the component version. For example, if the app loads the latest theme from unpkg.com, then better use the Telerik Blazor CDN or a static asset from the NuGet package. In this case it's a lot easier to match the theme version with the components version.

## Answer

**Nahuel** answered on 19 Sep 2023

Dimo, thanks for all the support. I would like to inform you that I finally fixed the issue. I've put both scripts (telerik.blazor.js and blazor.server.js) inside the component's _Index.cshtml and I started the Blazor server as stated in the GitHub repo you've kindly shared here Once I did that, the component worked as expected and now the grid expands normally.

### Response

**Dimo** commented on 20 Sep 2023

Good, thanks for the update!
