# The/All Color Tool

## Question

**Doo** asked on 22 Dec 2020

Hi! I need to have a proper color palette in the editor as a toolbar that should appear if Tools="@EditorToolSets.All" is applied. I need to have an editor with descent background, highlight, and foreground/font color.

## Answer

**Marin Bratanov** answered on 22 Dec 2020

Hi Hassan, You can Follow the implementation of a built-in tool for that here: [https://feedback.telerik.com/blazor/1480866-text-color-pickers.](https://feedback.telerik.com/blazor/1480866-text-color-pickers.) I've added your Vote for it, and the thread offers a workaround you can implement for the time being. Regards, Marin Bratanov

### Response

**DoomerDGR8** answered on 22 Dec 2020

Thank you for the lightning-fast reply. I went through what you've shared. Now, the follow-up question: can the KendoBlazor ColorPicker be placed on the Custom Toolbar of the Editor? If so, can the editor's color (background or foreground be bound to whatever was selected in the ColorPicker?

### Response

**Marin Bratanov** answered on 22 Dec 2020

Hello Hassan, You can implement your own color picker based on the kendo picker as explained here [https://github.com/telerik/blazor-ui/tree/master/common/kendo-in-blazor.](https://github.com/telerik/blazor-ui/tree/master/common/kendo-in-blazor.) Then, use that as a custom tool like shown in the demo: [https://demos.telerik.com/blazor-ui/editor/custom-tools.](https://demos.telerik.com/blazor-ui/editor/custom-tools.) The page I previously linked is where you can get notifications for when such a feature becomes available out-of-the-box. At the moment, there isn't a ready-made option for this yet. On another note - the Kendo UI widgets are jQuery widgets, and the UI for Blazor components are native Blazor components so they don't rely on jQuery and they don't wrap Kendo widgets. Thus, since there isn't a Blazor ColorPicker yet (you can Follow that here ), the only option i could suggest is rolling out your own - either by basing it on the jQuery widgets as per the idea above, or creating something entirely your own (say, a dropdown list with a few colors). Regards, Marin Bratanov
