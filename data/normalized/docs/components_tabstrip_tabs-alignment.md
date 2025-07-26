
# TabStrip Tabs Alignment

By design, the tabs are displayed on the left side of the TabStrip header.

You can customize their alignment through the `TabAlignment` parameter. It takes a member of the `Telerik.Blazor.TabStripTabAlignment` enumeration:

* `Start` (default)
* `End`
* `Center`
* `Justify`
* `Stretched`

>caption Set the desired tab alignment.

````RAZOR
<TelerikTabStrip TabAlignment="@TabStripTabAlignment.End">
    <TabStripTab Title="First">
        First tab content.
    </TabStripTab>
    <TabStripTab Title="Second">
        Second tab content.        
    </TabStripTab>
    <TabStripTab Title="Third">
        Third tab content.
    </TabStripTab>
</TelerikTabStrip>
````

## See Also

* [Live Demo: TabStrip - Tabs Position and Alignment](https://demos.telerik.com/blazor-ui/tabstrip/tab-positions)