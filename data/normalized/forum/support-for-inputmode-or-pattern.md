# Support for inputmode or pattern?

## Question

**Lar** asked on 11 Feb 2020

Is their currently a way to specify either inputmode="decimal" or pattern="\d*" so that an iPhone will present a user with a number only keyboard with a decimal in the case of inputmode="decimal" or a number only keyboard without the decimal key in the case of pattern="\d*"? Currently if I try to add it directly in to the HTML I get an InvalidOperationExecption specifying that the TelerikNumericTextBox does not have a property matching the name 'inputmode'.

## Answer

**Marin Bratanov** answered on 12 Feb 2020

Hello Larry, At the moment, you can use a "regular" input where you can add such attributes, and style it like ours: [https://docs.telerik.com/blazor-ui/themes/form-elements#inputs.](https://docs.telerik.com/blazor-ui/themes/form-elements#inputs.) In the meantime you can also try our numeric textbox that limits the input too (even if the user writes letters, there is an indication they are not allowed): [https://demos.telerik.com/blazor-ui/numerictextbox/validation](https://demos.telerik.com/blazor-ui/numerictextbox/validation) Components (such as ours or any component you make in your app) will throw such exceptions when a parameter is used that is not implemented. There are two solutions to this: implementing the parameter in question implementing attribute splatting You can Follow the implementation of additional attributes or attribute splatting for the Telerik textbox in these pages (at this point I don't know if attribute splatting will be implemented, or explicit parameters): [https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes](https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes) [https://feedback.telerik.com/blazor/1416922-add-to-teleriktextbox-more-parameters-such-as-type-autocomplete-required-readonly](https://feedback.telerik.com/blazor/1416922-add-to-teleriktextbox-more-parameters-such-as-type-autocomplete-required-readonly) I also logged here an enhancement idea that the NumericTextBox we have should render type=number to guide mobile devices for the proper keyboard type, so you can Follow it too: [https://feedback.telerik.com/blazor/1453380-numerictextbox-should-render-inputmode-decimal-out-of-the-box.](https://feedback.telerik.com/blazor/1453380-numerictextbox-should-render-inputmode-decimal-out-of-the-box.) I must also note that a keyboard for a mobile device must be accompanied by proper validation on the server, because a user can always tamper with the input, and desktop users with physical keyboards do not benefit from customized virtual layouts. So, you may want to add a data annotation validation anyway, or use our numeric textbox that does not accept anything but numbers. Regards, Marin Bratanov

### Response

**Larry** answered on 12 Feb 2020

Thank you for the suggestions. It is not the end of the world if the functionality is not there but it just makes for a nicer end user experience on a mobile device.
