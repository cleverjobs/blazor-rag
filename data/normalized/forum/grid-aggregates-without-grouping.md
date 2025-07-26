# Grid Aggregates without grouping

## Question

**IanIan** asked on 28 May 2020

Is there a way of displaying grid aggregates, without grouping the grid. I am trying to implement a simple grid with a footer 'row' that would show column totals Grouping the data is not really appropriate, I suppose I could add an arbitrary grouping, but the extra UI elements introduced with grouping would detract from a clean UI design. If not, what would be a good way to implement this.

## Answer

**Marin Bratanov** answered on 28 May 2020

Hi Ian, You can Follow the implementation of such a Footer template here: [https://feedback.telerik.com/blazor/1451928-need-footer-template-like-header-template-for-grid-columns-to-show-aggerates-for-all-the-rows-in-a-grid.](https://feedback.telerik.com/blazor/1451928-need-footer-template-like-header-template-for-grid-columns-to-show-aggerates-for-all-the-rows-in-a-grid.) I've added your Vote on your behalf to raise its priority. At the moment, the only idea I can offer is putting your own calculations in the header template. Regards, Marin Bratanov

### Response

**Ian** answered on 28 May 2020

Yes, a footer template is exactly what I am after. Thanks for the quick reply
