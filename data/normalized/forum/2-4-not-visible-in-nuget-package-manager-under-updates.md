# 2.4 not visible in NuGet package manager under updates

## Question

**Rob** asked on 20 Nov 2019

Hi, I have just updated to v2.3 but I dont see version 2.4 in my NuGet package manager. I have check "Include prerelease" but I get "No packages found". I have updated all my Microsoft.AspNetCore.* packages to 3.1.0.-preview3.19555.2

## Answer

**Marin Bratanov** answered on 20 Nov 2019

Hello Robert, If your trial period has expired, the nuget feed may not allow you to download anymore. A way to check if this is the case is to go to your account and see if you have the 2.4.0 ZIP archive so you can create a local feed: [https://docs.telerik.com/blazor-ui/installation/zip](https://docs.telerik.com/blazor-ui/installation/zip) Regards, Marin Bratanov
