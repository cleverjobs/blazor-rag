# Is it possible to change the alignment of items per cell rather than for the entire grid?

## Question

**Dav** asked on 01 Dec 2021

For example, I want the items in the upper left cell to be horizontal centered. But I want the items in the upper right cell to be horizontal aligned left. Is something like this possible without using custom css?

## Answer

**Marin Bratanov** answered on 01 Dec 2021

Hi David, One option is to use the TextAlign of the grid columns: [https://docs.telerik.com/blazor-ui/components/grid/columns/bound#appearance](https://docs.telerik.com/blazor-ui/components/grid/columns/bound#appearance) Alternatively, you can use the OnCellRener event and add a Class to the desired columns through it, and change the alignment with CSS. Depending on which elements you want to alter, you may still have to use some CSS, you can read more here. Regards, Marin Bratanov Progress Telerik
