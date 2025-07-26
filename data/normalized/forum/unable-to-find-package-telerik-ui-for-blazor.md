# Unable to find package Telerik.UI.for.Blazor

## Question

**Tol** asked on 22 Jan 2020

Environment: VS 2019 w/ all latest updates. Installed Telerik UI For Blazor through Progress Control Panel. Attempting to create new Telerik Blazor solution, or add new Telerik Blazor project to existing solution, yields the following error: NU1101 Unable to find package Telerik.UI.for.Blazor. No packages exist with this id in source(s): Local Packages, Microsoft Visual Studio Offline Packages, nuget.org Restarted VS as well as machine, same error. Instructions on how to resolve would be appreciated.

## Answer

**Marin Bratanov** answered on 22 Jan 2020

Hello Michael, From the list of feeds where VS looked for our package, it looks like the Telerik feed through which our UI for Blazor package is distributed, is not add on the machine. Here's how to add it: [https://docs.telerik.com/blazor-ui/installation/nuget](https://docs.telerik.com/blazor-ui/installation/nuget) Alternatively, you can use a local feed: [https://docs.telerik.com/blazor-ui/installation/zip](https://docs.telerik.com/blazor-ui/installation/zip) You can find more details on what you need to get things running in this article: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need](https://docs.telerik.com/blazor-ui/getting-started/what-you-need) If you prefer tutorials, here are two: WASM apps: [https://docs.telerik.com/blazor-ui/getting-started/client-blazor](https://docs.telerik.com/blazor-ui/getting-started/client-blazor) server Blazor apps: [https://docs.telerik.com/blazor-ui/getting-started/server-blazor](https://docs.telerik.com/blazor-ui/getting-started/server-blazor) Regards, Marin Bratanov

### Response

**Rob** commented on 11 Oct 2024

I know this is an old post, but the solutions offered didn't work for me either and they seem to be incorrect. Removing the NuGet.Config after following Steps 1 to 4 makes no sense as those steps actually create the NuGet.Config file ... just chasing your tail if I follow those directions. Tell me to create the file, then next steps to delete file?? The issue is that I never get prompted to enter my Telerik Account credentials. I don't understand the point of the Telerik Control Panel and selecting products to install if it doesn't actually install what is need to run a project using Telerik UI Blazor? Rob.

### Response

**Lance | Senior Manager Technical Support** commented on 14 Oct 2024

Hi Rob, That is a valid question and is sometimes a point of confusion. Let me explain the difference between the nuget packages vs local installation of the entire product, this will help you understand the decision you will want to make in the future. It's good to step back and understand the difference between stuff that needs to be installed locally, and stuff that comes solely from NuGet. Telerik UI for Blazor provides NuGet packages, which means you do not need to install anything using the Progress Control Panel. You can just add the Telerik NuGet server to your nuget.config and that's all that is needed for a project to add the references. So, then what is the point of using the Progress Control Panel, and select "UI for Blazor" in there? That's how you get the Visual Studio Extensions, local demos, offline package sources/assemblies, and more. These will get installed to C:\Program Files (x86)\Progress\Telerik UI for Blazor [version] \. Therefore at the end of the day, you're kind of doing two things (local product install and project-independent package add), but only the latter is necessary. I hope this helps explain things, let me know if you have any further questions. Side Note Just as an experiment, try using the Telerik UI for Blazor project wizard for a quick throwaway project. You'll see int he wizard, we let you choose the package source for where the nuget.confgi will add a source. You might be asking yourself "why would I use the Telerik server if I can add a local folder path to my nuget.config as a package source?". This depends on where that project is going to live. If it's only going to ever be on your PC, and you are never going to change the local installed version, then it's fine. However, if you plan on building this project in CI-Cd (Azure DevOps, GitHub Actions, etc), then you'll prefer using the nuget server as a package source because that project can restore packages from everywhere it can be compiled. You can see this article for information on authentication the connection from CI Restoring NuGet Packages in CI - Telerik UI for Blazor.

### Response

**ToltingColtAcres** answered on 22 Jan 2020

that worked, great, thanks. Next issue: After building the skeleton template installed through extensions -> Telerik -> Telerik UI for Blazor -> Create new project running the resulting build yields a web page that simply says "Loading..." and nothing else... Any idea?

### Response

**Marin Bratanov** answered on 22 Jan 2020

Can you confirm the startup project is the .Server project in the WASM solution? I'm also attaching a solution I created with the VS extensions and it works fine for me, so you can compare against it (e.g., with a tool like WinMerge to see what is the differences between the project you have that fails, and this one). The loading sign not disappearing in a WASM app indicates that something fails during loading of the assets and/or a JS error is thrown, but what is the exact error and its cause is hard to tell based on the available information. If comparing against the sample here does not help, please open a support ticket and send me the sample project that fails so I can have a look at it. Regards, Marin Bratanov

### Response

**ToltingColtAcres** answered on 22 Jan 2020

ok I'll take a look. no errors on build or startup that I can determine. info: Microsoft.AspNetCore.DataProtection.KeyManagement.XmlKeyManager[0] User profile is available. Using 'C:\Users\tca\AppData\Local\ASP.NET\DataProtection-Keys' as key repository and Windows DPAPI to encrypt keys at rest. Hosting environment: Development Content root path: D:\Development\MyApp\MyApp.Admin\Server Now listening on: [http://localhost:62354](http://localhost:62354) Application started. Press Ctrl+C to shut down. info: Microsoft.AspNetCore.Hosting.Diagnostics[1] Request starting HTTP/1.1 GET [http://localhost:62354/](http://localhost:62354/) info: Microsoft.AspNetCore.Routing.EndpointMiddleware[0] Executing endpoint 'Fallback {*path:nonfile}' info: Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware[2] Sending file. Request path: '/index.html'. Physical path: 'D:\Development\MyApp\MyApp.Admin\Client\wwwroot\index.html' info: Microsoft.AspNetCore.Routing.EndpointMiddleware[1] Executed endpoint 'Fallback {*path:nonfile}' info: Microsoft.AspNetCore.Hosting.Diagnostics[2] Request finished in 169.9494ms 200 text/html info: Microsoft.AspNetCore.Hosting.Diagnostics[1] Request starting HTTP/1.1 GET [http://localhost:62354/css/site.css](http://localhost:62354/css/site.css) info: Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware[2] Sending file. Request path: '/css/site.css'. Physical path: 'D:\Development\MyApp\MyApp.Admin\Client\wwwroot\css\site.css' info: Microsoft.AspNetCore.Hosting.Diagnostics[2] Request finished in 9.4318ms 200 text/css info: Microsoft.AspNetCore.Hosting.Diagnostics[1] Request starting HTTP/1.1 GET [http://localhost:62354/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js](http://localhost:62354/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js) info: Microsoft.AspNetCore.Hosting.Diagnostics[1] Request starting HTTP/1.1 GET [http://localhost:62354/_framework/blazor.webassembly.js](http://localhost:62354/_framework/blazor.webassembly.js) info: Microsoft.AspNetCore.Hosting.Diagnostics[1] Request starting HTTP/1.1 GET [http://localhost:62354/css/bootstrap/bootstrap.min.css](http://localhost:62354/css/bootstrap/bootstrap.min.css) info: Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware[2] Sending file. Request path: '/_framework/blazor.webassembly.js'. Physical path: 'D:\Development\MyApp\MyApp.Admin\Client\bin\Debug\netstandard2.1\dist\_framework\blazor.webassembly.js' info: Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware[2] Sending file. Request path: '/css/bootstrap/bootstrap.min.css'. Physical path: 'D:\Development\MyApp\MyApp.Admin\Client\wwwroot\css\bootstrap\bootstrap.min.css' info: Microsoft.AspNetCore.Hosting.Diagnostics[2] Request finished in 20.1225ms 200 text/css info: Microsoft.AspNetCore.Hosting.Diagnostics[2] Request finished in 71.0469ms 200 application/javascript info: Microsoft.AspNetCore.StaticFiles.StaticFileMiddleware[2] Sending file. Request path: '/_content/Telerik.UI.for.Blazor/js/telerik-blazor.js'. Physical path: 'C:\Users\tca\.nuget\packages\telerik.ui.for.blazor\2.6.1\staticwebassets\js\telerik-blazor.js' info: Microsoft.AspNetCore.Hosting.Diagnostics[1] Request starting HTTP/1.1 GET [http://localhost:62354/css/open-iconic/font/css/open-iconic-bootstrap.min.css](http://localhost:62354/css/open-iconic/font/css/open-iconic-bootstrap.min.css)

### Response

**Marin Bratanov** answered on 23 Jan 2020

Hello, It does not look like there are any errors here, but you can still check the browser console for runtime errors that can break the app, and for broken network requests (things like proxies, firewalls, antivirus programs can tamper with the browser requests and break them even if the server returns them properly). Without being able to see, read and debug the code, I can only guess and I would encourage you to open a ticket if this issue persists so I can take a look and avoid further guesswork. Regards, Marin Bratanov

### Response

**ToltingColtAcres** answered on 23 Jan 2020

Well your sample app didn't work either... same issue. Very strange.

### Response

**Marin Bratanov** answered on 23 Jan 2020

Do you get any errors in the browser console? Perhaps one of these: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors?](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors?) Does a WASM project work on your end without the Telerik components? Regards, Marin Bratanov

### Response

**James** answered on 17 Aug 2020

Why is it such a mission to add Telerik newget packages ?? I dont have to go through hoops for any other third party providers to install or update nuget packages this is very frustrating and a waste of my time

### Response

**FRANK** commented on 29 Dec 2023

I could not agree more. Why do you waste people's time when they're already focused on their project (not learning your specific way to do things!). if the same is true for your controls, then this trial will end very rapidly!

### Response

**Marin Bratanov** answered on 17 Aug 2020

I am sorry that you are having a hard time with our packages, James. What we provide is the following: a private feed that you can add globally for your machine (see also the troubleshooting information in the article): [https://docs.telerik.com/blazor-ui/installation/nuget.nupkg](https://docs.telerik.com/blazor-ui/installation/nuget.nupkg) files that you can use as local custom package sources: [https://docs.telerik.com/blazor-ui/installation/zip](https://docs.telerik.com/blazor-ui/installation/zip) The second approach should be quite easy as it merely requires copying files to a shared folder and pointing your nuget.config file that way. The first approach with our private feed is a tad mode complicated than with "regular" packages because: most free products are on nuget.org which is a package source that Visual Studio sets up for you - you don't have to do it yoursefl, like any other custom package source our components and software are not free, so they cannot be available from a free package source like nuget.org - this requires that we provide a private one, and that, inevitably, requires a bit of setup Regards, Marin Bratanov

### Response

**FRANK** commented on 29 Dec 2023

Then you should do all of that for us in your install program! Or, at least provide EASY instructuions.. Not make us go to google to find out why there are errors. or, better still, INSTALL THE PACKAGES FROM YOUR INSTALLER!

### Response

**Lance | Senior Manager Technical Support** commented on 02 Jan 2024

Hi Frank, We do have easy to follow instructions on how to add the Telerik Server to you package sources here=> Telerik NuGet Feed - Telerik UI for Blazor That being said, our installer does add a local package source for you, however, since you're having trouble with it, I imagine that's why you're missing the local source. So, I would recommend following the instructions in that link to add the Telerik NuGet server so you can get up and running quickly. Ticket Escalation I would like to also share that I've spoken with Seth, and I have escalated your situation to both the UI for Blazor and the Visual Studio Extensions support teams. You will have already gotten an email notification saying that a Support Ticket was opened for you (that was me, it is ticket #1635933). Those teams are treating the case with priority, so you will get a quicker response than typical trial support response times. Additional Assistance If you have any questions in the meantime, please feel free to open the Support Ticket and post additional context about the current issue. Alternatively, you can open a new Support Ticket to get fast parallel assistance in different topics. You can see your current Technical Support tickets here=> [https://www.telerik.com/account/support-center](https://www.telerik.com/account/support-center) You can open a new Technical Support ticket here=> [https://www.telerik.com/account/support-center/contact-us](https://www.telerik.com/account/support-center/contact-us) I will be keeping a close eye on things to make sure there is smooth transition/communication across any relevant teams needed to assist you.

### Response

**Rustam** commented on 18 Jun 2025

Hi, I am unable to restore NuGet packages for my Blazor project using Telerik UI for Blazor. When I run dotnet restore, I consistently receive error NU1301: Failed to retrieve information about 'Telerik.*' packages from the source [https://nuget.telerik.com/blazor-ui-dev/.](https://nuget.telerik.com/blazor-ui-dev/.) The specific error is Response status code does not indicate success: 503 (Service Unavailable). This issue is preventing my project from building. The NuGet feed was accessible and working fine recently. Could you please check the status of the [https://nuget.telerik.com/blazor-ui-dev/](https://nuget.telerik.com/blazor-ui-dev/) NuGet feed? Any information on this outage or advice on how to resolve this would be greatly appreciated. Thank you.

### Response

**Lance | Senior Manager Technical Support** commented on 18 Jun 2025

HI Rustam, Where did you get that URL to the server? The correct path is [https://nuget.telerik.com/vs/index.json,](https://nuget.telerik.com/vs/index.json,) this is for every product and every service. You can learn more about the server URL, setting credential, package source mapping and more here=> [https://www.telerik.com/blazor-ui/documentation/installation/nuget.](https://www.telerik.com/blazor-ui/documentation/installation/nuget.)
