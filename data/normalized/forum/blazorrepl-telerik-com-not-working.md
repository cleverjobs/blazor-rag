# blazorrepl.telerik.com not working

## Question

**Cla** asked on 12 May 2022

Opening the page it return this error on chrome console: System.AggregateException: One or more errors occurred. (Could not load list of method overrides due to Method not found: System.Collections.Generic.IList`1<Microsoft.Extensions.Configuration.IConfigurationSource> Microsoft.Extensions.Configuration.IConfigurationBuilder.get_Sources()) ---> System.TypeLoadException: Could not load list of method overrides due to Method not found: System.Collections.Generic.IList`1<Microsoft.Extensions.Configuration.IConfigurationSource> Microsoft.Extensions.Configuration.IConfigurationBuilder.get_Sources() at Microsoft.AspNetCore.Components.WebAssembly.Hosting.WebAssemblyHostBuilder.CreateDefault(String[] args) at BlazorRepl.Client.Program.Main(String[] args) --- End of inner exception stack trace --- callEntryPoint @blazor.webassembly.js:1 VM262:1 Uncaught ReferenceError: webVitals is not defined at <anonymous>:1:313 at gtm.js?id=GTM-6X92:502:414 at HTMLScriptElement.<anonymous> (gtm.js?id=GTM-6X92:503:118)

### Response

**Claudio** commented on 12 May 2022

nevigate in private mode seem to solve...

## Answer

**Dimo** answered on 16 May 2022

Hi Claudio, This might be a caching issue after a REPL update. Sorry about the trouble. Did this occur with any REPL example, or a specific one only? I should also point out that we uploaded a new REPL version yesterday with some fixes. Generally, the first thing to try is a hard reload or cache clear. Let us know if any problem persists. Regards, Dimo
