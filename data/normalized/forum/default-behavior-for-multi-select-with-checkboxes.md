# Default behavior for multi-select with checkboxes

## Question

**Dou** asked on 20 Aug 2020

I have a grid set up to allow multi-selection and I use a GridCheckboxColumn for row selection. What I'm finding is that you can check multiple checkboxes to select multiple rows, however if you click on a row in a different column it unchecks all selected rows and selects only the row you clicked on. I can kind of understand that behavior as it's a scenario where you can also use ctrl+click to select multiples, and in that case if you click a row without holding down ctrl then you would expect other selected rows to be deselected. I can live with that. The problem I'm having though is that let's say you're going through and using the checkboxes to select numerous rows. If you just barely miss the checkbox on your click, but your click is still inside the checkbox column, all your selected rows become deselected. Is there a way to disable the ctrl+click behavior at least in the checkbox column so missing the checkbox won't cause you to lose all your selections? Or disable that for the whole grid and allow selection with just a click, not requiring ctrl? Or maybe some other solution? Thanks.

## Answer

**Marin Bratanov** answered on 20 Aug 2020

Hello Doug, You can also Follow this feature implementation that will allow it as an out-of-the-box feature: [https://feedback.telerik.com/blazor/1454469-select-rows-only-with-checkboxes-clicking-the-rows-to-not-affect-selection.](https://feedback.telerik.com/blazor/1454469-select-rows-only-with-checkboxes-clicking-the-rows-to-not-affect-selection.) You can also find several workaround ideas in the thread that you can try to see if one of them will suit your needs. I've also added your Vote on your behalf to raise the priority of the idea. Regards, Marin Bratanov

### Response

**Doug** answered on 21 Aug 2020

Thanks Marin. I looked through the forums but should have reviewed the feature requests as well. Got it working with the row template and header template for the select all.
