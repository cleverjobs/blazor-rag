# How to change the color of the chips within the ChipList component?

## Question

**RicRic** asked on 21 May 2024

Hello, I am currently experimenting with the ChipList component and the documentation suggests that it delivers the same customization options as the Chip component. However, I am unable to find a way to change the ThemeColor of the chips. Is this feature supported, and if so, how can it be implemented? Reference that suggests this is possible: Blazor ChipList Customization Built on top of the existing Blazor Chip component, the Telerik UI for Blazor ChipList delivers the same customization options to meet any design requirements. These include the color and style of the ChipList, whether to display a close or delete icon and whether to add avatars or images as part of the ChipList content. Thanks

## Answer

**Nansi** answered on 24 May 2024

Hi Ric, I confirm that setting the chip color in the ChipList is not a straightforward approach, as it is in the Chip. The reason is that in the ChipList we are setting the ChipList properties. If we expose the ThemeColor it will be applicable for the ChipList and for all chips in the collection. I will discuss with our development team if it is possible to add the color as a data binding parameter. If this is possible and it will meet your requirements, I will log this as a feature request. I will come back to you by the end of the next week. In the meantime here are some options to set chip colors in the ChipList: 1. One color for all chips Set the ChipList Class parameter to target a specific ChipList. Target the element of the chip with.k-chip and set the color CSS rule. Here is a REPL example. 2. Different colors for each chip Add a color property in the model. Use the ChipList ItemTemplate. Wrap the rendering of the chips in a <div>. Set the model color property as color CSS style to the <div>. Here is a REPL example. 3. Theme You can set a theme for the project. With this approach, you will set the theme for the whole project and not just for the ChipList. Regards, Nansi Progress Telerik

### Response

**Karl** commented on 27 Nov 2024

Hey Nansi, Has there been any movement on this? I have a need to set the color of chips based on the ChipItem data. Using option 2 seems to only set the inner color of the chip and it makes it look pretty weird. This wouldn't be a terribly hard component to recreate with the funcationality - but I'd rather not if Teleriks can do it.

### Response

**Dimo** commented on 28 Nov 2024

@Karl - we have a public feature request about ChipList colors. It's not very popular now, so it may have to wait for some more customer demand. I voted on behalf of you and Ric.

### Response

**Michael** answered on 17 Jan 2025

Hi Ric, simply overwrite the css class for the selected Item For example .k-chip-solid-base.k-selected { background-color: red !important; color: white !important; } Regards, Michael
