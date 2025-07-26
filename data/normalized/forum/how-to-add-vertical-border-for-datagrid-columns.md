# How to add vertical border for DataGrid columns

## Question

**CJCJ** asked on 07 Mar 2025

I have a Blazor DataGrid with couple of Locked columns. I want to add vertical borders only for the other scrollable columns. I have tried the examples in here but no luck Blazor Change Border Color of Grid Columns - Telerik UI for Blazor I s there a way to add vertical boarders when there are Locked columns? Thanks

## Answer

**Anislav** answered on 07 Mar 2025

Hi Charith, Yes, it is possible to control which cell borders are displayed when you have locked grid columns. In this case, the CSS selectors will be a bit different. You can use.k-grid-content-sticky and.k-grid-header-sticky to select the cells and headers of the locked (sticky) columns, and then remove their borders as shown below: <style>.k-grid-content-sticky,.k-grid-header-sticky { border-inline-end-width: 0!important;
} </style> You can check out the example that I set up: [https://blazorrepl.telerik.com/mTudurFJ446V7xg721](https://blazorrepl.telerik.com/mTudurFJ446V7xg721) Regards, Anislav Atanasov

### Response

**CJ** commented on 09 Mar 2025

Thanks Anislav, What's the best way to apply this style only for the last sticky column? I want to display the border only for the last locked column, other locked columns do not have a border. I tried with last column HeaderClass that doesn't seem to work and GridColumn does not has Class property. Attached screenshot shows what I want to achieve. I"ve a updated PERL to demonstrate the issue. I want to apply style-forunit-Price class for the last locked column in this example Telerik REPL for Blazor - The best place to play, experiment, share & learn using Blazor.

### Response

**Anislav** commented on 10 Mar 2025

One possible solution is to use the data-col-index attribute that the Grid assigns to columns. While this approach works, keep in mind that you'll need to update your CSS selector if you add more sticky columns. Here’s a CSS selector that achieves this: .k-grid-content-sticky:not ( td [data-col-index="1" ] ),.k-grid-header-sticky:not ( th [data-col-index="1" ] ) { border-inline-end-width: 0!important;
} You can also check out this REPL example that demonstrates the approach: [https://blazorrepl.telerik.com/GJknbukW40sMb7A336.](https://blazorrepl.telerik.com/GJknbukW40sMb7A336.) Regards, Anislav Atanasov

### Response

**CJ** commented on 10 Mar 2025

Great, Thank you!

### Response

**CJ** commented on 20 Mar 2025

I remove alternative background colors like this. But it's still getting background color on hover. How can I remove the hover background color? Thank you. /*Remove alternative row background color for sticky columns on Rows*/.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-content-sticky,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky>.k-table-td,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky { background-color: white!important;
} Tried following but no luck .tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-content-sticky,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky>.k-table-td,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-content-sticky:hover,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky>.k-table-td:hover,.tgrid-remove-alt-color-sticky-columns-rows.k-master-row.k-table-alt-row.k-grid-row-sticky:hover { background-color: white!important;
}
