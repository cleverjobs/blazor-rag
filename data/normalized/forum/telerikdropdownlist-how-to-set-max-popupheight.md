# TelerikDropDownList: how to set max PopupHeight?

## Question

**DeeDee** asked on 14 Jan 2021

hi...would appreciate guidance on how to set max PopupHeight such that it will be auto until it hits a threshold px level of e.g. 200px after which the dropdown 'fixes' at that max height and becomes scrollable? many thanks

### Response

**Ted** commented on 08 Feb 2023

This doesn't really help. Specifying "auto" should fit the popup BOTH minimum height and maximum height so that the popup does not extend below the bottom of its parent container. Currently if there are many items in the popup, setting "auto" for the height extends the popup below the bottom of its container so that items are not visible and also there is no scroll bar, so the popup is totally unusable!! If there are a few items in the popup and "auto" is specified, a bunch of empty rows are placed at the bottom of the popup for some reason?! This is UX 101, so please put a fix in for this!

### Response

**Dimo** commented on 13 Feb 2023

@Ted - auto height means that an element will expand, according to its content. I assume that you are suggesting an automatic screen boundary detection, which makes sense, but not always. If the user opens the dropdown near the bottom of the screen, they will face a great deal of scrolling and no hint that they can reposition the dropdown for a larger dropdown and better UX. So, I recommend a combination of Height="auto" and some MaxHeight value. For example, you can restrict the dropdown height, based on the viewport height. <ComboBoxPopupSettings Height="auto" MaxHeight="60vh" />

### Response

**Ted** commented on 13 Feb 2023

Hi Dimo, Yes, specifying Height="auto" & MaxHeight does work in some cases when the max height value is small and the browser window height is large, but it does not work in many other cases if MaxHeight is set to any normal medium number of rows, see screenshot below. Also, this isn't a screen boundary check, it is a check to stay within the boundary of the parent window/dialog or container of the combo box. Can you please submit this as a bug fix for an upcoming version of Telerik Blazor and/or provide another fix in the meantime to get the combo box to autosize its height correctly to its container? The combo box is simply not usable in its current state.

### Response

**Dimo** commented on 13 Feb 2023

@Ted - Our dropdowns always render in the app root, so they don't take into account the component's container. This requires custom app logic. However, the screenshot does not make it clear what is the "parent window" - it looks like the ComboBox is constrained by the browser window and in this case, the dropdown should open UP, just like in our online ComboBox demos (shrink the browser window vertically to see that). Please send a runnable REPL test page, so that I can see what is your exact scenario.

### Response

**Ted** commented on 13 Feb 2023

Dimo, When I click that REPL page link I get this: I also don't have time and bandwidth to create a whole custom page example for you. This is simply a TelerikComboBox inside of a TelerikForm directly inside a browser window, it should be easily reproducible at your end. The combo box has <ComboBoxPopupSettings MaxHeight="22em" Height="auto" /> Here are some screenshots of the page with the browser window larger (so you can see the entire combo box height), then resized to a smaller size. Obviously this would be an issue on a mobile device too. This needs to be fixed on the Telerik side, the combo box is not useable currently!

### Response

**Dimo** commented on 13 Feb 2023

OK, I think these screenshots show what is happening - the MaxHeight value is too large, so the dropdown cannot display UP, so it always displays DOWN. Try with a smaller value, which corresponds to the available space ABOVE the ComboBox. With regard to mobile devices, use the adaptive mode of the component. I will check with the team if we can implement automatic screen (viewport) boundary detection for desktop usage. I also reported the DNS REPL error, although this may be something intermittent or specific to your network, as the tool opens on my side.

### Response

**Ted** commented on 13 Feb 2023

Dimo, Please, your suggestion doesn't make any sense. I can't set the MaxHeight to a smaller value in the general case. Sure, I can hardcode it to a value to get it to work for this very specific senario, combobox position, and window size, but that's not a fix! This needs to be a dynamic fix for all window sizes and combobox positions for the general case, which can only be done in the code and/or css of the combobox itself at the Telerik end. Please let's get this in as a bug fix in an upcoming release of Telerik Blazor, otherwise the combobox is not ready for Production use.

### Response

**Dimo** commented on 16 Feb 2023

@Ted - see and follow this screen boundary detection feature request. I already voted on your behalf. Currently, the easiest and universal option is to use Height="auto" and MaxHeight="45vh" (or a similar value below 50vh). This will guarantee that the dropdown will always fully visible on the screen (showing either up or down) and will shrink automatically if the item count is small.

## Answer

**Nadezhda Tacheva** answered on 15 Jan 2021

Hi Dee, In the upcoming release (2.21.0) we will have implemented component-specific CSS classes. Having a PopupClass parameter of the DropdownList component, you can easily set the maximum height of its dropdown with CSS. In the meantime, in the public

### Response

**Ted** commented on 08 Feb 2023

This doesn't really help. Specifying "auto" should fit the popup BOTH minimum height and maximum height so that the popup does not extend below the bottom of its parent container. Currently if there are many items in the popup, setting "auto" for the height extends the popup below the bottom of its container so that items are not visible and also there is no scroll bar, so the popup is totally unusable!! If there are a few items in the popup and "auto" is specified, a bunch of empty rows are placed at the bottom of the popup for some reason?! This is UX 101, so please put a fix in for this!
