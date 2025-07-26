# Not assign k-state-valid class on form creation

## Question

**Way** asked on 23 Nov 2020

I am using a Combobox (probably the same for all editors) and it is auto assigned the k-state-valid class upon creation. I would like to have this class only be assigned once the Forms Validate method is called. Is there a way to do this?

## Answer

**Marin Bratanov** answered on 23 Nov 2020

Hi Wayne, I'm afraid this is not possible, these classes reflect the current validation state of the component and the component assigns them on its own internally. If you set an invalid value (either manually, or through code), the component will switch it out with the invalid class to provide the red border that one expects when having an invalid input. When the component becomes valid that updates as well. Our validation happens in the oninput (ValueChanged) event, not delayed to events like onchange. Could you provide some more details on why this class is a problem, because I am not aware of situation where it is? Regards, Marin Bratanov

### Response

**Wayne Hiller** answered on 23 Nov 2020

The situation is that I am using the Telerik controls with others from Blazorise (Bootstrap). The Bootstrap theme adds a green border and check mark when an input is changed by the user or the form is validated if it is valid. I have added the styles to make the Telerik inputs look the same. The issue is the Telerik inputs show the Green border immediately because they start out with the k-sate-valid class. I might be able to add a class like can-validate to the Telerik inputs upon focus (or when the form is validated), then base my .k-state-valid style on that.

### Response

**Marin Bratanov** answered on 23 Nov 2020

Hi Wayne, If necessary, you should add CSS rules that remove any Telerik styling you do not wish to see, and add your own classes when/as desired to cascade such customized styling. Internally we set the valid and invalid class based on the edit context data, so they are correct - the fact that this happens on initial rendering is because we should evaluate the initial value too - if it is invalid, there must be an indication. Thus, the behavior is correct and if specific styling is desired, it should be added by the application. Regards, Marin Bratanov

### Response

**Wayne Hiller** answered on 24 Nov 2020

Is it possible to hook into the onfocus event?

### Response

**Marin Bratanov** answered on 24 Nov 2020

Hello Wayne, The following Knowledge Base article shows how: [https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events](https://docs.telerik.com/blazor-ui/knowledge-base/inputs-handle-keyboard-events) Regards, Marin Bratanov

### Response

**Wayne Hiller** answered on 24 Nov 2020

Actually I don't think the inputs are working correctly They start out with a class of k-state-valid but the data model had a Required attribute on it and the data field is empty. They should start with no class or k-state-invalid if they are validated on creation.

### Response

**Marin Bratanov** answered on 24 Nov 2020

Hi Wayne, The class is applied according to what the framework returns for the field state. The fact that initially it considers the form valid is something that is up to the framework. Regards, Marin Bratanov
