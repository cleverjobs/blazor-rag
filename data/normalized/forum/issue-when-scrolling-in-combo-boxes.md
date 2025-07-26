# Issue when scrolling in combo boxes?

## Question

**And** asked on 14 Feb 2023

When scrolling down in the virtualized combo boxes, anything typed into the text box will reset to the initial value. To see this behavior, visit the combo box doc for virtualization: [https://docs.telerik.com/blazor-ui/components/combobox/virtualization.](https://docs.telerik.com/blazor-ui/components/combobox/virtualization.) In the Local data example, click preview. Then type “Na” in the input box. Then scroll down in the list of popup options. The “Na” in the input box disappears. In the Remote data example, click preview. Then click inside the input box where it says “Name 1234”. Click backspace a couple times so the input becomes “Name 12”. Then scroll down in the list of popup options. The input resets to “Name 1234”. The same behavior happens in the remote data example for the multi column combo box: [https://docs.telerik.com/blazor-ui/components/multicolumncombobox/virtualization](https://docs.telerik.com/blazor-ui/components/multicolumncombobox/virtualization) Is there a way to prevent the typed input from resetting when the user scrolls?
