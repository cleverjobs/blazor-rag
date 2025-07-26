# Unable to update through nuget: Blazor 4.5.0+

## Question

**Ric** asked on 26 Oct 2023

I am starting a new project and went to download the latest version of Blazor from nuget and I get the following error: GET [https://nuget.telerik.com/v3/package/telerik.fonticons/index.json](https://nuget.telerik.com/v3/package/telerik.fonticons/index.json) GET [https://nuget.telerik.com/v3/package/telerik.svgicons/index.json](https://nuget.telerik.com/v3/package/telerik.svgicons/index.json) OK [https://nuget.telerik.com/v3/package/telerik.fonticons/index.json](https://nuget.telerik.com/v3/package/telerik.fonticons/index.json) 6039ms OK [https://nuget.telerik.com/v3/package/telerik.svgicons/index.json](https://nuget.telerik.com/v3/package/telerik.svgicons/index.json) 6037ms NU1101: Unable to find package Telerik.FontIcons. NU1101: Unable to find package Telerik.SvgIcons. Package restore failed. The last version I can successfully download is Telerik.UI.for.Blazor 4.4.0. Everything after that seems to have an issue with the icon dependencies. Anyone have any thoughts on what I might be missing, has anyone else been able to successfully start a new project with 4.5.0 or higher?

## Answer

**Rick** answered on 26 Oct 2023

I found the solution; those libraries are published to nuget instead of the Telerik feed. Updated source mapping and that fixed it.

### Response

**Hristian Stefanov** commented on 27 Oct 2023

Hi Rick, I'm happy to see you quickly found the solution on your own. Thank you for sharing it here, publicly, so other developers can benefit from it. Kind Regards, Hristian
