# Multi Select Drop Down stopped working after last update

## Question

**Dea** asked on 26 Apr 2021

After the last update the multi select drop down stopped working. It no longer drops down. You can type the names of items in the list and hit enter and they will populate the text area but the drop down never displays. Any ideas on what might be happening? As a side note I tried to change to an Autocomplete control and it would not drop down either. That might provide some insight as to the problem. I think it has something to do with the markup that caused it to behave a bit differently but not sure. I do know for sure it worked before and now it doesn't.

## Answer

**Dean** answered on 26 Apr 2021

BTW... I realize in a clean project it works so it must be sensitive to something in my HTML markup that it wasn't sensitive to before. Any ideas would be helpful. Thanks,

### Response

**Marin Bratanov** answered on 26 Apr 2021

Hello Dean, There is a bug in 2.23.0 for popups (like dropdowns - comboboxes, autocomlete, multiselect) where they don't show up in a window. It is caused by a new feature in the window and it will be fixed in our next 2.24.0 release planned for mid-May. Until then, you can try adding this CSS to work around the issue: <style>.k-animation-container { z-index: 15000;
}
</style> If that's not the problematic case, could you send me some more details on the issue? Regards, Marin Bratanov

### Response

**Dean** answered on 26 Apr 2021

Thanks for the fix. Seems like something like that should get an immediate hot fix. New customers will have no idea why it isn't working. Regardless, thanks for the help. I'll try it right now.

### Response

**Dean** answered on 26 Apr 2021

Thank you for the update! The new css fixed the problem. Your fast turnaround on this issue is much appreciated as my phone is getting blown up! I didn't catch the bug and pushed a new update into production on Friday. My phone is getting BLOWN up this morning so your fast turnaround was simply AWESOME!!!!

### Response

**Marin Bratanov** answered on 26 Apr 2021

Glad I could be of help, Dean. --Marin
