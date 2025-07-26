# Icon for TelerikMultiSelect in Blazor.

## Question

**Sou** asked on 04 Jun 2021

Hi All, Can any one help me to integrate a dropdown icon in TelerikMultiSelect component in blazor. Thanks in advance

### Response

**Alan** commented on 05 Jan 2022

Can do this with css. something like: .k-multiselect.k-searchbar:after { width: 1em; height: 1em; content: "\e006"; outline: 0; font-size: 16px; font-family: 'WebComponentsIcons', serif; font-style: normal; font-weight: 400; line-height: 1; speak: none; text-transform: none; text-decoration: none; position: absolute; right: 5px; top: 5px; display: inline;
}.k-multiselect.k-reset +.k-searchbar:after { display: none;
}
