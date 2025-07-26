# TelerikColorPalette: Missing Data in TelerikMessages.de-DE.resx

## Question

**Hen** asked on 16 Jul 2024

I am using localisation like this: builder.Services.AddSingleton(typeof(ITelerikStringLocalizer), typeof(SampleResxLocalizer)); That worked just fine until I added the TelerikColorPalette-Control for the first time. Blazor throwed errors and it took me a while to get to the problem. It seems that there are missing entries in the TelerikMessages.de-DE.resx but I cannot figure out which. Same problem with TelerikColorPicker... I allready downloaded the latest version of TelerikMessages.resx and TelerikMessages.de-DE.resx from the demo-project and I also tried the communtiy-version. How can I fix this problem ?

### Response

**Hendrik** commented on 16 Jul 2024

I figured out myself: the missing Entries are ColorPicker_AriaLabel and PopupList_AriaLabel. Now it works...
