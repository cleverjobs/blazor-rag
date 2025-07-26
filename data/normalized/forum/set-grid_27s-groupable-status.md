# Set grid's groupable status

## Question

**Ric** asked on 12 Feb 2021

On my own machine in visual studio this works, but it only works sometimes on the web server. Essentially when the grid loads the first time, I set it as non groupable because the items in the grid at that time do not need to be grouped, there are only ever a few items at this stage. Depending on other events that happen, the amount of data in the grid changes and I change it to groupable. I do this with a Boolean such as in the attached file. Depending on the boolean, I change it to true or false. This is working fine on my own machine in Visual Studio, and it seems to work fine on the web server on the first load when the web app wakes up for the first time, but doing a page refresh then it doesn't work anymore. Seems like having a slight delay allows it to set some stuff maybe, but on refresh it's too quick? I get the drag and drop bar but I can't drag any fields, it's like all fields have been set to non groupable. Maybe I am trying to be too fancy changing up the grouping ability?

## Answer

**Marin Bratanov** answered on 17 Feb 2021

Hello Rick, I've logged this for improvement and you can Follow its status here: [https://feedback.telerik.com/blazor/1507313-cannot-toggle-groupable-at-runtime.](https://feedback.telerik.com/blazor/1507313-cannot-toggle-groupable-at-runtime.) The page also offers a workaround that I hope would serve for the time being. Regards, Marin Bratanov
