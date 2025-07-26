# Should we remove the default .css files that come with the Server Side Blazor template?

## Question

**Dav** asked on 29 Nov 2021

When adding the Telerik theme to my existing dotnet 6 Blazor Server app, should I remove the .css files that come with that template? Here is what my HEAD looks like right now. <head> <meta charset="utf-8" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <base href="~/" /> <!--CSS--> <link rel="stylesheet" href="css/bootstrap/bootstrap.min.css" /> <link href="css/site.css" rel="stylesheet" /> <link href="Portal.styles.css" rel="stylesheet" /> <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /> <!--JS--> <script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer> </script> <component type="typeof(HeadOutlet)" render-mode="ServerPrerendered" /> </head> Should I remove the top 3 .css lines under the CSS section and leave only the Telerik theme?

## Answer

**Apostolos** answered on 01 Dec 2021

Hello David, Thank you for the code snippet along with your question. Telerik themes style Telerik components only. Any other stylesheets take care of the application layout and other content, so you need them. On a side note, we provide a Bootstrap theme. However, this theme is still related to our components only. You can find more information on Bootstrap Notes section of Built-in Themes documentation. Regards, Apostolos Giatsidis Progress Telerik
