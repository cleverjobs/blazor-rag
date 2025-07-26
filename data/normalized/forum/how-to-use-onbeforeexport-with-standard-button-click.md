# How to use OnBeforeExport with standard button click

## Question

**CJCJ** asked on 29 Jan 2025

Hello! I want to export Blazor grid content to CSV and make some changes before export. This example works fine with GridCommandButton Blazor Grid Export Export Events - Telerik UI for Blazor I want to use a standard button instead of GridCommandButton. <Button.. OnClick="ExportGridData"> Export </Button> internal void ExportGridData()
{
gridRef?.ExportToCsv();
} My issue is, executing ExportToCsv does not trigger OnBeforeExport. Is there a way to trigger OnBeforeExport when calling ExportToCsv() from a button click event? Thank you.

## Answer

**Dimo** answered on 31 Jan 2025

Hi Charith, Indeed, this scenario makes sense to be enhanced from us and we have a feature request about it: Set export options like in OnBeforeExport when using export methods I see that you have already voted for it. You can also use the suggested workaround in the top post. On a side note, please ask the license holder at your company to assign you a Telerik UI for Blazor license. This will make your account compliant with our license agreement and you will also be able to receive support responses from us. Regards, Dimo Progress Telerik
