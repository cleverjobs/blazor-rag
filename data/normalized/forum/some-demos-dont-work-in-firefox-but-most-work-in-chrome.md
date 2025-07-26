# Some demos dont work in Firefox but most work in Chrome?

## Question

**Bit** asked on 14 Oct 2019

Anxious to get started with Blazor components, especially the grid. I was browsing the various demos and noticed some didnt seem to respond in Firefox. Opened them in Chorme and they worked. The grid however works fine in Firefox 69.0.2 (64-bit), Windows 10 examples: (1) Menu. Items wont drop down [https://demos.telerik.com/blazor-ui/menu/overview](https://demos.telerik.com/blazor-ui/menu/overview) (2) Dropdown list. Items wont drop down [https://demos.telerik.com/blazor-ui/dropdownlist/overview](https://demos.telerik.com/blazor-ui/dropdownlist/overview) There may be others, but both of the above worked ok in Chrome

## Answer

**Marin Bratanov** answered on 14 Oct 2019

Hello, We are aware of this problem and we are working on it. It's a bug in our code related to FF and that's why things work fine in Chrome. We will do our best to have it fixed in our upcoming release. Regards, Marin Bratanov

### Response

**BitShift** answered on 14 Oct 2019

Ok, thanks. Wont stop us from using Blazor though, as our first few projects will be intranet type apps and our group all uses Chrome as the standard install.

### Response

**Marin Bratanov** answered on 17 Oct 2019

Hi, This turned out to be a mix between browser behavior and the default template styling. It will be documented and you can preview the information here. Regards, Marin Bratanov
