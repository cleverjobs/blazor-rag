# DatePicker - Clicking Month garbled

## Question

**Lar** asked on 07 Dec 2022

Please see attachment. Why when I click on the month in the upper left of a Telerik datepicker is it garbled? Is there a way I can clean this up or is this a product defect?

### Response

**Dimo** commented on 12 Dec 2022

It looks like the app is using an outdated theme. Check points 3 and 4 in the Upgrade process. Another possible reason can be conflicting styles in the app. Use the browser's DOM inspector or remove all other stylesheets, except ours to verify this.

### Response

**Larry** commented on 12 Dec 2022

That fixed it, I upgraded to 3.7 and fixed the links in the _Host.cshtml file to these: <link rel="stylesheet" href="[https://blazor.cdn.telerik.com/blazor/3.7.0/kendo-theme-default/all.css"](https://blazor.cdn.telerik.com/blazor/3.7.0/kendo-theme-default/all.css") /> <script src="[https://blazor.cdn.telerik.com/blazor/3.7.0/telerik-blazor.min.js"](https://blazor.cdn.telerik.com/blazor/3.7.0/telerik-blazor.min.js") defer></script>
