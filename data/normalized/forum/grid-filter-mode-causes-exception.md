# Grid filter mode causes exception

## Question

**Eri** asked on 24 Oct 2019

I am seeing that the grid filter mode causes the following exception to be thrown: "System.InvalidOperationException: JavaScript interop calls cannot be issued at this time. This is because the component is being prerendered and the page has not yet loaded in the browser or because the circuit is currently disconnected. Components must wrap any JavaScript interop calls in conditional logic to ensure those interop calls are not attempted during prerendering or while the client is disconnected." Steps to reproduce (project using example from [https://docs.telerik.com/blazor-ui/components/grid/overview](https://docs.telerik.com/blazor-ui/components/grid/overview) is at [https://github.com/austineric/GridTest](https://github.com/austineric/GridTest) ): Open solution Ctrl + F5 In the address bar add "/test" to the url In Visual Studio change the output to "GridTest - ASP.NET Core Web Server" Clear All in the output window Refresh the browser page View the exception in the output window Run the same test but remove the "FilterMode="Telerik.Blazor.GridFilterMode.FilterRow"" and see that the exception does not appear Error produced using.Net Core 3.0.100 Telerik UI for Blazor 2.2.1 Visual Studio 16.3.5 The grid appears to be working and filtering correctly despite the exception. Should I disregard? Should I be doing something differently?

## Answer

**Marin Bratanov** answered on 25 Oct 2019

Hi Eric, The upgrade to .NET Core 3.1 should also include an upgrade to netcoreapp3. 1 from netcoreapp3.0 as per the MS blog post (see the "Upgrade an existing project" section): [https://devblogs.microsoft.com/aspnet/asp-net-core-updates-in-net-core-3-1-preview-1/.](https://devblogs.microsoft.com/aspnet/asp-net-core-updates-in-net-core-3-1-preview-1/.) This removes the exception on my end. I created a pull request with the fix: [https://github.com/austineric/GridTest/pull/1](https://github.com/austineric/GridTest/pull/1) Regards, Marin Bratanov
