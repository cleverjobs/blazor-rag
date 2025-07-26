# GridCheckboxColumn does not have HeaderTemplate / Template

## Question

**Cla** asked on 30 Sep 2021

I can't find a way to customize the GridCheckboxColumn element. GridColumn have a Template element but seem not applicable to GridCheckboxColumn. My goal is to add a clickable icon next to selection check in the header. How to solve? Thanks

## Answer

**Marin Bratanov** answered on 30 Sep 2021

Hello Claudio, You can Follow the implementation of a header template for the selection column here: [https://feedback.telerik.com/blazor/1497026-add-headertemplate-for-the-gridcheckboxcolumn.](https://feedback.telerik.com/blazor/1497026-add-headertemplate-for-the-gridcheckboxcolumn.) In the meantime you could implement this through a "regular" grid column where you will have a header template, and for the selection checkbox you can use the approach of custom selection checkbox youcan find in this thread (you don't need the row template): [https://feedback.telerik.com/blazor/1463819-grid-row-template-with-selection-unsure-how-to-bind-to-selected-item](https://feedback.telerik.com/blazor/1463819-grid-row-template-with-selection-unsure-how-to-bind-to-selected-item) Regards, Marin Bratanov
