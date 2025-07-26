# Svg icons in html markup

## Question

**Giu** asked on 07 May 2024

Hello, Until recently, I was using font icons in html markup (k-icon, k-i- imagename ), but with a recent update to Telerik for Blazor 5.1.1, these do not work anymore. For components which have a Icon property, I simply replace the FontIcon references with SvgIcon. However, for icons referenced in markup, I'm not able to get the icons to display, as suggested in Changes in Icon Rendering. Please advise. Thank you.

## Answer

**Svetoslav Dimitrov** answered on 10 May 2024

Hello Giuseppe, I have two suggestions that might resolve the issue: 1. In your global Imports file, add the FontIcons namespace: @using Telerik.FontIcons 2. Load this stylesheet: <link href="[https://blazor.cdn.telerik.com/blazor/5.1.1/kendo-font-icons/font-icons.css"](https://blazor.cdn.telerik.com/blazor/5.1.1/kendo-font-icons/font-icons.css") rel="stylesheet" type="text/css" /> below the definition of the theme in your application. Here is a REPL snippet where the HTML definition of the font icons works as expected. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Giuseppe** commented on 10 May 2024

Hello Svetoslav, That's what I ended up doing. I guess I misunderstood the documentation. Thank you.
