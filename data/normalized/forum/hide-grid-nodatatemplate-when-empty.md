# Hide Grid NoDataTemplate when empty

## Question

**Cla** asked on 03 Jun 2022

Hi, i would like to hide the row showed when the grid has no data. I tried set an empty NoDataTemplate as you can show in this sample, but there is still an empty row in the grid. [https://blazorrepl.telerik.com/mwOKORks03LqmocU06](https://blazorrepl.telerik.com/mwOKORks03LqmocU06) My actual workaround is using css: <TelerikGrid Class="hide-no-data-template">...</TelerikGrid> .hide-no-data-template .k-grid-norecords { display: none; } or set the diplay attribute via JSInterop for specific cases. I think when NoDataTemplate is empty you should not show an empty row but simply hide the template row. Can be solved?

## Answer

**Marin Bratanov** answered on 04 Jun 2022

Hi Claudio, In the common case, the grid should show an indication to the user while it is loading data and when there is no actual data - this is important for the UX so that the user knows what is happening, whether they should wait, or whether the grid is really empty. Thus, the NoDataTemplate is just a way for you to customize the appearance - the necessary HTML elements above it will and should still render so that content you put there will be styled and positioned as intended. I am not sure what the issue is with those elements being there in the case you have, but using CSS to hide them is a valid way. Regards, Marin Bratanov Progress Telerik

### Response

**Claudio** answered on 06 Jun 2022

Hi Marin, my question is caused by the fact that in previous Kendo-UI library for JQuery / AngularJS the no data template behaviour is different. As you can see in the documentation the default behavious was not showing the template in the grid, so this is a breaking change of blazor library: [https://docs.telerik.com/kendo-ui/api/javascript/ui/grid/configuration/norecords](https://docs.telerik.com/kendo-ui/api/javascript/ui/grid/configuration/norecords) Can be scheduled an implementation to restore this feature without using css? Thanks

### Response

**Dimo** commented on 08 Jun 2022

Claudio, can you explain what is the problem with the empty row? This can help us understand your scenario better.

### Response

**Claudio** commented on 08 Jun 2022

Actually empty template has graphics side effect, if you hovering the grid with mouse it highlight the empty row: for us the best solution would be keep the same behaviour of Kendo UI for JQuery / Angular, showing the template only if declared explicitely, but this solution will cause a breaking changes against the current version of the blazor library, so the minimal change would be to handle the empty template not showing an empty row.

### Response

**Dimo** commented on 08 Jun 2022

Fair point. I have sent this to our front-end colleagues for evaluation and fixing. Edit: you can track this GitHub issue.
