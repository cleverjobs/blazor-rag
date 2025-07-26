
# TabStrip Tabs Size

By design, the tabs are displayed in medium size.

You can customize the size of the TabStrip tabs using the `Size` parameter. It is recommended to use predefined constants from the `ThemeConstants.TabStrip.Size` static class. The available options are:

* `small` — Reduces the default padding of the TabStrip tabs. This size is useful when you want to fit more tabs in a limited space.
* `medium` (default) — Represents the default padding of the TabStrip tabs.
* `large` — Increases the default padding of the TabStrip tabs. This size is useful when you want to provide larger elements for easier end-user interaction.

>caption Set the desired tab size.

````RAZOR
<TelerikTabStrip Size="@ThemeConstants.TabStrip.Size.Large">
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