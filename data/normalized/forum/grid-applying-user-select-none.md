# Grid applying user-select-none

## Question

**Dou** asked on 07 Nov 2024

I have a telerik grid and the user-select-none and k-user-select_none css is getting applied to the grid preventing text selection but for the life of me I can't figure out why that's getting applied. I have grids in other applications where that doesn't get applied so why this one? What causes the grid to apply that css? The grid setup doesn't seem to be materially different between applications so any guidance would be appreciated.

### Response

**Hristian Stefanov** commented on 08 Nov 2024

Hi Doug, I can confirm that the ".k-user-select-none" CSS class is applied when cell selection is enabled in the Grid. To remove it, set the DragToSelect parameter of the GridSelectionSettings tag to false. Here’s a demo for reference: Grid - Cell Selection. As for the " user-select-none " CSS class, it doesn’t appear to originate from the Grid component itself but likely appears from somewhere else in the app. Kind Regards, Hristian

### Response

**Doug** commented on 08 Nov 2024

Hristian, Thanks for the response. Setting DragToSelect=false resolved the issue but there still must be something else in play here. Previously I didn't have a GridSelectionSettings tag defined but the grid still behaved as if DragToSelect was true. That's not supposed to be the default, correct? So it's as if something else was causing the DragToSelect functionality to be set without me setting it explicitly, and I also looked at the grid in a different application and it doesn't have a GridSelectionSettings tag defined either and yet it allows me to select text. I stripped my grid down to the bare minimum and it still has the k-user-select-none class applied to it. So it's as if something external to the grid is causing that CSS class to get applied. One thing that's different about this app than my other one with the grid is that this one uses a TelerikDrawer. Whether that has any effect or not I don't know but I'll mention it just in case it triggers any thoughts. If needed I can try and write you a runnable repro at some point but at the moment I'm a bit under deadline pressure so I need to keep moving forward but if you have any thoughts on this they would be appreciated. Thanks.

### Response

**Hristian Stefanov** commented on 11 Nov 2024

Hi Doug, As of version 6.2.0, I can confirm that cell selection in the Grid is enabled by default when selection is used, with the DragToSelect parameter also set to true by default. To remove the " k-user-select-none " CSS class, you’ll need to manually disable this option. I've updated the documentation to clarify this behavior, and the changes will be live shortly. In summary, starting with version 6.2.0, this CSS class appears by default when using selection in the Grid, and you can remove it by manually disabling the parameter. Kind Regards, Hristian

### Response

**Doug** commented on 11 Nov 2024

Thanks Hristian. I'm on v6.2.0 and what I've observed is that if I don't enable selection then cell selection is also no longer enabled which falls in line with what you've stated above. However, even though cell selection is not enabled, k-user-select-none still gets applied and I can't select text. So it appears that even without selection enabled, if I want to select text I have to explicitly disable DragToSelect. That also means I need a GridSelectionSettings element when I don't have selection enabled which seems a little counterintuitive.

### Response

**Hristian Stefanov** commented on 12 Nov 2024

Hi Doug, I apologize if my previous message caused any confusion. What I meant to convey is that when cell selection is enabled, the " DragToSelect " parameter is " true " by default, which results in the application of the " k-user-select-none " CSS class. If cell selection is not enabled, or if the " DragToSelect " parameter is set to " false ", this CSS class will not be applied, which is the expected behavior. Here is a demo for reference where cell selection is disabled, but row selection is enabled, and the " k-user-select-none " class is not applied. If you're still encountering issues, please share a small, runnable reproduction of your Grid configuration so I can better understand the scenario. Kind Regards, Hristian
