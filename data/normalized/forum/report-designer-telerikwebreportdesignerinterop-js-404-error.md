# Report Designer "telerikWebReportDesignerInterop.js" 404 error

## Question

**Tha** asked on 19 Aug 2021

I followed How to set up in Blazor application | Telerik Reporting All done! But when it run i got an error "telerikWebReportDesignerInterop.js 404" <script src="_content/telerik.webreportdesigner.blazor/telerikWebReportDesignerInterop.js" defer> </script> and in console show: fail: Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost[ 111 ]
Unhandled exception in circuit 'Gyr8E4g_PwQHf7G2UKY2h3obMpujPfFp2x9i7dkB4oQ'.
Microsoft.JSInterop.JSException: Could not find 'telerikWebReportDesignerInterop.createWebReportDesignerWidget' ( 'telerikWebReportDesignerInterop' was undefined).
Error: Could not find 'telerikWebReportDesignerInterop.createWebReportDesignerWidget' ( 'telerikWebReportDesignerInterop' was undefined).
at https: //localhost:5001/_framework/blazor.server.js:1:67713 at Array.forEach (<anonymous>)
at e.findFunction (https: //localhost:5001/_framework/blazor.server.js:1:67673) at v ( [https://localhost:](https://localhost:) 5001 /_framework/blazor.server.js: 1: 69415 )
at https: //localhost:5001/_framework/blazor.server.js:1:70361 at new Promise ( <anonymous> )
at e. beginInvokeJSFromDotNet ( [https://localhost:](https://localhost:) 5001 /_framework/blazor.server.js: 1: 70334 )
at https: //localhost:5001/_framework/blazor.server.js:1:26441 at Array. forEach ( <anonymous> )
at e. invokeClientMethod ( [https://localhost:](https://localhost:) 5001 /_framework/blazor.server.js: 1: 26411 )
at Microsoft.JSInterop.JSRuntime.InvokeAsync[TValue]( Int64 targetInstanceId, String identifier, Object[] args )
at Microsoft.JSInterop.JSRuntimeExtensions. InvokeVoidAsync ( IJSRuntime jsRuntime, String identifier, Object[] args )
at Microsoft.AspNetCore.Components.RenderTree.Renderer. GetErrorHandledTask ( Task taskToHandle ) Telerik Reporting 15.1.21.616 <PackageReference Include="Telerik.Reporting.Services.AspNetCore" Version="15.1.21.616" /> <PackageReference Include="Telerik.Reporting.OpenXmlRendering" Version="15.1.21.616" /> <PackageReference Include="Telerik.ReportViewer.Blazor" Version="15.1.21.616" /> <PackageReference Include="Telerik.WebReportDesigner.Blazor" Version="15.1.21.616" /> <PackageReference Include="Telerik.WebReportDesigner.Services" Version="15.1.21.616" /> Startup.cs namespace CSharp.Net5.BlazorIntegrationDemo { using Microsoft.AspNetCore.Builder; using Microsoft.AspNetCore.Hosting; using Microsoft.Extensions.Configuration; using Microsoft.Extensions.DependencyInjection; using Microsoft.Extensions.DependencyInjection.Extensions; using Microsoft.Extensions.Hosting; using System; using Telerik.Reporting.Cache.File; using Telerik.Reporting.Services; using Telerik.WebReportDesigner.Services; public class Startup { public Startup ( IConfiguration configuration ) { this.Configuration=configuration;
} public IConfiguration Configuration { get; } // This method gets called by the runtime. Use this method to add services to the container. // For more information on how to configure your application, visit [https://go.microsoft.com/fwlink/?LinkID=398940](https://go.microsoft.com/fwlink/?LinkID=398940) public void ConfigureServices ( IServiceCollection services ) {
services.AddControllers();

services.AddRazorPages()
.AddNewtonsoftJson();
services.AddServerSideBlazor(); // Configure dependencies for ReportsController. services.TryAddSingleton<IReportServiceConfiguration>(sp=> new ReportServiceConfiguration
{
ReportingEngineConfiguration=sp.GetService<IConfiguration>(),
HostAppId="Net5BlazorDemo",
Storage=new FileStorage(),
ReportSourceResolver=new UriReportSourceResolver(System.IO.Path.Combine(sp.GetService<IWebHostEnvironment>().ContentRootPath, "..", "..", "..", "..", "Report Designer", "Examples" )),
}); // Configure dependencies for ReportDesignerController. services.TryAddSingleton<IReportDesignerServiceConfiguration>(sp=> new ReportDesignerServiceConfiguration
{
DefinitionStorage=new FileDefinitionStorage(
System.IO.Path.Combine(sp.GetService<IWebHostEnvironment>().ContentRootPath, "..", "..", "..", "..", "Report Designer", "Examples" )),
SettingsStorage=new FileSettingsStorage(
System.IO.Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "Telerik Reporting" )),
ResourceStorage=new ResourceStorage(
System.IO.Path.Combine(sp.GetService<IWebHostEnvironment>().ContentRootPath, "..", "..", "..", "..", "Report Designer", "Examples", "Resources" ))
});
} // This method gets called by the runtime. Use this method to configure the HTTP request pipeline. public void Configure ( IApplicationBuilder app, IWebHostEnvironment env ) { if (env.IsDevelopment())
{
app.UseDeveloperExceptionPage();
} else {
app.UseExceptionHandler( "/Error" );
}

app.UseStaticFiles();
app.UseRouting();
app.UseEndpoints(endpoints=>
{
endpoints.MapControllers();
endpoints.MapBlazorHub();
endpoints.MapFallbackToPage( "/_Host" );
});
} /// <summary> /// Loads a reporting configuration from a specific JSON-based configuration file. /// </summary> /// <param name="environment"> The current web hosting environment used to obtain the content root path </param> /// <returns> IConfiguration instance used to initialize the Reporting engine </returns> static IConfiguration ResolveSpecificReportingConfiguration ( IWebHostEnvironment environment ) { // If a specific configuration needs to be passed to the reporting engine, add it through a new IConfiguration instance. var reportingConfigFileName=System.IO.Path.Combine(environment.ContentRootPath, "reportingAppSettings.json" ); return new ConfigurationBuilder()
.AddJsonFile(reportingConfigFileName, true )
.Build();
}
}
} WebReportDesignerDemo.razor @page "/webreportdesigner"
@using Telerik.WebReportDesigner.Blazor <style> #wrd1 { position: relative; height: 880px; padding-right: 50px;
} </style> @* Create the WebReportDesignerWidget *@<p> This Web Report Designer instance works with reports hosted locally using the Reporting REST service. For more information, visit the <a target="_blank" href="[https://docs.telerik.com/reporting/web-report-designer">](https://docs.telerik.com/reporting/web-report-designer">) Web Report Designer </a> article. </p> <WebReportDesigner DesignerId="wrd1" ServiceUrl="/api/reportdesigner" Report="Dashboard.trdp" ToolboxArea="new ToolboxAreaOptions() { Layout=ToolboxAreaLayout.List }" PropertiesArea="new PropertiesAreaOptions() { Layout=PropertiesAreaLayout.Categorized }" />

### Response

**Dimitar** commented on 23 Aug 2021

The Report Designer REST Service seems to be correctly set up based on the provided code, still to ensure that it is working as expected, please try the solution from the Test whether Web Report Designer Service is Responding KB article and let me know the result of this test. I suspect that the issue is somewhere in the adding the web report designer component part. Please make sure that you have added all necessary references to Pages/_Host.cshtml and they are in the correct order. For example, the jQuery reference must be before the references to the report viewer and web report designer JS files. If you will need further help, please do the following: Install the Fiddler Jam extension then generate a log and share it with us. In the case where the test of the web designer REST service is unsuccessful, you may attach a trace listener and record a trace log - Troubleshooting reporting implementation into ASP.NET Core application. You may also send the _Host.cshtml and the page with the web designer or a runnable project that demonstrates the issue. Thank you for trying Telerik Reporting!

### Response

**Thanh** commented on 23 Aug 2021

@page "/"
@namespace CSharp.Net5.BlazorIntegrationDemo.Pages
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <title> Telerik Reporting & Blazor </title> <base href="~/" /> <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" /> <link href="css/site.css" rel="stylesheet" /> @* Report Viewer dependencies *@<script src="[https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">](https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js">) </script> <script src="[https://kendo.cdn.telerik.com/2020.3.1118/js/kendo.all.min.js">](https://kendo.cdn.telerik.com/2020.3.1118/js/kendo.all.min.js">) </script> <script src="/api/reports/resources/js/telerikReportViewer"> </script> <script src="api/reportdesigner/designerresources/js/webReportDesigner-15.1.21.616.min.js/"> </script> <link rel="stylesheet" href="[https://unpkg.com/@@progress/kendo-theme-default@latest/dist/all.css"](https://unpkg.com/@@progress/kendo-theme-default@latest/dist/all.css") /> </head> <body> <app> <component type="typeof(App)" render-mode="ServerPrerendered" /> </app> <div id="blazor-error-ui"> <environment include="Staging,Production"> An error has occurred. This application may no longer respond until reloaded. </environment> <environment include="Development"> An unhandled exception has occurred. See browser dev tools for details. </environment> <a href class="reload"> Reload </a> <a class="dismiss"> 🗙 </a> </div> <script src="_framework/blazor.server.js"> </script> @* Our Blazor app JS Interop file for working with the ReportViewer widget *@<script src="_content/telerik.reportviewer.blazor/interop.js" defer> </script> <script> window.trvEventHandlers={ exportBegin: function ( e, args ) { console.log( "This event handler will be called before exporting the report in " + args.format + " format." );
}, exportEnd: function ( e, args ) { console.log( "This event handler will be called after exporting the report." ); console.log( "The exported report can be found at: " + window.location.origin + args.url);
}
} </script> @* Our Blazor app JS Interop file for working with the WebReportDesigner widget *@<script src="_content/telerik.webreportdesigner.blazor/telerikWebReportDesignerInterop.js" defer> </script> </body> </html> Here is the _Host.cshtml file content.

### Response

**Dimitar** commented on 24 Aug 2021

After discussing this case in a ticket, Thanh was able to resolve his issue by manually creating the Interops: var telerikReportViewerInterop={};
telerikReportViewerInterop.createReportViewerWidget=function ( element, configs ) { //debugger; return $(element).telerik_ReportViewer( JSON.parse(configs)).data( "telerik_ReportViewer" );
}

telerikReportViewerInterop.refreshReport=function ( element ) { return $(element).data( "telerik_ReportViewer" ).refreshReport();
} var telerikWebReportDesignerInterop={};
telerikWebReportDesignerInterop.createWebReportDesignerWidget=function ( element, configs ) { //debugger; return $(element).telerik_WebReportDesigner( JSON.parse(configs)).data( "telerik_ReportDesigner" );
}

## Answer

**Steve** answered on 09 Dec 2022

Where do you add this code for manually creating the interops? UPDATE: Never mind, I just realized I needed to wrap this in a script tag and remove the script tag based on src: @*<script src="_content/Telerik.ReportViewer.Blazor/interop.js" defer></script>*@<script> var telerikReportViewerInterop={}; telerikReportViewerInterop.createReportViewerWidget=function (element, configs) { //debugger; return $(element).telerik_ReportViewer(JSON.parse(configs)).data("telerik_ReportViewer"); } telerikReportViewerInterop.refreshReport=function (element) { return $(element).data("telerik_ReportViewer").refreshReport(); } var telerikWebReportDesignerInterop={}; telerikWebReportDesignerInterop.createWebReportDesignerWidget=function (element, configs) { //debugger; return $(element).telerik_WebReportDesigner(JSON.parse(configs)).data("telerik_ReportDesigner"); } </script>
