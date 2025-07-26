# DropDownList with optional input

## Question

**Jer** asked on 18 Mar 2022

I want to provide a dropdownlist with some known values. There is a chance that the user will want to input another value other than in the dropdown. Is there an example of having a dropdown list with either a optional value that can be specified in a textbox or such?

## Answer

**Marin Bratanov** answered on 19 Mar 2022

Hi Jerdobi, The combobox can let the user input custom values, but they must then be strings as it is a mere text input in this case: [https://docs.telerik.com/blazor-ui/components/combobox/custom-value.](https://docs.telerik.com/blazor-ui/components/combobox/custom-value.) For other intents and purposes, the combo box works mostly like the dropdownlist and has the same set of events, behaviors and functionality. If you want the users to edit the data, you may want to consider a grid, or a dedicated button in the header/footer template of the dropdown to open a dialog to let them add the desired new value. The following enhancement would also let you put a grid in a dropdown: [https://feedback.telerik.com/blazor/1506370-dropdown-container-popup-component-tied-to-an-anchor-for-positioning.](https://feedback.telerik.com/blazor/1506370-dropdown-container-popup-component-tied-to-an-anchor-for-positioning.) It also links ideas for dedicated dropdown grids and other similar components. If you find any of these interesting, you can use the supplied sample snippets for the time being, and also Vote for and Follow the enhancements you find useful. Regards, Marin Bratanov
