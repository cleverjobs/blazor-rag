# Mismatch between what is visualized in the drop-down list VS what is visualized in the input box

## Question

**NiV** asked on 19 Aug 2023

Hi there. I'm using the MultiSelect component and limiting how many items the user can select from the drop-down list. I've used the following guide to achieve that goal (specifically the first code snippet in the "Solution" section): [https://docs.telerik.com/blazor-ui/knowledge-base/multiselect-always-select-item-limit-total#solution](https://docs.telerik.com/blazor-ui/knowledge-base/multiselect-always-select-item-limit-total#solution) Adding the AutoClose="false" instruction in the TelerikMultiSelect element and selecting more than one item will create a mismatch between what is seen in the drop-down list VS what is seen in the input box. Losing focus of the component and then regaining focus of it will show the correct items that have been selected, but deselecting the items in this state will also create the mismatch mentioned. The following gif showcases both situations: [https://i.gyazo.com/9ad670d9b3cffc3d0b43cb457bb57a6d.mp4](https://i.gyazo.com/9ad670d9b3cffc3d0b43cb457bb57a6d.mp4) Here is the REPL link: [https://blazorrepl.telerik.com/cdkCbXcm22boLMeV33](https://blazorrepl.telerik.com/cdkCbXcm22boLMeV33) The issue does not happen because of the "static item" used in the example; here is a REPL link which has the code about the "static item" removed: [https://blazorrepl.telerik.com/mHEsFjwQ26ywR1tD29](https://blazorrepl.telerik.com/mHEsFjwQ26ywR1tD29)

## Answer

**Georgi** answered on 23 Aug 2023

Hi, Fabio, Thank you for the detailed explanation and provided examples. Indeed, there is a discrepancy between the highlighted items and the actually selected items in the input. I logged a bug report in our feedback portal on your behalf. You will be automatically notified of any status changes regarding this item. Kind regards, Georgi Progress Telerik
