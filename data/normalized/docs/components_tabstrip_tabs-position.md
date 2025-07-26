
# TabStrip Tabs Position

By default, the tab titles display on top of the tab content.

You can customize their position through the optional `TabPosition` attribute of the `TelerikTabStrip` tag. It takes a member of the `Telerik.Blazor.TabPosition` enumeration:

* `Top` (default)
* `Left`
* `Right`
* `Bottom`

>caption Set the desired tab position.

````RAZOR
<TelerikTabStrip TabPosition="@TabPosition.Bottom">
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