# Trying to export to Excel from Data Grid - missing DemoFileExporter

## Question

**Ste** asked on 13 Feb 2020

At this point, I'm a trial user. I have been able to use a Data Grid in my Visual Studio Blazor project just fine. Now I'm trying to add an export-to-Excel feature, similar to what is described here: [https://demos.telerik.com/blazor-ui/spreadprocessing/overview](https://demos.telerik.com/blazor-ui/spreadprocessing/overview) I'm down to one build error. The name DemoFileExporter cannot be found. DemoFileExporter.Save(JsRuntime, fileData, "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "Locations.xlsx"); My guess is it is part of TelerikBlazorDemos.DocumentProcessing. Is that right? If so, I don't know where/how to get it. Is there a Nuget package for it? If not, how can I get it and add it to my Visual Studio project?

## Answer

**Steve** answered on 13 Feb 2020

I found it. During installation, it put a demo project onto my hard drive here: C:\Program Files (x86)\Progress\Telerik UI for Blazor 2.7.1\demos I opened that solution, found the few source files that were pertinent and copied them to my data grid project/solution.

### Response

**Marin Bratanov** answered on 14 Feb 2020

Hi Steve, For built-in excel export of the grid, Follow this page (my post from 13 Jan 2020 offers an example you can use as base to actually export the current data only too): [https://feedback.telerik.com/blazor/1431614-export-grid-to-excel](https://feedback.telerik.com/blazor/1431614-export-grid-to-excel) Indeed, this particular class is part of our demos, as the exporting feature is not something we have out-of-the-box yet, this class in our demos is used for the generated documents through the DocumentProcessing Libaries we offer - the demo you are looking at generates a file behind the scenes from the same data that is shown in the grid. Regards, Marin Bratanov
