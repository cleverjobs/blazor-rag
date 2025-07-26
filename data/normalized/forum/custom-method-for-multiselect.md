# custom method for multiselect

## Question

**n/an/a** asked on 18 Mar 2022

Hello, Any way possible that a custom method can be fired using the selected items from multiselect. There is absolutely no where in the documentation to specify this. It is only provided SelectedItemsChanged that takes lambda. When trying to fire a custom method on selected items when the user clicks a button, the follwing error is thrown: Argument 2: cannot convert from 'method group' to 'EventCallback'. It is provided a link below : The lambda expression in the handler is required by the framework: [https://github.com/aspnet/AspNetCore/issues/12226.](https://github.com/aspnet/AspNetCore/issues/12226.) It doesn't really make sense why this link has been provided as it takes you to a blog page and absolutely no solution is provided. So may I ask, how do you fire a custom method only on the selected items? Thank you. 7 Kind regards

## Answer

**Marin Bratanov** answered on 18 Mar 2022

Hi, Please review the available events in the component to see which one will suit your needs - likely ValueChanged, OnChange or OnBlur: [https://docs.telerik.com/blazor-ui/components/multiselect/events.](https://docs.telerik.com/blazor-ui/components/multiselect/events.) You can get the user selection via the Value parameter. You may also find useful this article on the concepts of data binding and value binding: [https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding.](https://docs.telerik.com/blazor-ui/getting-started/value-vs-data-binding.) Regards, Marin Bratanov
