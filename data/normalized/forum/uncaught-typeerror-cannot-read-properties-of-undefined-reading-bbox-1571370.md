# Uncaught TypeError: Cannot read properties of undefined (reading 'bbox')

## Question

**Ila** asked on 04 Jul 2022

I'm trying to export my chart to PDF using the telerikClientExporter.js and I'm getting this error: rror: Microsoft.JSInterop.JSException: Cannot read properties of undefined (reading 'bbox') TypeError: Cannot read properties of undefined (reading 'bbox') at i ([http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:627)](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:627)) at [http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:773](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:773) at o ([http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:555)](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:555)) at a ([http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:698)](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:698)) at r ([http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:346)](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:346)) at Object.Group ([http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:1303)](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:1303)) at s ([http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:6:28365)](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:6:28365)) at [http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:830](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:830) at o ([http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:555)](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:555)) at a ([http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:698)](http://localhost/ReportsBlazor/lib/progress/kendo-drawing/dist/cdn/js/kendo-drawing.js:7:698))

## Answer

**Svetoslav Dimitrov** answered on 07 Jul 2022

Hello Ilan, We have an open feature request for allowing the usage of the Kendo Drawing API in a Blazor application to export the Chart/Gauges to PDF. You can Vote for that feature request and click the Follow button to receive email notifications on status updates. Regards, Svetoslav Dimitrov

### Response

**Ilan** commented on 07 Jul 2022

Is there any other way to export chart to Pdf?

### Response

**Svetoslav Dimitrov** commented on 12 Jul 2022

Until the feature request is implemented you can use some custom JavaScript to implement the behavior.
