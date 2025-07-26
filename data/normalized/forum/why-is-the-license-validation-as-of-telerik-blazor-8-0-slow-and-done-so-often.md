# Why is the license validation as of Telerik Blazor 8.0 slow and done so often?

## Question

**JimJim** asked on 20 Mar 2025

My team has noticed a significant increase in build times for our Visual Studio 2022 solution since the 8.0 update. It got marginally better with 8.1.1 but still much slower than before. We have about 6 projects in the solution that reference the Telerik UI for Blazor libraries. Each of these projects appears to be doing its own license validation step. The step takes 5-10 seconds per project so adds 30-60 seconds to the build time. This wouldn't be that onerous, but this is done with every single build, even incremental builds. So the edit/compile/test cycle has gotten significantly slower, impacting productivity negatively. Can something be done to make this less onerous? Maybe checking once per Visual Studio session? Once a day?

## Answer

**Dimo** answered on 25 Mar 2025

Hello Jim, We have another ticket from your company (1682020), which is on the same topic and was closed yesterday by your colleague with a confirmation that there was some other setup issue, which caused unnecessary rebuilds and a longer app build time overall. On the other hand, I confirm that a few additional seconds per clean build per project are expected. Afterwards, there is caching, which should make the project builds faster. Regards, Dimo

### Response

**Jim** commented on 25 Mar 2025

Yes, Dimo, we discovered that yesterday. In addition we found that "extra" licensing checks could be avoided by use of the "Removed Unused References" feature in Visual Studio. I think this is somewhat poorly named as one of the things it does is remove "transitive" references. So if Project1 uses Telerik.Blazor, Project2 uses Telerik.Blazor, and Project1 uses Project2, then it will remove the direct reference in Project1, avoiding the license check for Project1. So either way, I think we are good to on this topic. Thanks, Jim
