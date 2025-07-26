# ComboBox; MultiSelect

## Question

**joh** asked on 13 Apr 2021

Basically anything with a drop down container does not show on Telerik Window. This is nothing fancy and really is weird. If I type something into the combo-box the drop down filtering does not show, but if I press the arrow it shows the data. On Multiselect there is nothing available to click like an arrow so the container never comes to the forefront. I test on a non windowed view and both perform correctly.

## Answer

**Marin Bratanov** answered on 13 Apr 2021

Hi John, This is an issue caused by a new feature in the window, it will be fixed in our next release (2.24.0), and for the time being this workaround will serve: <style>.k-animation-container { z-index: 15000;
}
</style> Regards, Marin Bratanov Progress Telerik
