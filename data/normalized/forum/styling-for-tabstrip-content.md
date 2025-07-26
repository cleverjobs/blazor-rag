# Styling for TabStrip Content

## Question

**Tho** asked on 01 Dec 2023

I'm trying to add styling to a specific tabstrip content (e.g. removing the padding). But I can't seem to figure out a way to select the specific tabstrip content. This code: <TelerikTabStrip> <TabStripTab Title="General Info" Class="tab-pane-general-info"> <div class="general-info"></div> </TabStripTab> <TabStripTab Title="Summary" Class="tab-pane-product-list"> <div class="product-list"></div> </TabStripTab> </TelerikTabStrip> Results in the following HTML: I don't have a way to identify the different tab contents. I know I can select on the div I created (.general-info), but I want to remove the padding from the k-tabstrip-content for a specific tab. Any ideas?

## Answer

**Georgi** answered on 05 Dec 2023

Hi, Thoman, Thank you for the provided code snippet and image! Yes, it is possible to remove the padding of a specific TabStrip content. You can use a ternary operator alongside the ActiveTabIndex to conditionally apply a custom style to the TabStrip that removes the padding like this: <TelerikTabStrip @bind-ActiveTabIndex="@ActiveTabIndex" Class=" @( ActiveTabIndex==0 ? " no-padding ": string.Empty ) "> <TabStripTab Title="Tab 1"> Content 1 </TabStripTab> <TabStripTab Title="Tab 2"> Content 2 </TabStripTab> </TelerikTabStrip> <style>.no-padding.k-tabstrip-content { padding: 0;
} </style> Alternatively, you can use the ActiveTabIndexChanged handler to dictate when to apply the custom style. Kind regards, Georgi Progress Telerik
