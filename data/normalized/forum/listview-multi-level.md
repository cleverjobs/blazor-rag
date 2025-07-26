# Listview multi level

## Question

**Ala** asked on 26 Jun 2022

hi, I cannot seem to find multi-level support on the listview like shown in the two examples below from a different Blazor can you please direct me to this feature and usage(if it exists) or give me some hints on how I can Achieve this with this with a combination of existing components Thanks for your help Alain

## Answer

**Dimo** answered on 29 Jun 2022

Hello Alain, Indeed, our ListView does not feature grouping or hierarchy. Here are components that can achieve similar interface: Grid TreeView PanelBar All of the above components can result in a display that is more or less similar to the left screenshot. If you prefer the right one (but without the slide animation), then you can use a single component (Grid or ListView), and change its entire data, depending on user actions. Regards, Dimo Progress Telerik
