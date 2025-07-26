# Master/detail in a tab strip content area

## Question

**Jst** asked on 15 Dec 2022

I have a Grid page in the content section of a TabStrip. I am trying to determine the best way to move from the grid to a detail page but still maintain the TabStrip. I want the detail page to stay in the same tab as the grid page was. I assume some sort of component swap process? Any suggestions

## Answer

**Nadezhda Tacheva** answered on 20 Dec 2022

Hi John, I can suggest different options depending on the exact scenario you want to achieve. For example, if you want to display details for the specific items of the Grid, you may use the DetailTemplate. Thus, the Grid rows will be expandable and you can render the desired content for each item based on the template context. If, on another hand, you want to display some general information in a dedicated details section, you may use conditional rendering for the elements. Here is a runnable sample demonstrating the approach: [https://blazorrepl.telerik.com/wmlQGkbY50Qxp5SV52.](https://blazorrepl.telerik.com/wmlQGkbY50Qxp5SV52.) You may additionally enable the PersistTabContent feature, so the state is not lost when switching between the tabs. I hope you will find the above information useful to move forward with your application. Please let us know if any other questions appear. Regards, Nadezhda Tacheva
