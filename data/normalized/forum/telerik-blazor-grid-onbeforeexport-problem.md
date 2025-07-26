# Telerik Blazor Grid OnBeforeExport problem.

## Question

**Tho** asked on 03 May 2022

Hi, I am using grid programmatic export SaveAsExcelFileAsync(); but the event OnBeforeExport never fires. Is there any problem when calling from programmatic export? When using the default button export it fires normally. I am using the latest version 3.2.0. Thank you, Thod

## Answer

**Joana** answered on 06 May 2022

Hi Thod, By default, the events fire only for operations that our customers do not have the control over. Thus, in the sceanario of programatic export the customer initiates the export operation. However, what we are currently missing in our API methods is the possibility to define the export options. We have a logged feature request on the matter to assure that everything is available through the methods: [https://feedback.telerik.com/blazor/1563558](https://feedback.telerik.com/blazor/1563558) Regards, Joana Progress Telerik

### Response

**Thod** answered on 10 May 2022

Thank you for your answer Joana. I was confused because at your export events guide you say that " The OnBeforeExport event fires after the user clicked the ExcelExport or CsvExport buttons, or by programmatically invoking the export. " [https://docs.telerik.com/blazor-ui/components/grid/export/events](https://docs.telerik.com/blazor-ui/components/grid/export/events) Customizing the export will be very useful so i am waiting for this future. Thank you Thod
