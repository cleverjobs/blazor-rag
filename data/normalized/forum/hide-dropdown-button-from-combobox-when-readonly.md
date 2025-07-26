# Hide dropdown button from combobox when readonly

## Question

**Pau** asked on 27 Sep 2022

Hi Is this possible, can't find it in the documentation? This question is for all components having an (image) button like the calendar This form is read only so the drowdown buttons , the calendar buttons should not be shown. (As also the * required , which we already solved) Eric

## Answer

**Nadezhda Tacheva** answered on 30 Sep 2022

Hi Eric, By design, when the ComboBox is disabled, we are adding, we are adding a "k-disabled" class to its main wrapping element. This class introduces some styling changes that indicate the component is disabled. For example, we are setting less opacity and no pointer events. The component elements (the input, the button that opens the dropdown) remain visible but the user is not able to click them. This applies to other dropdown components and date pickers. If you want to hide the button or the icon, you can achieve that with some custom CSS. The easiest way to proceed is to inspect the rendering using your dev tools, so you can find the correct element you need to additionally style. I would recommend using the "k-disabled" class in the selector to ensure these styles will be applied only to the disabled state of the component. Here is a sample that demonstrates how to hide the buttons in a ComboBox and a DatePicker. You may use it as a base to customize the components in your application: [https://blazorrepl.telerik.com/mQYNxaOs087e8slj51](https://blazorrepl.telerik.com/mQYNxaOs087e8slj51) I hope the above-listed information and sample will help you move forward. Please let us know if you are experiencing any difficulties. Regards, Nadezhda Tacheva Progress Telerik

### Response

**Paul** commented on 05 Oct 2022

Hi Nadezhda Nice solution, thanks! Paul

### Response

**Paul** answered on 30 Sep 2022

Hi Ok i understand , but a property like "HideButtonOnReadOnly" would be a nice feature to have for all developers. Can you add this to the feature list? Paul

### Response

**Nadezhda Tacheva** answered on 05 Oct 2022

Hi Paul, Such a property would interfere with the design we have incorporated for the disabled state of the select and date/time picker components. The Telerik UI products share a unified design, so the same behavior can be observed in our other suites. By design, the button remains visible but the whole component has less opacity and no pointer events. While we've considered that the current styles clearly indicate to the user that the components are disabled, one can of course customize them as needed using the approach listed above. Regards, Nadezhda Tacheva Progress Telerik
