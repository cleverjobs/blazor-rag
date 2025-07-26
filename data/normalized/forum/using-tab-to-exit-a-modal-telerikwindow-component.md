# Using tab to exit a modal TelerikWindow component

## Question

**Tac** asked on 06 Jul 2022

Hi all, We have a Blazor Server app that uses Telerik for Blazor 3.4.0 We noticed that when we have TelerikWindow component where the Modal=true is defined, users can still use the tab button to navigate outside of the pop up. They can even access the actions and dropdowns on the site behind the TelerikWindow. We tested this on Edge, Chrome, and Firefox. From this documentation it seems that we'd only need to set Modal="true" for a TelerikWindow component to behave similar to a TelerikDialog component: [https://docs.telerik.com/blazor-ui/components/window/modal](https://docs.telerik.com/blazor-ui/components/window/modal) You can even observe this behavior in the Telerik REPL: Here is a TelerikDialog component: [https://blazorrepl.telerik.com/QcOVYAGb10rFakuj32](https://blazorrepl.telerik.com/QcOVYAGb10rFakuj32) Here is a TelerikWindow component with Modal="true": [https://blazorrepl.telerik.com/wGOhYUQv27XDlK8506](https://blazorrepl.telerik.com/wGOhYUQv27XDlK8506) Thanks

## Answer

**Dimo** answered on 08 Jul 2022

Hello Jon, Indeed, modal Windows can prevent tabbing to outside content, but this needs to be specifically implemented. While we do this, I can suggest the included workaround on the linked page. You can also use the Dialog, if you don't need features such as Window dragging or resizing. I also voted on your behalf to raise the request's priority. Regards, Dimo Progress Telerik

### Response

**TacoWombat** commented on 08 Jul 2022

Hi Dimo, Thanks for the workaround! Hopefully this feature will be added to the implementation plan soon. Since the feature request ([https://feedback.telerik.com/blazor/1528232-modal-window-should-trap-the-tab-keys-so-you-cannot-focus-content-behind-the-window)](https://feedback.telerik.com/blazor/1528232-modal-window-should-trap-the-tab-keys-so-you-cannot-focus-content-behind-the-window)) is still set to "unplanned", will the documentation be updated to include the work around? Jon

### Response

**Dimo** commented on 11 Jul 2022

Hi Jon, Yes, we can mention non-existent features or workarounds in the Knowledge Base section. I have logged an internal task.
