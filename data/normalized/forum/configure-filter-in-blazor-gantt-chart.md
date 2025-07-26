# Configure Filter in Blazor Gantt Chart

## Question

**duk** asked on 10 Jan 2023

Hello, I would like to customize the filtering view window in Gantt. Is there a possibility to search for simple values using a text field? In addition, I would also like to make changes to the labels (language: German). The same applies to the event settings (double-click on events), where I would also like to change the language to German. Many thanks in advance.

## Answer

**Hristian Stefanov** answered on 13 Jan 2023

Hi Paul, Thank you for the detailed explanation and the provided screenshots. Now let me cover the two questions below...Is there a possibility to search for simple values using a text field?.. You can easily customize the filter menu and make it display only a textbox by using some CSS. Start by setting the desired DefaultFilterOperator, and then apply the custom CSS that hides the other fields. I have prepared a sample for you that shows the result from the above CSS approach: REPL link. Please run the REPL and test it to see if it suits your needs...I would also like to make changes to the labels (language: German).. You can change the language for the whole Gantt component by using Localization. The article shows on how localization works in the Blazor components and how to enable it in an app.=====I hope you will find the above information helpful. If we can help with anything further, I'm at your disposal. Regards, Hristian Stefanov Progress Telerik

### Response

**duktionsplanungIGP** commented on 09 Feb 2023

Hello Hristian, Thank you very much for your answer. Unfortunately, despite instructions, I could not achieve the desired result. I performed the following steps (based on the instructions): Step 1 in Startup.cs: using System.Collections.Generic;
using System.Globalization;
using Projecttitle.Data;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Localization;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Options;
using Plk.Blazor.DragDrop;
using Radzen;
using Telerik.Blazor.Services;
using ServerLocalizationResx.Services;

namespace Projecttitle
{
public class Startup
{
public Startup(IConfiguration configuration)
{
Configuration=configuration;
}


public IConfiguration Configuration { get; }

// This method gets called by the runtime. Use this method to add services to the container.
// For more information on how to configure your application, visit [https://go.microsoft.com/fwlink/?LinkID=398940](https://go.microsoft.com/fwlink/?LinkID=398940)
public void ConfigureServices(IServiceCollection services)
{

services.AddControllers();
services.AddLocalization(options=> options.ResourcesPath="Resources");
services.Configure <RequestLocalizationOptions> (options=>
{
// define the list of cultures your app will support
var supportedCultures=new List <CultureInfo> ()
{
new CultureInfo("en-US"),
new CultureInfo("fr-FR"),
new CultureInfo("bg-BG")
};

// set the default culture
options.DefaultRequestCulture=new RequestCulture("de-DE");

options.SupportedCultures=supportedCultures;
options.SupportedUICultures=supportedCultures;
});

services.AddRazorPages();
services.AddServerSideBlazor();
services.AddSingleton <WeatherForecastService> ();
services.AddSingleton <MitarbeiterService> ();
services.AddSingleton <AuftragService> ();
services.AddBlazorDragDrop();
services.AddScoped <TooltipService> ();
services.AddScoped <NotificationService> ();
services.AddScoped <DialogService> ();
services.AddTelerikBlazor();
// register a custom localizer for the Telerik components, after registering the Telerik services
services.AddSingleton(typeof(ITelerikStringLocalizer), typeof(SampleResxLocalizer));

services.AddBlazorContextMenu(options=>
{
options.ConfigureTemplate("myTemplate", template=>
{
template.MenuCssClass="my-menu";
template.MenuItemCssClass="my-menu-item";

});
});
// This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{

app.UseRequestLocalization(app.ApplicationServices.GetService<IOptions <RequestLocalizationOptions>>().Value);

// the rest is just a sample app configuration
app.UseResponseCompression();
if (env.IsDevelopment())
{
app.UseDeveloperExceptionPage();
}
else
{
app.UseExceptionHandler("/Error");
// The default HSTS value is 30 days. You may want to change this for production scenarios, see [https://aka.ms/aspnetcore-hsts.](https://aka.ms/aspnetcore-hsts.)
app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseEndpoints(endpoints=>
{
endpoints.MapControllers();
endpoints.MapBlazorHub();
endpoints.MapFallbackToPage("/_Host");
});
}
}
} Step 2: Added CultureController.cs in Projekttitel-->Controller(folder)-->CultureController.cs using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Localization;
using Microsoft.AspNetCore.Mvc;
using ServerLocalizationResx.Services;

namespace ServerLocalizationResx.Controllers
{
[Route("[controller]/[action]")]
public class CultureController : Controller
{
public IActionResult SetCulture(string culture, string redirectUri)
{
if (culture !=null)
{
HttpContext.Response.Cookies.Append(
CookieRequestCultureProvider.DefaultCookieName,
CookieRequestCultureProvider.MakeCookieValue(new RequestCulture(culture, culture)));
}

return LocalRedirect(redirectUri);
}

public IActionResult ResetCulture(string redirectUri)
{
HttpContext.Response.Cookies.Delete(CookieRequestCultureProvider.DefaultCookieName);

return LocalRedirect(redirectUri);
}
}
} Step 2 (continue) for _Host.cshtml: @page "/"
@namespace Projecttitle.Pages
@using Microsoft.AspNetCore.Localization
@using System.Globalization
@addTagHelper *, Microsoft.AspNetCore.Mvc.TagHelpers
@{
Layout=null;
} <!DOCTYPE html> <html lang="en"> <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <title> Projecttitle </title> <base href="~/" /> <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" /> <link href="css/site.css" rel="stylesheet" /> <link href="Projecttitle.styles.css" rel="stylesheet" /> <link rel="stylesheet" href="_content/Radzen.Blazor/css/default.css"> <link href="_content/Blazor.ContextMenu/blazorContextMenu.min.css" rel="stylesheet" /> <script src="_content/Blazor.ContextMenu/blazorContextMenu.min.js"> </script> <link href="_content/Blazored.Typeahead/blazored-typeahead.css" rel="stylesheet" /> <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer> </script> <script src="_framework/blazor.server.js"> </script> </head> <body> @{
this.HttpContext.Response.Cookies.Append(CookieRequestCultureProvider.DefaultCookieName,
CookieRequestCultureProvider.MakeCookieValue(new RequestCulture(CultureInfo.CurrentCulture, CultureInfo.CurrentUICulture))
);
} <component type="typeof(App)" render-mode="ServerPrerendered" /> <div id="blazor-error-ui"> <environment include="Staging,Production"> An error has occurred. This application may no longer respond until reloaded. </environment> <environment include="Development"> An unhandled exception has occurred. See browser dev tools for details. </environment> <environment include="Development"> <script> window.Blazor.defaultReconnectionHandler.onConnectionDown=function ( ) { setTimeout ( function ( ) {
location.reload();
}, 7000 );
} </script> </environment> <a href="" class="reload"> Reload </a> <a class="dismiss"> 🗙 </a> </div> <script> Blazor.defaultReconnectionHandler._reconnectCallback=function ( d ) { document.location.reload(); } </script> <script src="_framework/blazor.server.js"> </script> <script src="_content/Radzen.Blazor/Radzen.Blazor.js"> </script> <script src="_content/Blazored.Typeahead/blazored-typeahead.js"> </script> </body> </html> Step 3: Implemented as in the Example in Index.razor Step 4: Created File "SampleResxLocalizer" and paste the example in it. Path ist under Project-->Shared-->Services-->SampleResxLocalizer.cs Step 4 (continue): I copied the german version of the resourcefile from GitHub and put it as file in my folder structure. Path is: Project-->Shared-->Resources-->TelerikMessages.resx The TelerikMessages.Deginer.cs is automatically created under my implemented file "TelerikMessages", which includes the german language. But I can't build my application and get the error in the building-process: "Unable to resolve service for type 'Microsoft.AspNetCore.ResponseCompression.IResponseCompressionProvider' while attempting to activate 'Microsoft.AspNetCore.ResponseCompression.ResponseCompressionMiddleware'." I don't know what change of the code could create this error. I hope you can find the problem by looking at my files. Thank you very much. Best Regards Paul

### Response

**Hristian Stefanov** commented on 13 Feb 2023

Hi Paul, Thank you for keeping me updated. I carefully reviewed the provided steps. The issue is due to the following line in the Startup.cs file: " app.UseResponseCompression(); ". To make things work, you need to remove it. It turns out that this is an old framework issue for older versions. Upon interest, here is the public dotnet item I found on the internet about it. I'm sorry for the inconvenience. I will also remove this line from our documentation. If further difficulties appear, let me know.
