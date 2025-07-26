# Blazor Grid Showing Error When Using GridToolBarTemplate

## Question

**Wil** asked on 23 Feb 2023

I was trying out a Telerik Blazor project and I am getting an error "Severity Code Description Project File Line Suppression State Error (active) RZ9996 Unrecognized child content inside component 'TelerikGrid'. The component 'TelerikGrid' accepts child content through the following top-level items: 'GridAggregates', 'GridColumns', 'GridToolBar', 'GridExport', 'DetailTemplate', 'GridSettings', 'RowTemplate', 'NoDataTemplate'. I didn't change anything and it gives me this error. I am using Telerik UI for Blazor 3.6.1. Thanks.

## Answer

**Justin** answered on 27 Feb 2023

Hello William, Indeed, the error likely stems from breaking changes introduced in Telerik UI for Blazor v4.0.0. In v4.0.0 the GridToolBar tag was renamed to GridToolBarTemplate. Our demos will always use the latest release for code. So, since you are using v3.6.1, you will need to remove "Template" from all instances of the "GridToolBarTemplate" tag. I hope this helps. Regards, Justin
