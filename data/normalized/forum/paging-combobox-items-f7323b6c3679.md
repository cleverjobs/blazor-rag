# Paging ComboBox items

## Question

**Bog** asked on 19 Mar 2020

Hi, is it possible to combine combobox with paging ?

## Answer

**Marin Bratanov** answered on 19 Mar 2020

Hello Boguslaw, You could use a grid with single selection and place it in an AnimationContainer so it acts like a dropdown. You can also Follow the implementation of a built-in virtualization feature in this page (I added your Vote on your behalf): [https://feedback.telerik.com/blazor/1457808-combobox-virtualization](https://feedback.telerik.com/blazor/1457808-combobox-virtualization) For the time being, custom filtering through the OnRead event can let you optimize the data queries and number of rendered items: [https://docs.telerik.com/blazor-ui/components/combobox/events#onread](https://docs.telerik.com/blazor-ui/components/combobox/events#onread) Regards, Marin Bratanov

### Response

**BobB** commented on 29 Nov 2021

Is paging for a Blazor combobox on the roadmap at all?

### Response

**Marin Bratanov** commented on 01 Dec 2021

In Blazor, what we'd rather do is to have a dropdown grid component, or a dropdown component that lets you put whatever you want in the dropdown (like a grid with paging): [https://feedback.telerik.com/blazor/1496930-dropdown-datagrid](https://feedback.telerik.com/blazor/1496930-dropdown-datagrid) [https://feedback.telerik.com/blazor/1506370-dropdown-container-popup-component-tied-to-an-anchor-for-positioning](https://feedback.telerik.com/blazor/1506370-dropdown-container-popup-component-tied-to-an-anchor-for-positioning) Feel free to Vote for them, and to Follow them for status updates.
