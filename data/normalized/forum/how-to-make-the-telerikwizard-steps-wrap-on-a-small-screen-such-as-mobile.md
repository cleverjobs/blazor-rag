# How to make the TelerikWizard steps wrap on a small screen such as mobile?

## Question

**JJ** asked on 13 Jul 2021

In the demos, TelerikWizard does not wrap onto multiple lines on mobile. How can I set it so that it wraps onto multiple lines if the steps do not fit on the page?

## Answer

**Nadezhda Tacheva** answered on 14 Jul 2021

Hi Jonathan, In the demo we have set fixed width to the container holding the Wizard for styling purposes. This is expected behavior in cases when the width of a container is fixed. You can also verify that yourself by checking the "View Source" tab in the demo page. If you don't set fixed width to the component or to its parent container, the Wizard will resize accordingly. You can test that in the live demo as well - inspect the parent div of the Wizard, remove its width and see its behavior on mobile devices. I hope you will find that information useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva
