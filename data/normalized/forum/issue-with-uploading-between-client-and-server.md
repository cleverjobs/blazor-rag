# Issue with uploading between Client and Server

## Question

**Doo** asked on 08 May 2021

I have my solution as an API Server on .Net 5 that does all the weightlifting, Elsa workflows, database IO & integrations. The portal is a Blazor Server-Side application on .Net 5. The deployment is like so: The portal connects with the API with the standard HttpClient dependency injection. Here is the API setup first: API - Program.cs public class Program { public static void Main ( string [] args ) { try { using IHost host=CreateHostBuilder(args).Build();
host.Run();
}
catch (Exception ex)
{ if (Log.Logger==null || Log.Logger.GetType().Name=="SilentLogger" )
{
Log.Logger=new LoggerConfiguration()
.MinimumLevel.Debug()
.WriteTo.Console()
.CreateLogger();
}

Log.Fatal(ex, "Host terminated unexpectedly" );
} finally {
Log.CloseAndFlush();
}
} private static IHostBuilder CreateHostBuilder ( string [] args )=> Host.CreateDefaultBuilder(args)
.UseServiceProviderFactory( new AutofacServiceProviderFactory(Register))
.ConfigureWebHostDefaults(webBuilder=>
{
webBuilder.UseStartup<Startup>()
.CaptureStartupErrors( true )
.ConfigureAppConfiguration(config=> { config.AddJsonFile( "appSettings.Local.json", optional: true ); })
.UseSerilog((hostingContext, loggerConfiguration)=>
{
loggerConfiguration
.ReadFrom.Configuration(hostingContext.Configuration)
.Enrich.FromLogContext()
.Enrich.WithProperty( "ApplicationName", typeof (Program).Assembly.GetName().Name)
.Enrich.WithProperty( "Environment", hostingContext.HostingEnvironment); # if DEBUG loggerConfiguration.Enrich.WithProperty( "DebuggerAttached", Debugger.IsAttached); # endif });
}); private static void Register ( ContainerBuilder builder )=> builder.RegisterLogger(autowireProperties: true );

} API - Startup.cs public class Startup { private IWebHostEnvironment CurrentEnvironment { get; } private IConfiguration Configuration { get; } private const string MyAllowSpecificOrigins="_myAllowSpecificOrigins"; public Startup ( IConfiguration configuration, IWebHostEnvironment env ) {
Configuration=configuration;
CurrentEnvironment=env;
} public void ConfigureServices ( IServiceCollection services ) {
services.AddLogging();

services.AddControllers()
.AddJsonOptions(options=>
{
options.JsonSerializerOptions.IgnoreNullValues=true;
options.JsonSerializerOptions.WriteIndented=true;
});

services.AddMvc(options=> options.EnableEndpointRouting=false )
.SetCompatibilityVersion(CompatibilityVersion.Version_3_0)
.AddXmlSerializerFormatters();

services.AddHealthChecks();

services.AddSwaggerGen(c=>
{
c.SwaggerDoc( "v1", new OpenApiInfo
{
Title="Api",
Version="v1",
Contact=new OpenApiContact
{
Name="Me",
Email="Me@Company.co",
Url=new Uri( "[https://internet](https://internet) exposed url/" )
}
});
});

services.AddDbContext<PrimaryDbContext>(options=> options.UseSqlServer(Configuration.GetConnectionString( "PrimaryConnection" )));

services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
.AddJwtBearer(options=>
{
options.TokenValidationParameters=new TokenValidationParameters
{
ValidateIssuer=true,
ValidateAudience=true,
ValidateLifetime=true,
ValidateIssuerSigningKey=true,
ValidIssuer=Configuration[ "Tokens:Issuer" ],
ValidAudience=Configuration[ "Tokens:Issuer" ],
IssuerSigningKey=new SymmetricSecurityKey(Encoding.UTF8.GetBytes(Configuration[ "Tokens:Key" ])),
ClockSkew=TimeSpan.Zero,
};
});

services.AddCors(options=> {
options.AddPolicy(MyAllowSpecificOrigins,
builder=> {
builder.AllowAnyOrigin();
});
});

services.AddMediatR( typeof (Startup));
services.RegisterAutoMapper();

services.Configure<SmtpSettings>(Configuration.GetSection( "SmtpSettings" ));
services.AddSingleton<IMailer, Mailer>();
services.AddSingleton<ISmtpServiceCustom, SmtpServiceCustom>();

RegisterServices(services);
ConfigureWorkflowService(services);
} public void Configure ( IApplicationBuilder app, IWebHostEnvironment env ) {
app.UseSwagger(); if (CurrentEnvironment.IsDevelopment())
{
app.UseDeveloperExceptionPage();
app.UseSwaggerUI(c=> { c.SwaggerEndpoint( "/swagger/v1/swagger.json", "Staging Api v1" ); });
} else {
app.UseSwaggerUI(c=> { c.SwaggerEndpoint( "v1/swagger.json", "Production Api v1" ); });
}

app.UseSerilogRequestLogging();

app.UseStaticFiles();
app.UseHttpActivities();
app.UseHttpsRedirection();
app.UseRouting();
app.UseCors(MyAllowSpecificOrigins);
app.UseAuthentication();
app.UseAuthorization();
app.UseHealthChecks( "/health", new HealthCheckOptions { ResponseWriter=JsonResponseWriter });
app.UseEndpoints(endpoints=> { endpoints.MapControllers(); });
} private static void RegisterServices ( IServiceCollection services )=> DependencyContainer.RegisterServices(services); private void ConfigureWorkflowService ( IServiceCollection services ) {
// Elsa setup
} private static Task JsonResponseWriter ( HttpContext context, HealthReport report ) {
context.Response.ContentType="application/json"; return JsonSerializer.SerializeAsync(context.Response.Body, new { Status=report.Status.ToString() }, new JsonSerializerOptions { PropertyNamingPolicy=JsonNamingPolicy.CamelCase });
}

} API Controller [ ApiController ]
[ Route( "api/[controller]" ) ]
[ EnableCors( "_myAllowSpecificOrigins" ) ] public class AttachmentController: ControllerBase { private readonly ILogger<AttachmentController> _logger; private readonly IBudgetReleaseRequestService _mainService; private readonly string _uploadFolderPath; public AttachmentController ( IWebHostEnvironment hostingEnvironment, ILogger<AttachmentController> logger, IBudgetReleaseRequestService mainService ) {
_logger=logger;
_mainService=mainService;
_uploadFolderPath=Path.Combine(hostingEnvironment.WebRootPath, "uploads" ); if (!Directory.Exists(_uploadFolderPath)) Directory.CreateDirectory(_uploadFolderPath);
}

[ HttpPost ]
[ Route( "UploadFileTelerik" ) ] public async Task<IActionResult> UploadFileTelerik ( IFormFile brrAttachment ) { if (brrAttachment==null ) return new EmptyResult(); try { var fileContent=ContentDispositionHeaderValue.Parse(brrAttachment.ContentDisposition); if (fileContent.FileName !=null )
{ var fileName=Path.GetFileName(fileContent.FileName.Trim( '"' )); var physicalPath=Path.Combine(_uploadFolderPath, fileName); await using var fileStream=new FileStream(physicalPath, FileMode.Create); await brrAttachment.CopyToAsync(fileStream);
}
}
catch
{ // Implement error handling here, this example merely indicates an upload failure. Response.StatusCode=500; await Response.WriteAsync( "some error message" ); // custom error message } // Return an empty string message in this case return new EmptyResult();
}

[ HttpPost ] public ActionResult Remove ( string fileToRemove ) { if (fileToRemove==null ) return new EmptyResult(); try { var fileName=Path.GetFileName(fileToRemove); var physicalPath=Path.Combine(_uploadFolderPath, fileName); if (System.IO.File.Exists(physicalPath))
{
System.IO.File.Delete(physicalPath);
}
}
catch
{
Response.StatusCode=500;
Response.WriteAsync( "some error message" );
} return new EmptyResult();
} # region Private private static string GetMimeTypeFromExtension ( string fileDtoFileExtension ) { return fileDtoFileExtension switch { ".txt"=> "text/plain", ".png"=> "image/png", ".jpeg"=> "image/jpeg", ".jpg"=> "image/jpeg", ".doc"=> "application/vnd.ms-word", ".docx"=> "application/vnd.openxmlformats-officedocument.wordprocessingml.document", ".xls"=> "application/vnd.ms-excel", ".xlsx"=> "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", ".ppt"=> "application/vnd.ms-powerpoint", ".pptx"=> "application/vnd.openxmlformats-officedocument.presentationml.presentation", ".pdf"=> "application/pdf",
_=> "application/octet-stream" };
} # endregion } Portal - Program.cs public class Program { public static void Main ( string [] args ) { try { using IHost host=CreateHostBuilder(args).Build();
host.Run();
}
catch (Exception ex)
{ if (Log.Logger==null || Log.Logger.GetType().Name=="SilentLogger" )
{
Log.Logger=new LoggerConfiguration()
.MinimumLevel.Debug()
.WriteTo.Console()
.CreateLogger();
}

Log.Fatal(ex, "Host terminated unexpectedly" );
} finally {
Log.CloseAndFlush();
}
} public static IHostBuilder CreateHostBuilder ( string [] args )=> Host.CreateDefaultBuilder(args)
.UseServiceProviderFactory( new AutofacServiceProviderFactory(Register))
.ConfigureWebHostDefaults(webBuilder=>
{
webBuilder.UseStartup<Startup>()
.CaptureStartupErrors( true )
.ConfigureAppConfiguration(config=> { config.AddJsonFile( "appsettings.Local.json", optional: true ); })
.UseSerilog((hostingContext, loggerConfiguration)=> {
loggerConfiguration
.ReadFrom.Configuration(hostingContext.Configuration)
.Enrich.FromLogContext()
.Enrich.WithProperty( "ApplicationName", typeof (Program).Assembly.GetName().Name)
.Enrich.WithProperty( "Environment", hostingContext.HostingEnvironment); # if DEBUG loggerConfiguration.Enrich.WithProperty( "DebuggerAttached", Debugger.IsAttached); # endif });
}); private static void Register ( ContainerBuilder builder )=> builder.RegisterLogger(autowireProperties: true );

} Portal - Startup.cs public class Startup { private IWebHostEnvironment CurrentEnvironment { get; } private IConfiguration Configuration { get; } public Startup ( IConfiguration configuration, IWebHostEnvironment env ) {
Configuration=configuration;
CurrentEnvironment=env;
} public void ConfigureServices ( IServiceCollection services ) {
services.AddLogging();
services.AddRazorPages();

services.AddResponseCompression(options=> {
options.EnableForHttps=true;
options.MimeTypes=new [] { "text/plain", "text/css", "application/javascript", "text/html", "application/xml", "text/xml", "application/json", "text/json" };
}); if (CurrentEnvironment.IsDevelopment() || Configuration[ "DeveloperHacks:ExtraException" ]=="1" )
{
services.AddServerSideBlazor(o=> o.DetailedErrors=true );
} else {
services.AddServerSideBlazor(o=> o.DetailedErrors=true )
.AddHubOptions(options=>
{
options.ClientTimeoutInterval=TimeSpan.FromMinutes( 10 );
options.KeepAliveInterval=TimeSpan.FromSeconds( 3 );
options.HandshakeTimeout=TimeSpan.FromMinutes( 10 );
});
}

services.AddHeadElementHelper();
services.AddBlazorDragDrop();
services.AddDevExpressBlazor();
services.AddTelerikBlazor();

services.AddAuthentication(sharedOptions=>
{
sharedOptions.DefaultAuthenticateScheme=CookieAuthenticationDefaults.AuthenticationScheme;
sharedOptions.DefaultSignInScheme=CookieAuthenticationDefaults.AuthenticationScheme;
sharedOptions.DefaultSignOutScheme=CookieAuthenticationDefaults.AuthenticationScheme;
sharedOptions.DefaultChallengeScheme=OpenIdConnectDefaults.AuthenticationScheme;
})
.AddOpenIdConnect(options=>
{
options.ClientId=Configuration[ "Okta:ClientId" ];
options.ClientSecret=Configuration[ "Okta:ClientSecret" ];
options.Authority=Configuration[ "Okta:Issuer" ];
options.CallbackPath="/authorization-code/callback";
options.ResponseType="code";
options.SaveTokens=true;
options.UseTokenLifetime=false;
options.GetClaimsFromUserInfoEndpoint=true;
options.TokenValidationParameters.ValidateIssuer=false;
options.TokenValidationParameters.NameClaimType="name";
options.Scope.Add( "openid" );
options.Scope.Add( "profile" );
})
.AddCookie();

services.AddMediatR( typeof (Startup));

RegisterServices(services);
} public void Configure ( IApplicationBuilder app, IWebHostEnvironment env ) { if (env.IsDevelopment())
{
app.UseDeveloperExceptionPage();
} else {
app.UseExceptionHandler( "/Error" );
app.UseHsts();
}

app.UseSerilogRequestLogging();

app.UseHeadElementServerPrerendering();

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthentication();
app.UseAuthorization();

app.UseEndpoints(endpoints=>
{
endpoints.MapBlazorHub();
endpoints.MapFallbackToPage( "/_Host" );
});
} private void RegisterServices ( IServiceCollection services ) { var baseAddress=Configuration[ "ApiSetup:BaseAddress" ]; // value: [http://localhost:8082/](http://localhost:8082/)

services.AddHttpClient<ILookupService, LookupService> (client=> { client.BaseAddress=new Uri(baseAddress); });
services.AddHttpClient<IBusinessLookupService, BusinessLookupService> (client=> { client.BaseAddress=new Uri(baseAddress); });
services.AddHttpClient<IApiUserService, ApiUserService> (client=> { client.BaseAddress=new Uri(baseAddress); });
services.AddHttpClient<IRequestService, RequestService> (client=> { client.BaseAddress=new Uri(baseAddress); });
services.AddHttpClient<IResourceService, ResourceService> (client=> { client.BaseAddress=new Uri(baseAddress); });
services.AddHttpClient<IApproverTemplateService, ApproverTemplateService>(client=> { client.BaseAddress=new Uri(baseAddress); });
services.AddHttpClient<IAttachmentService, AttachmentService> (client=> { client.BaseAddress=new Uri(baseAddress); });
}

} Razor Page: @page "/request-handle"
@page "/authorization-code/request-handle"

@page "/request-handle/{requestId:long}"
@page "/authorization-code/request-handle/{requestId:long}"

@page "/request-handle/{requestId:long}/{actorId}"
@page "/authorization-code/request-handle/{requestId:long}/{actorId}"

@page "/request-handle/{requestId:long}/{actionId:guid}"
@page "/authorization-code/request-handle/{requestId:long}/{actionId:guid}"

@inherits RequestHandleModel

@attribute [Authorize] <PageHeader PageTitle="Release Request" AreaName="Request"> </PageHeader> @if (Model !=null)
{ <EditForm Context="_" OnValidSubmit="@HandleValidSubmit" EditContext="@EditContextCustom"> <DataAnnotationsValidator /> <DxFormLayout CssClass="dxFormLayoutHeaderStyle" CaptionPosition="CaptionPosition.Vertical"> <DxFormLayoutItem ColSpanMd="12"> <Template> <ValidationSummary /> </Template> </DxFormLayoutItem> <DxFormLayoutGroup Caption="Files" ColSpanMd="12"> <DxFormLayoutItem Caption="" ColSpanMd="12"> <Template> <TelerikUpload SaveUrl="@FileUploaderUrlT" SaveField="brrAttachment" RemoveField="fileToRemove" AllowedExtensions="@(new List<string> {".jpg ", ".jpeg ", ".png ", ".pdf ", ".xlsx ", ".xls ", ".doc ", ".docx "})" MaxFileSize="26214400" MinFileSize="1024"> </TelerikUpload> </Template>
</DxFormLayoutItem> </DxFormLayoutGroup> </DxFormLayout> </EditForm> }
else
{ <p> @LoadingMessage </p> } <TelerikLoaderContainer Size="LoaderSize.Large" OverlayThemeColor="dark" LoaderPosition="LoaderPosition.Top" Text="Please wait..." LoaderType="LoaderType.ConvergingSpinner" Visible="@LoaderContainerVisible" /> <TelerikNotification Class="high-zindex" @ref="@Notification" AnimationType="AnimationType.Fade" AnimationDuration="300" /> Razor CodeBehind: protected string FileUploaderUrlT=$" {ConfigHelper[ "ApiSetup:BaseAddress" ]} api/Attachment/UploadFileTelerik"; // where ApiSetup:BaseAddress=> // [http://localhost:8082/](http://localhost:8082/) Through the portal, the registered clients work perfectly. However, the Upload Control fails at uploading a file: Details: Preflight Details: XHR The request URL is perfectly correct. The API server is never hit. This setup works fine on my dev machines. It fails only when on staging or production. I cannot expose the API in any other way. I am looking at these two topics as I'm searching: Upload component reports 'File failed to upload' File Upload fails with error 404 in API call Any hep will be appreciated.

## Answer

**Marin Bratanov** answered on 08 May 2021

Hi Hassan, From what I gather, the api at localhost:8020 is accessible only from the server (which probably includes your dev machine since you have everything running locally while developing). The Upload component does not make the request from the blazor app, it makes it from the browser. This is a truly asynchronous file upload that issues an HTTP call from the browser to the designated endpoint. This means that the browser (the client) needs to be able to call the API, and in your case it seems that the API is not available. The SaveUrl provided is localhost which means that the Upload component will try to send the file to the local computer where the browser runs, it will never get to the server. So, if you cannot expose a secured API endpoint to receive files, you may actually need a FileSelect component to give you the file in the Blazor app itself, so it is actually on the server machine, from where you could save it to the disk or issue your own call to the API. Regards, Marin Bratanov Progress Telerik
