# Grid paging issue

## Question

**con** asked on 16 Jun 2020

Hi, Here is my Grid: <div class="row"> <div class="col-lg" style="background-color:orange"> <TelerikGrid Data="@orders" Sortable="true" Pageable="true" PageSize="10"> <GridColumns> <GridCheckboxColumn /> <GridColumn Field="@(nameof(OrdersModel.OrdDate))" /> <GridColumn Field="@(nameof(OrdersModel.OrdNo))" /> </GridColumns> </TelerikGrid> </div> </div> See how Paging looks like in attached file. Thoughts?

## Answer

**Svetoslav Dimitrov** answered on 16 Jun 2020

Hello Konstantin, From the screenshot you have sent to us I can see that you might be missing our theme, which provides the necessary CSS rules. To validate that, you can go the _Host.cshtml file, under the Pages folder and check for a line like: <link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-bootstrap/all.css" /> If that line is missing or commented our you should add it. You can read more about how you can fetch our themes here: [https://docs.telerik.com/blazor-ui/themes/overview.](https://docs.telerik.com/blazor-ui/themes/overview.) You need to ensure they are available on the page. For example, if you are using the CDN, it is possible that a firewall setting at your workplace blocks it. Regards, Svetoslav Dimitrov

### Response

**const** answered on 16 Jun 2020

Hi Svetoslav, That solved the issue, thank you, now Grid is rendering properly. But another issue came: Error: Could not find 'TelerikBlazor' in 'window'. at [https://localhost:44362/_framework/blazor.server.js:8:30748](https://localhost:44362/_framework/blazor.server.js:8:30748) at Array.forEach (<anonymous>) at p ([https://localhost:44362/_framework/blazor.server.js:8:30709)](https://localhost:44362/_framework/blazor.server.js:8:30709)) at [https://localhost:44362/_framework/blazor.server.js:8:31416](https://localhost:44362/_framework/blazor.server.js:8:31416) at new Promise (<anonymous>) at e.beginInvokeJSFromDotNet ([https://localhost:44362/_framework/blazor.server.js:8:31390)](https://localhost:44362/_framework/blazor.server.js:8:31390)) at [https://localhost:44362/_framework/blazor.server.js:1:19202](https://localhost:44362/_framework/blazor.server.js:1:19202) at Array.forEach (<anonymous>) at e.invokeClientMethod ([https://localhost:44362/_framework/blazor.server.js:1:19173)](https://localhost:44362/_framework/blazor.server.js:1:19173)) at e.processIncomingData ([https://localhost:44362/_framework/blazor.server.js:1:17165)](https://localhost:44362/_framework/blazor.server.js:1:17165)) Please advise

### Response

**Svetoslav Dimitrov** answered on 16 Jun 2020

Hello Konstantin, This issue is related to a JS Interop error. The first thing I would suggest is for you to check in your _Host.cshtml for a line like: <script src="[https://kendo.cdn.telerik.com/blazor/<VERSION](https://kendo.cdn.telerik.com/blazor/<VERSION) NUMBER>/telerik-blazor.min.js" defer> </script> where the version number should be 2.14.1. In this (link: [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors) ) article you can find more troubleshooting steps regarding those errors. If neither of those help you solve the issue I would suggest you do the upgrade process again by following the steps from this link: [https://docs.telerik.com/blazor-ui/upgrade/overview.](https://docs.telerik.com/blazor-ui/upgrade/overview.) Regards, Svetoslav Dimitrov

### Response

**const** answered on 16 Jun 2020

Thank you, Svetoslav, all works now!
