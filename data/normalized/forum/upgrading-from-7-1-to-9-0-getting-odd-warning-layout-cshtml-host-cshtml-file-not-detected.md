# Upgrading from 7.1 to 9.0 getting odd warning Layout.cshtml/Host.cshtml file not detected?

## Question

**RobRob** asked on 04 Jun 2025

I have a _Host.cshtml (underscore) not a Host.cshtml. The information provided is pretty generic "manually update your code after the wizard completes"? Not much of a wizard, what exactly do I need to manually update? Rob.

## Answer

**Maria** answered on 06 Jun 2025

Hello Rob, Thank you for the additional info. The issue comes from the target framework of the project. Currently, the Server project type is supported only for .NET 6. We deprecated the support for .NET 6 in our latest release. The logic in the Upgrade Wizard is based on the project type and target framework. When you update the project’s target framework to .NET 9, the Upgrade Wizard identifies the application as a WebApp project. Detection for this project type differs because the project structure and files it contains are distinct. This is where the error arises, as it cannot locate the Layout.cshtml and Host.cshtml files. If you want to stay in the current setup for your project - Server project type and .NET 9 target framework, you need to upgrade your project manually. The steps for the manual upgrade are provided in my previous reply. Let me know if I can assist you further. Regards, Maria Progress Telerik

### Response

**Maria** answered on 05 Jun 2025

Hеllo Rob, Thank you for the image provided. For the warning that displays in the wizard, I will need some additional information. Could you please specify the type of project you want to upgrade and its target framework? For the manual upgrade process, you can perform the steps provided in our documentation article. Please refer here: Manual Upgrade Process. I hope this information is useful. Looking forward to your reply with the additional details for the project. Regards, Maria Progress Telerik

### Response

**Rob** commented on 05 Jun 2025

Hi Maria, .NET 9 Blazor-Server app Looking at your manual upgrade process: 1. Yes, feed is working and 9.0.0 was downloaded 2. N/A 3. Tried manual "Update" for the Package: 4. We're using (not CDN): @{
var telerikUiForBlazorVersion=typeof(TelerikRootComponent).Assembly.GetName().Version;
} <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js?@telerikUiForBlazorVersion"> </script> 5. N/A 6. Using TailwindCSS and override Telerik (contractors setup we may change this in the future) 7. N/A we have no .resx files 8. Already implemented I was able to eventually solve the issue; there was another update to VS 2022 17.14.4 (oddly the update didn't change the VS version number?). Installed the VS update. Then I manually removed the duplicate entries in the csproj files: Performed a Solution "Clean". Then performed a solution Rebuild and this time it worked. On a side note (not related to this specific task but might be a clue), when running Telerik Extensions "update", nothing happened on exit of VS 2022 ... the extension update was NOT install. So I loaded VS 2022 again, and went to the menu to run Telerik Extensions update again, and the 2nd time the extension did run after VS 2022 closed. Rob
