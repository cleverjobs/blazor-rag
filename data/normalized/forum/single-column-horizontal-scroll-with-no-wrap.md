# Single Column Horizontal Scroll with No Wrap

## Question

**CeeCee** asked on 27 Aug 2020

Is there an option to have a horizontal scroll while not wrapping the text for a single column?

## Answer

**Cee** answered on 27 Aug 2020

Here is snippet of the current behavior. I would like the text to not wrap as displayed, but also provide a horizontal scrollbar for seeing the remaining text.

### Response

**Marin Bratanov** answered on 28 Aug 2020

Hi Cee, If you set a larger Width to the column, it will have more horizontal space. If you set a large enough width, so the total of the columns width is larger than the width of the treelist, the entire treelist will have a horizontal scorllbar (read more here ). You can also enable column resizing so the end user can adjust the column widths in case they go that deep (maybe not all of them will) or in case a particular row has unexpectedly long text (you can't have control over the actual data). If you want scrollbars per-cell, you can use the cell template and you can add a div with the desired scrolling settings (like a different overflow or white-space CSS rules). You could, technically, set them for the <td> elements of the treelist without a template, but then they would affect all cells and not just the one you want to target, so that might not be desired. For example, something like the rules below, where the special-cell-overflow class is added to the treelist to distinguish it from other tables, grids and treelist instances: .special-cell-overflow.k-grid-content td { overflow: auto; text-overflow: initial
} Regards, Marin Bratanov

### Response

**Cee** answered on 27 Jan 2021

Thank you Marin
