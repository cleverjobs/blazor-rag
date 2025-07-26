# Unable to load the service index for source https://nuget.telerik.com/v3/index.json.

## Question

**Cha** asked on 12 Sep 2022

Hi Team, I was working working telerik Blazor UI from 3 months, But suddenly i started to get the below exception, whenever i was restoring nuget package. Unable to load the service index for source [https://nuget.telerik.com/v3/index.json.](https://nuget.telerik.com/v3/index.json.) Response status code does not indicate success: 401 (Unauthorized). is it happening due to licensee key expiry ?

## Answer

**Dimo** answered on 13 Sep 2022

Hello Chandradev, It looks like you have previously installed a trial version of UI for Blazor ( Telerik.UI.for.Blazor. Trial NuGet package). Now you have a license, so install and use the commercial version ( Telerik.UI.for.Blazor NuGet package). Check our NuGet feed troubleshooting page. Also check which Telerik account you are using for the Progress Control Panel and the NuGet source. Regards, Dimo
