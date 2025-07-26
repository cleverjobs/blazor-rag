# FormItem "Enabled" attribute in example code causing an error "...does not have a property matching the name..."

## Question

**Jes** asked on 03 Jun 2021

Hi, When I try to run the example on the following page I get an error: Page: [https://docs.telerik.com/blazor-ui/components/form/formitems/overview#customize-the-appearance-of-the-editors-in-the-form](https://docs.telerik.com/blazor-ui/components/form/formitems/overview#customize-the-appearance-of-the-editors-in-the-form) Error: Unhandled exception rendering component: Object of type 'Telerik.Blazor.Components.FormItem' does not have a property matching the name 'Enabled'. Additionally, the example that uses the "[Editable(false)]" attribute on the model attached to the form does not render the control in a disabled state, as stated. (Example on this page: [https://docs.telerik.com/blazor-ui/components/form/overview](https://docs.telerik.com/blazor-ui/components/form/overview) ) Any help would be appreciated. Thank you, Jesse

## Answer

**Svetoslav Dimitrov** answered on 08 Jun 2021

Hello Jesse, As an attached file I have added a demo application that uses the Telerik UI for Blazor Form component to showcase how to disable a form item by using the [Editable(bool value)] data annotation attribute, using a template to disable an item, disable the form item using the Enabled parameter, and the difference between the disabled fields and an enabled one. Could you run the application and see if it works as expected for you? If it does you could compare it against your own and see if any differences are causing the issue. If this does not help you could modify the application so that the issue is reproducible so that we can further investigate. Regards, Svetoslav Dimitrov Progress Telerik
