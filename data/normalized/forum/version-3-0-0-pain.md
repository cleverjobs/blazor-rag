# Version 3.0.0 pain

## Question

**Mat** asked on 24 Jan 2022

We just upgraded our project to 3.0.0 in order to implement the OnResize of TileLayout and it caused so many errors due to the minor changes, and one that doesn't even throw an error until deployed...PopupHeight. WHY? How is this an improvement? So, now, my comboboxes, drop-downs, and autocompletes go from: <TelerikComboBox Data="@data" PopupHeight="auto" /> to: <TelerikComboBox Data="@data"> <ComboBoxSettings> <ComboBoxPopupSettings Height="auto" /> </ComboBoxSettings> </TelerikComboBox> (as if our combobox properties are that limited...sorry to rant)

### Response

**Alex** commented on 25 Jan 2022

I feel your pain. The full list of breaking changes is here [https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/3-0-0](https://docs.telerik.com/blazor-ui/upgrade/breaking-changes/3-0-0)
