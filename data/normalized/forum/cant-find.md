# Cant find

## Question

**Bit** asked on 14 May 2020

In this example [https://docs.telerik.com/blazor-ui/getting-started/server-blazor](https://docs.telerik.com/blazor-ui/getting-started/server-blazor) This part, <head> . . .
<script src="_content/Telerik.UI.for.Blazor/js/telerik-blazor.js" defer></script><!-- For Trial licenses use
<script src="_content/Telerik.UI.for.Blazor.Trial/js/telerik-blazor.js" defer></script>
--></head> When I run my app, I get a 404 on telerik-blazor.js Where is the _content folder? Also, this section <head> . . .
<link rel="stylesheet" href="_content/Telerik.UI.for.Blazor/css/kendo-theme-default/all.css" /><!-- For Trial licenses use
<link rel="stylesheet" href="_content/Telerik.UI.for.Blazor.Trial/css/kendo-theme-default/all.css" />
--></head> Get a 404 on all.css

## Answer

**BitShift** answered on 14 May 2020

Ahh, maybe my nuget feed isn't pulling content in correctly? I was able to setup the feed and add a reference however.

### Response

**BitShift** answered on 14 May 2020

I can use the CDN, but there is an error in these examples. This @progress needs to be escaped in Razor with @, so becomes @@progress How can I figure out why my Nuget feed isnt working? [https://docs.telerik.com/blazor-ui/getting-started/what-you-need](https://docs.telerik.com/blazor-ui/getting-started/what-you-need) <!DOCTYPE html> <html> <head> . . . <link rel="stylesheet" href=" [https://unpkg.com/](https://unpkg.com/) @progress/kendo-theme-default@latest/dist/all.css" /> <!-- Choose only one of the themes --> <!-- <link href=" [https://unpkg.com/](https://unpkg.com/) @progress/kendo-theme-bootstrap@latest/dist/all.css" rel="stylesheet" /> <link href=" [https://unpkg.com/](https://unpkg.com/) @progress/kendo-theme-material@latest/dist/all.css" rel="stylesheet" /> --> <script src=" [https://kendo.cdn.telerik.com/blazor/2.13.0/telerik-blazor.min.js](https://kendo.cdn.telerik.com/blazor/2.13.0/telerik-blazor.min.js) " defer></script> </head>

### Response

**Svetoslav Dimitrov** answered on 15 May 2020

Hello Randal, For the 404 error with the static assets, you can check the following articles for more information on known issues and solutions: [https://docs.telerik.com/blazor-ui/troubleshooting/deployment#reported-issues](https://docs.telerik.com/blazor-ui/troubleshooting/deployment#reported-issues) [https://docs.telerik.com/blazor-ui/troubleshooting/js-errors#missing-file](https://docs.telerik.com/blazor-ui/troubleshooting/js-errors#missing-file) If you can restore the packages, this means that the nuget feed is working, and that the issue with the assets is related to the deployment or networking issues in the current environment. If those ideas do not work for you, please open a Support ticket so we can further investigate a sample and/or a live URL. Regards, Svetoslav Dimitrov
