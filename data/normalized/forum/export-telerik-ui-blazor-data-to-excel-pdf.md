# Export Telerik UI Blazor data to Excel/PDF

## Question

**Med** asked on 02 Jan 2020

Is there a component available to export data from telerik blazor/grid to Excel and PDF? I have data displayed in a grid and we would like to add export to excel/PDF and printing functionality. If this is not yet available, is there any plan to include this functionality soon by any chance? Thank you

## Answer

**Kristian** answered on 02 Jan 2020

Hi Medhanie, We have a public page where you can Vote for and Follow the progress of Export to Excel feature - [https://feedback.telerik.com/blazor/1431614-export-grid-to-excel.](https://feedback.telerik.com/blazor/1431614-export-grid-to-excel.) I hope it will be ready for release around April. The export to PDF Functionality is not yet planned. You can follow the progress of the feature here - [https://feedback.telerik.com/blazor/1434269-export-grid-to-pdf.](https://feedback.telerik.com/blazor/1434269-export-grid-to-pdf.) We prioritize the next features considering the community interest and you can raise the priority by voting for it. The printing you can implement right now with a few lines of code. I created an example for you here - [https://github.com/telerik/blazor-ui/tree/master/grid/print](https://github.com/telerik/blazor-ui/tree/master/grid/print) Regards, Kristian

### Response

**Aleksandr** answered on 05 Nov 2020

Kristian, Marin, i have found an example how to export Nested grid to excel Export nested grid this approach require data for nested grid be loaded together with parent, any way to make it work with dynamic loading data for nested grid?

### Response

**Marin Bratanov** answered on 06 Nov 2020

Hello Aleksandr, That's an example made by our customer Hussam that can cater to some cases. There are a couple of important considerations why the grid cannot do what you ask: The DetailTemplate is a template, it is not controlled by the grid. There is no feature in the framework that lets the grid get its template. This is why the excel export has a note in its documentation that templates are not exported. The export operation happens synchronously, it needs all the data it will work on in order to create the loop over it to add rows. It could not possibly know what and when you need to fetch for a template it cannot use. What I can suggest you look into is stepping on Hussam's example you found and adding the async data retrieval you want in the place of the nested grid creations. If you do that, I'd encourage you to post a second example in that folder to showcase this, we award such contributions with Telerik points. Regards, Marin Bratanov

### Response

**Aleksandr** answered on 06 Nov 2020

Marin, thx a lot for the suggestion, I will think it over. P.S - I asked it because we easily do it with jQuery grid

### Response

**Marin Bratanov** answered on 06 Nov 2020

Hi Aleksandr, With jQuery, everything happens through a DOM manipulation, which is a bad practice in Blazor - the framework handles the shadow DOM and its manipulations. Thus, the two contexts are extremely different. Regards, Marin Bratanov

### Response

**Aleksandr** answered on 07 Nov 2020

so, made it possible using expand & collapse grid events, works as expected public void Collapse(GridRowCollapseEventArgs args) { Console.WriteLine("ReportSubscriptionViewModel Collapse"); var reportModel=(SubscriptionReportModel)args.Item; var dataItem=Data.FirstOrDefault(_=> _.Id==reportModel.Id); dataItem.NestedData=new List<SubscriptionReportNestedModel>(); } public async Task Expand(GridRowExpandEventArgs args) { Console.WriteLine("ReportSubscriptionViewModel Expand"); var reportModel=(SubscriptionReportModel)args.Item; var dataItem=Data.FirstOrDefault(_=> _.Id==reportModel.Id); dataItem.NestedData=await _reportsApiService.GetSubscriptionNestedAsync(dataItem.Id); DoWorkHide(); }
