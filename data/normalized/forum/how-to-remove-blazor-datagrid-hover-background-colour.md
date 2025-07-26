# How to remove Blazor DataGrid Hover background colour

## Question

**CJCJ** asked on 23 Mar 2025

I have a Blazor DataGrid with three Locked columns. Those locked columns are coming with alternative background colour on hover. How can I remove that? I removed background colours as follows /*Remove alternative row background color for sticky columns on Rows*/.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-content-sticky,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky>.k-table-td,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky { background-color: white!important;
} Tried following to remove the hover background colour, but not luck. .tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-content-sticky,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky>.k-table-td,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-content-sticky:hover,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky>.k-table-td:hover,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky:hover { background-color: white!important;
}

## Answer

**Anislav** answered on 27 Mar 2025

What about the following CSS: <style>.k-master-row:hover.k-grid-content-sticky,.k-master-row:hover.k-grid-row-sticky,.k-master-row:hover.k-grid-row-sticky>.k-table-td,.k-master-row.k-hover.k-grid-content-sticky,.k-master-row.k-hover.k-grid-row-sticky,.k-master-row.k-hover.k-grid-row-sticky>.k-table-td { background-color: white!important;
}
</style> Reagrds, Anislav Atanasov

### Response

**Anislav** commented on 08 Apr 2025

Does it work for you?

### Response

**CJ** commented on 10 Apr 2025

Hi Anislav, I have 3 sticky columns and a few more non sticky columns in this grid. Your solution cleared the background color of the sticky columns. Now there is a background color difference in the non-sticky columns. How can I apply the same style for non sticky columns? Thanks
