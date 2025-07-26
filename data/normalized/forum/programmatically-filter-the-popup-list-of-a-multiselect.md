# Programmatically filter the popup list of a MultiSelect

## Question

**TedTed** asked on 30 Jun 2023

I'd like to be able to programmatically filter only the values shown in the popup list of the MultiSelect. Is there a way to do this that does not use the built in filtering, which is clunky? I tried the suggestion here ( Blazor MultiSelect Demos - Custom Filtering | Telerik UI for Blazor ), but the issue with that is the OnRead mechanism filters not only the values shown in the popup list, but also all the values available to the MultiSelect itself. This means that if items are already selected in the MultiSelect, then the popup list is shown, then I filter the popup list using OnRead (and the filter does not include the values already selected in the MultiSelect), the MultiSelect loses those existing selections and they disappear. So the OnRead mechanism does not work for only filtering the popup list. When using the default filtering, that filtering only filters the popup list and keeps any existing selection in the MultiSelect, which is the correct behavior I'm looking for, but programmatically done. So, bottom line, I'd like a mechanism to programmatically filter only the items displayed in the popup list that works separately from the default filtering of the MultiSelect.

## Answer

**Yanislav** answered on 05 Jul 2023

Hello Ted, Correct me if I misunderstood any part of the requirement. Based on the description, it seems that the aim is to display selected items in the popup, even if they don't match the filter term. Is that correct? If that's the case, you can modify the filtered data during the OnRead event. To meet your concrete requirement, you can add the selected items to the filtered collection after calling the ToDataSourceResult method. This way, the selected items will be always included in the list. Here's an example that demonstrates this approach: [https://blazorrepl.telerik.com/mREBazbP32MxCUyq24](https://blazorrepl.telerik.com/mREBazbP32MxCUyq24) I hope this helps. Regards, Yanislav
