# Is it possible to overwrite or expose the GetEnumData function of the TelerikEnumEditor?

## Question

**Mat** asked on 31 Jan 2024

I am trying to create dropdowns in my filter and I see there is an item that is currently unscheduled but am looking for a solution I can implement now Unplanned feature looking at the TelerikEnumEditor I see that the enums are doing exactly what I need but I need to change the Data Dictionary<int,string> to my own data. I have found a way to overwrite the GetEnumData function but it's not passing the information it's altering it within the class, Is there a way for me to access the Data member of the component when I am defining my filter fields or pass it along with it? or are there other alternatives I have missed? Thanks Matt

## Answer

**Svetoslav Dimitrov** answered on 05 Feb 2024

Hello Matt, Our components work with default enum values, which are of int type. We have an open feature request for the support of Enum values different than int. Do you have a custom Enum that overrides the default enum int values? I am curious to find out more about the scenario you are having as there might be other alternatives as you mentioned. Regards, Svetoslav Dimitrov Progress Telerik
