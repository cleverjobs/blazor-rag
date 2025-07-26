# Error with JS interop

## Question

**Dan** asked on 23 Aug 2020

Hello, I am trying to integrate your blazor components in to my app. I am getting the following error: [2020-08-22T23:29:42.283Z] Error: Microsoft.JSInterop.JSException: Could not find 'TelerikBlazor' in 'window'. Error: Could not find 'TelerikBlazor' in 'window'. Failed to load resource: the server responded with a status of 404 (Not Found) blazor.server.js:1 [https://localhost:5001/_content/telerik.ui.for.blazor/js/telerik-blazor.js](https://localhost:5001/_content/telerik.ui.for.blazor/js/telerik-blazor.js) My Startup.cs public class Startup { public Startup(IConfiguration configuration) { Configuration=configuration; } public IConfiguration Configuration { get; } // This method gets called by the runtime. Use this method to add services to the container. // For more information on how to configure your application, visit [https://go.microsoft.com/fwlink/?LinkID=398940](https://go.microsoft.com/fwlink/?LinkID=398940) public void ConfigureServices(IServiceCollection services) { services.AddRazorPages(); services.AddServerSideBlazor(); services.AddDatabaseServices(); services.AddTelerikBlazor(); } // This method gets called by the runtime. Use this method to configure the HTTP request pipeline. public void Configure(IApplicationBuilder app, IWebHostEnvironment env) { if (env.IsDevelopment()) { app.UseDeveloperExceptionPage(); } else { app.UseExceptionHandler("/Error"); // The default HSTS value is 30 days. You may want to change this for production scenarios, see [https://aka.ms/aspnetcore-hsts.](https://aka.ms/aspnetcore-hsts.) app.UseHsts(); } app.UseHttpsRedirection(); app.UseStaticFiles(); app.UseRouting(); app.UseEndpoints(endpoints=> { endpoints.MapBlazorHub(); endpoints.MapFallbackToPage("/_Host"); }); } } This project using Server Side Blazor <Project Sdk="Microsoft.NET.Sdk.Web"> <PropertyGroup> <TargetFramework>netcoreapp3.1</TargetFramework> </PropertyGroup> *** <ItemGroup> <PackageReference Include="Telerik.UI.for.Blazor" Version="2.16.0" /> </ItemGroup> <ItemGroup> <_ContentIncludedByDefault Remove="wwwroot\css\bootstrap\bootstrap.min.css" /> <_ContentIncludedByDefault Remove="wwwroot\css\bootstrap\bootstrap.min.css.map" /> </ItemGroup> <ItemGroup> <Folder Include="wwwroot\css" /> </ItemGroup> </Project> 3.1.401 [/usr/local/share/dotnet/sdk] This is on a mac platform for development

## Answer

**Marin Bratanov** answered on 23 Aug 2020

Hi Daniel, Could you try the information from the following pages and see if it helps you resolve this: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) [https://docs.telerik.com/blazor-ui/troubleshooting/deployment](https://docs.telerik.com/blazor-ui/troubleshooting/deployment) Regards, Marin Bratanov

### Response

**Daniel** answered on 23 Aug 2020

Thank you so much for your help. It was the casing issue. I also submitted a pull request to fix the blazor-dashboard sample.

### Response

**Marin Bratanov** answered on 24 Aug 2020

Hi Daniel, Thank you for noticing and the PR, I have, indeed, missed to fix the path casing in this sample app. You'll find your Telerik Points updated as a small "thank you" for letting me know and for the fix. Regards, Marin Bratanov
