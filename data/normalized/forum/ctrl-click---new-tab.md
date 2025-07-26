# Ctrl+Click -> New Tab

## Question

**n/an/a** asked on 17 Nov 2020

I've been testing the Telerik Blazor out and one thing that seems to be missing is the ability to Ctrl+Click to open items in a new tab. Is there a way to use OnClick with event args so you can see if ctrl+click was used?

### Response

**Jake** commented on 23 Nov 2021

Has this been answered someplace else? I do not see any anchor links when using the Menu for naviagtion. Do I have to create a template? I don't want to do that because my Nav model does the automatic binding and I don't want double navigation. This is the HTML that get generated. (Version: 2.29.0)

### Response

**Svetoslav Dimitrov** commented on 26 Nov 2021

Hello Jake, To achieve the desired behavior you should indeed use the Template. Another useful thing you can do is to rename the field in the model that automatically does the binding (for example, if the name of the field is "Url" you should change it to something different). By changing the name of the field you will avoid double navigation issues.

### Response

**Jake** commented on 26 Nov 2021

Hi Svetoslav, I did rename the field and use a template. I'm just lazy and wanted use all the automatic bindings. Thank you.

### Response

**Svetoslav Dimitrov** commented on 01 Dec 2021

Hello Jake, I am happy to read that everything works as expected for you now! If you have any further questions do not hesitate to contact us!

## Answer

**Svetoslav Dimitrov** answered on 20 Nov 2020

Hello Dustin, As an attached file you could see an application, which references Telerik UI for Blazor 2.19.0 and has a menu component used for navigation (with URL field) in the Index page. When we render the menu the elements used for navigations are <a> tag with href attribute where you can use the Control + Click combination to open in a new browser tab. Could you run the application and if it works as expected for you, compare it against your own to see if any difference causes the issue. If this does not help or if I have misunderstood the question, could you modify the application so that the behavior is reproduced and I can investigate further? Regards, Svetoslav Dimitrov
