# Input gets focused on Cancel or Set

## Question

**Zhi** asked on 02 Feb 2021

Based on the example [https://demos.telerik.com/blazor-ui/datetimepicker/overview,](https://demos.telerik.com/blazor-ui/datetimepicker/overview,) on Cancel or Set, the Input gets focused. On the mobile, it causes the keyboard to appear as well, which is not an intuitive behaviour. Is it possible for this behaviour to be removed? Thanks!

## Answer

**Marin Bratanov** answered on 02 Feb 2021

Hi Zhi Yuan, Generally speaking from an accessibility point of view, popups must have a default focus (we do that), and when they close, they must return the user to the flow of the application in the place where they took it from. In this case, that's an interaction with the picker component. That said, I have logged an enhancement idea so that this does not happen: [https://feedback.telerik.com/blazor/1505044-avoid-input-focus-after-interacting-with-the-popup-of-the-pickers-in-order-to-prevent-the-soft-keyboard-from-showing.](https://feedback.telerik.com/blazor/1505044-avoid-input-focus-after-interacting-with-the-popup-of-the-pickers-in-order-to-prevent-the-soft-keyboard-from-showing.) You can Follow its status in the portal. Regards, Marin Bratanov
