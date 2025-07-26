# Issues with validation across multiple tabs

## Question

**BenBen** asked on 21 Jun 2022

I have an EditForm with a TabStrip and multiple tabs each with required fields. I'm finding that validation finds the required fields only on tabs that were active at some point and had their contents loaded into the DOM. If the user never selects the tabs, validation will skip some required fields. We have a workaround where each tab is quickly activated after the first render but I'm hoping there is a cleaner solution. Is there a way to tell Telerik to load all tabs into the DOM on initialization?

## Answer

**Nadezhda Tacheva** answered on 24 Jun 2022

Hi Ben, The TabStrip has a Persist Content functionality that allows keeping the tabs content in the DOM while switching the active tabs. However, in order to have the tab content rendered in the DOM in first place, one must first activate the specific tab. It wouldn't be optimal to render the content of all tabs on initialization - a very common scenario is that some tabs are never even activated, so what will be the purpose of having their content in the DOM then, this will affect the performance of the component. As far as I can understand your scenario, the user has to go through all of the tabs to successfully submit the form as all of them contain required fields. In this case, I would recommend considering the Wizard component. It allows Form integration and you can easily prevent the user from submitting the form if there are some invalid fields. Take your time to revise it and please let me know if any questions are raised. Regards, Nadezhda Tacheva

### Response

**Ronnie** commented on 14 Nov 2024

What you are saying is that if developers have required fields on several tabs, they should use another control. This is not good enough. It is usual to present fields on several tabs and validate the fields across the form before it can be saved. This is common in user interfaces. In Windows applications, this can be implemented without any problems or workarounds. Validation should not need to rely on a user to select all the tabs where fields require validation. Telerik must provide developers with a way to validate fields across several tabs without requiring developers to use workarounds. Perhaps this can be something for Telerik to implement in the TabStrip control for the next release of Telerik UI for Blazor.

### Response

**Nadezhda Tacheva** commented on 19 Nov 2024

Hi Ronie, To clarify, I am not saying that it is necessary to use another control. You can, of course, use the TabStrib. I just recommend the Wizard component for better management of the required tabs. Let me share some more details. From UX perspective, I find it odd that a tab contains some required fields and yet the user is able to skip those tabs (not activate them at all). The TabStrip component does not provide an option to force the user to activate a specific tab. The Wizard, on another hand, does. For example, you can use the linear flow feature to ensure the user will go through all needed steps to fill all the required fields. At this stage, I am not aware of your exact implementation. If you want to fire validation for the fields in tabs that are not yet activated, you can use one Form and spread its fields throughout the tabs. You can use our demo for reference: Form - Templates.
