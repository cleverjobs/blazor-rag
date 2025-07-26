# How can I change the background color of a predefined dialog box.

## Question

**Dou** asked on 04 Apr 2023

The background of the predefined dialog box appears transparent.

## Answer

**Dimo** answered on 07 Apr 2023

Hi Doug, The CSS theme file is outdated or the older version is cached. Please see this forum thread about Dialog background. Regards, Dimo Progress Telerik

### Response

**Doug** commented on 07 Apr 2023

I still have the same results. I found only this line to modify from 3.5.0 to 4.1.0. <link rel="stylesheet" href="[https://blazor.cdn.telerik.com/blazor/4.1.0/kendo-theme-default/all.css"](https://blazor.cdn.telerik.com/blazor/4.1.0/kendo-theme-default/all.css") /> This is an update from Trial to a paid version. I followed the instructions for the upgrading from trial to paid a while ago. Any suggestions?

### Response

**Dimo** commented on 10 Apr 2023

Clear the browser cache. Make sure that there is only one registered Telerik CSS theme in the app. Make sure that the CSS file version matches the NuGet package version (i.e. both are 4.1.0). If the problem persists, check the browser's DOM inspector for conflicting CSS styles that may be breaking the Dialog's appearance. If you are not comfortable with step (4), then remove all other CSS files from the app to see if this fixes the Dialog appearance. If the problem still persists, send us a live URL or a runnable project for inspection.

### Response

**Doug** commented on 12 Apr 2023

Please excuse my ignorance on a few things. I'm new to web app development. 1. I cleared the cache. 2. Is the css them registered in the _Layout_cshtml? It's as follows: <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <base href="~/" /> <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" /> <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> <link href="css/site.css" rel="stylesheet" /> <link href="tpCentralWeb.styles.css" rel="stylesheet" /> <component type="typeof(HeadOutlet)" render-mode="ServerPrerendered" /> <link href="@Url.Content("lib/blazor-ui/swatches/default-ocean-blue.css")" rel="stylesheet" type="text/css" /> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer></script> @* Report Viewer dependencies *@<script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js"></script> <script src="_content/Telerik.ReportViewer.BlazorNative/js/reporting-blazor-viewer.js"></script> <link rel="stylesheet" href="[https://blazor.cdn.telerik.com/blazor/4.1.0/kendo-theme-default/all.css"](https://blazor.cdn.telerik.com/blazor/4.1.0/kendo-theme-default/all.css") /> <link href="_content/Telerik.ReportViewer.BlazorNative/css/reporting-blazor-viewer.css" rel="stylesheet" /> 3. Would that be the Telerik.UI.for.Blazor package. if so, then they match. 4 Not familiar with DOM inspector, but looked around and I don't see anything that would break the Dialogs appearance. 5. I believe I successfully removed the all CSS files from the app and nothing changed. 6. The app has authentication, so is it secure to send a live URL and provide you with the username and password?

### Response

**Dimo** commented on 13 Apr 2023

Тhe app even registers 3 duplicate themes for the Blazor components: <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> <link href="@Url.Content("lib/blazor-ui/swatches/default-ocean-blue.css")" rel="stylesheet" type="text/css" /> <link rel="stylesheet" href="[https://blazor.cdn.telerik.com/blazor/4.1.0/kendo-theme-default/all.css"](https://blazor.cdn.telerik.com/blazor/4.1.0/kendo-theme-default/all.css") /> Of all these, you need just one. It should be compatible with both the Telerik UI for Blazor version and the Blazor ReportViewer version. Also remove one of the duplicate telerik-blazor.js files. And to answer your specific questions: OK. Based on the latest information, that wouldn't help. Yes, 3 times. Not necessarily. All 3 themes are registered in different ways and can be compatible with different Telerik UI for Blazor versions. Only static assets with a _content URL are surely compatible, because they are taken from the NuGet package itself. The others may or may not be. HTML, CSS and DOM inspector knowledge is required when using web components. Start from here (CSS knowledge) and here (CSS tools). This means that the breakage is not caused by custom CSS, but most likely, it is caused by incompatible CSS theme version. Yes, but you need to open a separate private ticket. Do that if you still need assistance after these latest tips. In the ticket, specify the Telerik product versions that you are using.

### Response

**Doug** commented on 13 Apr 2023

Thank you Dimo for the explanation. I have a better understanding of CSS structure and organization now...as well as Blazor. I masked out two of the three css references and that solved the issue. I did them one at a time and found that it was the ..default-ocean-blue.css file that was causing the issue. Thanks again.
