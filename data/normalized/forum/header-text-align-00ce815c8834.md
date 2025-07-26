# Header text align

## Question

**And** asked on 05 Sep 2019

Hello I need to display prices and quantities in columns and it's no problem for data. Templates is very usefull thing. But for Price header I need to place label in center. How can I use it? Thank you.

## Answer

**Marin Bratanov** answered on 05 Sep 2019

Hello Andriy, At the moment, header templates are not implemented yet in the grid. You can Follow their status in the following page (I added your vote): [https://feedback.telerik.com/blazor/1407601-grid-column-header-title-as-template.](https://feedback.telerik.com/blazor/1407601-grid-column-header-title-as-template.) While you could override the CSS rules for the grid headers and text-align: center the text, that would affect all the columns because there is no way to differentiate them at the moment. Nevertheless, here's a sample such rule I made for you in case it suits your needs: .k-grid.k-header.k-link, /* for sortable grid */.k-grid.k-header { text-align: center;
} Regards, Marin Bratanov
