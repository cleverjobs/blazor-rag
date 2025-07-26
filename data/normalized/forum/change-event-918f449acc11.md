# Change Event

## Question

**Ric** asked on 21 Aug 2019

OnChange doesn't seem to be working for me, is there an example somewhere? Not seeing the event in the documentation.

## Answer

**Marin Bratanov** answered on 22 Aug 2019

Hello Rick, The following snippet shows how to handle the ValueChanged event (the only event the DropDownList component has right now): [https://docs.telerik.com/blazor-ui/components/dropdownlist/overview#examples.](https://docs.telerik.com/blazor-ui/components/dropdownlist/overview#examples.) Regards, Marin Bratanov

### Response

**Rick** answered on 22 Aug 2019

Works perfect, thank you.

### Response

**Ivan** answered on 20 May 2020

This appears to have changed, and does not show the use of the ValueChanged event. I simply cannot get this to work..

### Response

**Svetoslav Dimitrov** answered on 20 May 2020

Hello, You can see how to handle the ValueChanged event for the DropDownList from our documentation from this link: [https://docs.telerik.com/blazor-ui/components/dropdownlist/events#valuechanged.](https://docs.telerik.com/blazor-ui/components/dropdownlist/events#valuechanged.) Regards, Svetoslav Dimitrov

### Response

**Mark** answered on 20 May 2020

Getting closer, thanks Svetoslav. The example provided doesn't appear to work for more complex types, or through the use of data binding (@bind-Value)? There is an OnChange event however this seems to get fired with no arguments and without updating the bound value..

### Response

**Marin Bratanov** answered on 20 May 2020

Hello Mark, The <ParameterName>Changed events don't allow @bind-<ParameterName> - that's how the framework operates. In fact, the <ParameterName>Change events exist to provide the @bind-<ParameterName> functionality, which is why the can't be used together. Thus, if you want two-way binding, you should use the OnChange event we provide specifically. Alternatively, handle the ValueChanged event and simply update the model field, as shown in the docs. On the possible fields - see what the Value parameter of the drpodown can take in the docs (see the bullet about the Value param): [https://docs.telerik.com/blazor-ui/components/dropdownlist/overview#features.](https://docs.telerik.com/blazor-ui/components/dropdownlist/overview#features.) Said shortly, numbers, strings, GUIDs and Enum members can be used. If you want to get an entire model, see here: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model](https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model) On OnChange not working - I'd suggest you open a support ticket and send us a simple runnable snippet that showcases the issue so we can offer a more concrete answer and avoid guessing. You can base it on the documentation example in order to keep it runnable. At the moment, my best guess is that the Value is not a supported type. Regards, Marin Bratanov
