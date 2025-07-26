# Telerik demo using Blazor WebAssembly AoT

## Question

**Jon** asked on 27 May 2021

Hello, Yesterday, ASP.NET Core, the web-dev component of .NET, received a new functionality in the new NET. 6 Preview 4: Ahead-of-Time (AoT) compilation for Blazor WebAssembly. Do you plan to update current Telerik Blazor demo to confirm that AoT will drastically enhance Telerik Blazor control execution speed ? Thanks. Jonathan.

## Answer

**Marin Bratanov** answered on 27 May 2021

Hello Jonathan, Our demo site uses the server-side flavor, so it does not run on WebAssembly where that could be applicable. Thus, any slowdown you may experience is more likely to be related to network latency between your browser and our server where the app actually runs. We will be looking into how AoT works out a bit later (definitely for the official release and support of .NET 6). If you do find any issues with AoT and our components, let us know. Regards, Marin Bratanov
