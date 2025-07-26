# Export to excel of two Telerik grids (Summary/detail) in a single file.

## Question

**Him** asked on 29 May 2023

I have two Telerik Grid (Summary & Detail Grid). Detail Grid also have child rows. I need to export to excel for both the grid together in a single file with keeping all the formatting (filtering, freezing, sorting etc). Please provide the solution for this implementation with proper example.

## Answer

**Nadezhda Tacheva** answered on 31 May 2023

Hi Himani, I will address your concerns separately as follows: Export formatted Grid By design, the built-in export functionality takes into consideration the filtering and sorting applied to the Grid to export the data in a format the user altered it. Including the frozen state of the columns, however, is not currently part of the built-in export. I will evaluate that with the team and will get back to you to provide more details. Export hierarchical Grid In general, templates are not exported, because there is no provision in the framework for getting them at runtime. So, since the child Grid is rendered in a Detail template, it cannot be included in the exported file out of the box. It is possible to achieve the desired result with a custom approach. You may check the following sample app for reference: [https://github.com/telerik/blazor-ui/tree/master/grid/export-to-xlsx-hierarchy.](https://github.com/telerik/blazor-ui/tree/master/grid/export-to-xlsx-hierarchy.) It is important to mention that this is a custom export functionality, so exporting formatted data should be handled by the application. You can manage the format of the data that will be passed for exporting. Prior to the export, you may check the Grid State to see if the user performed any filtering or sorting to modify the data in the needed way. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Nadezhda Tacheva** answered on 02 Jun 2023

Hi Himani, I am stepping in to provide an update on including the frozen state of the columns in the built-in export. This scenario is a bit specific as there are differences in the behavior of frozen columns in Grid and in Excel. Let me give a simple example. In Excel, if a column is frozen, all columns on its left side cannot be moved. In the Grid, however, there could be a frozen column in the middle and it is still possible to scroll the columns on the left and right side of the frozen one. These differences prevent us from achieving complete feature parity in terms of frozen columns in the Grid and in Excel. So, including them in the built-in export may lead to undesired behavior in the generated Excel file. A possible option is to customize the exported file to freeze only the desired columns using the Document Processing libraries: SpreadStreamProcessing SpreadProcessing As for a built-in feature, you may open a feature request in our portal where you can describe the exact desired behavior for exporting the frozen columns considering the above-listed differences. If it gains community interest, we will consider possible options for implementation. Regards, Nadezhda Tacheva
