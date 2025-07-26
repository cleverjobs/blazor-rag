# Add Missing Text Colors to Blazor Editor

## Question

**TimTim** asked on 15 Mar 2022

Hi, How do I add colors to the Editor text color picker in the editor? The colors Red, Purple, Pink, etc are missing from the color picker. The editor can support the missing colors, but they are included in the color picker. Thanks,

## Answer

**Apostolos** answered on 18 Mar 2022

Hi Tim, The built-in color tools expose a Colors property which allows you modify the color palettes in one of the following ways: Provide a member of ColorPalettePresets which gives you a variety of predefined color palettes. Create a new custom list with colors using the supported formats. Take a look at the color tool customization documentation article which includes a runnable example for both options. I hope you find the above information useful. Regards, Apostolos Progress Telerik
