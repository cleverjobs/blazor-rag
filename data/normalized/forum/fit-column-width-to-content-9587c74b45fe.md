# Fit Column Width to Content

## Question

**Ger** asked on 21 Apr 2021

V2.23 includes the ability to fit column width to content. I can't see how to enable it. Does anyone know? Regards, Gerhard

## Answer

**Marin Bratanov** answered on 21 Apr 2021

Hello Gerhard, This is done by double clicking the borders between the column headers of a resizable grid. So, you also need to set the Resizable parameter of the grid to true. You can read more about the feature in the documentation: [https://docs.telerik.com/blazor-ui/components/grid/columns/resize.](https://docs.telerik.com/blazor-ui/components/grid/columns/resize.) Regards, Marin Bratanov

### Response

**Gerhard** answered on 21 Apr 2021

Thank you Marin. I misunderstood what this feature does. I was hoping that it could be automatic, i.e once the data has been loaded, the columns would auto-size to fit the data width and perhaps with min/max boundaries defined.

### Response

**Marin Bratanov** answered on 22 Apr 2021

Hi Gerhard, There are many reasons why that isn't implemented and one of the major ones is that rendering and data retrieval are decoupled, so firing up such functionality on load will cause flicker and will be a serious performance hit. Nevertheless, you can Follow such a feature here: [https://feedback.telerik.com/blazor/1513385-autofit-column-widths-on-data-load.](https://feedback.telerik.com/blazor/1513385-autofit-column-widths-on-data-load.) I've also added your Vote for it. Regards, Marin Bratanov Progress Telerik
