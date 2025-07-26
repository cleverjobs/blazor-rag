# How to get id

## Question

**EdEd** asked on 09 Feb 2020

In the example at the bottom of [https://docs.telerik.com/blazor-ui/components/autocomplete/events,](https://docs.telerik.com/blazor-ui/components/autocomplete/events,) How would I get the id of the selected car in the Change event? Seems like all I get is the string value. Thanks ... Ed

## Answer

**Marin Bratanov** answered on 09 Feb 2020

Hi Ed, The following article explains how to get an entire model item from a dropdown selection: [https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model](https://docs.telerik.com/blazor-ui/knowledge-base/dropdowns-get-model) The autocomplete (as noted in its documentation and the KB) is a free text input for the user, and the dropdown is only a set of text suggestions for the user, this is a key difference between that and other dropdowns - it is basically a textbox. Regards, Marin Bratanov

### Response

**Ed** answered on 09 Feb 2020

It almost sounds like I should be using the dropdownlist instead. It kinda raises the question, why use an autocomplete in the firstplace if I can get the desired functionality out of a ddl? Thanks ... Ed

### Response

**Marin Bratanov** answered on 10 Feb 2020

Hello Ed, Most dropdowns have similarities and which one you would use is up to the particular needs and UX you want. Here are a couple of differences between the DropDownList and the AutoComplete: the autocomplete value is always a string, while the ddl can also work with number values, guid and enums the autocomplete is a free text input, like a simple <input> but with suggestions the user can pick from, while the ddl only allows choice from a predefined collection of options the autocomplete offers filtering of the results, including custom filtering, while the dll (at this point) does not. When it does, the UX will be different - filtering in the dll is usually a filter textbox in the dropdown as opposed to typing directly in an input Regards, Marin Bratanov

### Response

**Diego Modolo** answered on 27 Apr 2020

I've tried to use the above example with AutoCompleteBox, but it does not have the TextField property. Is there another way of achieving the behavior without this property?

### Response

**Marin Bratanov** answered on 27 Apr 2020

Hi Diego, The auto complete component is a free text input with facilities for the end user, but it is only a text input. For your case, I suspect you will need a ComboBox. I suggest you review the AutoComplete documentation for more details, and especially the green box right after the screenshot: [https://docs.telerik.com/blazor-ui/components/autocomplete/overview.](https://docs.telerik.com/blazor-ui/components/autocomplete/overview.) Regards, Marin Bratanov
