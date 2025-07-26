# Since v3 has anyone had the TelerikGrid or TelerikTreeList Pager control display width only show the first digit?

## Question

**Kel** asked on 01 Jun 2022

I'm having trouble finding the cause of why the display has changed and the paging control is cutting off the value. I can't see the difference from the Telerik doc examples. or ... The width of the browser window or resolution doesn't have any effect. We are using the "_content/Telerik.UI.for.Blazor/css/kendo-theme-bootstrap/all.css".

## Answer

**Dimo** answered on 06 Jun 2022

Kelly - based on our research, it looks like browsers do not apply one of our styles correctly. You can follow this GitHub issue, in case you are interested. In the meantime, use a CSS workaround: div.k-pager.k-pager-sizes.k-dropdownlist { width: min-content; /* OR */ width: 6em;
}
